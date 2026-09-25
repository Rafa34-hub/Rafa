"""Genera el CRONOGRAMA 26-27 provisional.

1. Distribueix les formacions de FORMACIONS_26-27_PROVISIONAL.xlsx al full
   'CRONO 25-26' (aules GOOGLE / FIREFOX / COPILOT, matí o tarda, 5-6 h/dia),
   respectant caps de setmana (gris), festius (vermell), vacances i les
   cel·les ja ocupades.
2. Crea els blocs de SETEMBRE-DESEMBRE 2027 a partir del CALENDARI LABORAL 2027.
3. Afegeix el full 'PLANIFICACIÓ 26-27' amb el resum de cada formació.

Ús: python generar_cronograma.py FORMACIONS.xlsx CRONOGRAMA.xlsx CALENDARI.xlsx SORTIDA.xlsx
"""
import datetime as dt
import math
import re
import shutil
import sys
import tempfile
import zipfile
from copy import copy

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.styles.colors import Color
from openpyxl.utils import get_column_letter as L

F_FORM, F_CRONO, F_CAL, F_OUT = sys.argv[1:5]
SHEET = "CRONO 25-26"

RED = "FFFF0000"
GREY_2027 = PatternFill("solid", fgColor=Color(theme=2, tint=-0.249977111117893))
VAC_FILL = PatternFill("solid", fgColor=Color(theme=5, tint=0.5999938962981048))
NON_WORK_KINDS = {"FFFF0000", "th0:-0.35", "th2:-0.25", "th5:0.6", "th4:0.6"}
EMPTY_KINDS = {None, "th0:0.0"}

# Offsets dins de cada bloc mensual (fila capçalera = hr)
ROOMS = {  # (aula, torn) -> offset respecte la fila de capçalera
    ("GOOGLE", "matí"): 1, ("FIREFOX", "matí"): 2, ("COPILOT", "matí"): 3,
    ("GOOGLE", "tarda"): 4, ("FIREFOX", "tarda"): 5, ("COPILOT", "tarda"): 6,
}
START = dt.date(2026, 10, 13)   # primer dia planificable (després de l'actualització del 23/09)
END = dt.date(2027, 7, 30)      # últim dia planificable (agost = vacances)


def kind(cell):
    f = cell.fill
    if f is None or f.fill_type is None:
        return None
    fg = f.fgColor
    return fg.rgb if fg.type == "rgb" else f"th{fg.theme}:{round(fg.tint, 2)}"


# ---------------------------------------------------------------- formacions
wf = openpyxl.load_workbook(F_FORM, data_only=True).active
courses = []
for r in list(range(4, 20)) + list(range(49, 53)):
    code, name, hours = wf[f"D{r}"].value, wf[f"E{r}"].value, wf[f"K{r}"].value
    if not name or not isinstance(hours, (int, float)):
        continue
    teacher = wf[f"X{r}"].value or (wf[f"Y{r}"].value if r >= 49 else None) or "PER ASSIGNAR"
    n_ed = int(wf[f"O{r}"].value or 1)
    for ed in range(1, n_ed + 1):
        courses.append(dict(row=r, code=code, name=name.replace("_x0019_ ", "'").replace("_x0019_", "'").replace("\x19", "'"), hours=int(hours),
                            teacher=str(teacher).strip(), ed=ed, n_ed=n_ed))
# Hores facilitades per l'usuari (no consten al fitxer d'origen)
EXTRA_HOURS = {"ADGG0208": 678, "FCOS02": 30, "CTRH0011": 10, "CTRHI0015": 10}
for r, prog in ((21, "CFCC"), (22, "CFCC"), (24, "FORMA I CONTRACTE"), (25, "FORMA I CONTRACTE"),
                (26, "FORMA I CONTRACTE"), (27, "FORMA I CONTRACTE")):
    code = wf[f"D{r}"].value
    courses.append(dict(row=r, code=code, name=f"{wf[f'E{r}'].value} [{prog} - {wf[f'V{r}'].value}]",
                        hours=EXTRA_HOURS[code], teacher="PER ASSIGNAR", ed=1, n_ed=1))
byrow = {}
for c in courses:
    byrow.setdefault((c["row"], c["ed"]), c)

# Ordre de programació, data objectiu, torn preferent i dependències
# (fila origen, edició, data mínima, torn preferent, depèn de)
PLAN = [
    # CFCC (treballadors): FCOS02 i després ADGG0208 (678 h)
    (22, 1, dt.date(2026, 10, 19), "tarda", None),
    (21, 1, dt.date(2026, 10, 19), "tarda", (22, 1)),
    # FORMA I CONTRACTE (aturats): mòduls complementaris i després ADGG0208 (678 h)
    (25, 1, dt.date(2026, 10, 19), "matí", None),
    (26, 1, dt.date(2026, 10, 19), "matí", (25, 1)),
    (27, 1, dt.date(2026, 10, 19), "matí", (26, 1)),
    (24, 1, dt.date(2026, 10, 19), "matí", (27, 1)),
    # MARIA: matins lliures, tardes només 1 formació/mes -> sempre matí
    (8, 1, dt.date(2026, 11, 2), "matí", None),    # ACTIC bàsic comunicació
    (10, 1, dt.date(2026, 11, 23), "matí", None),  # ACTIC bàsic continguts
    (17, 1, dt.date(2027, 1, 11), "matí", None),   # IA ed.1
    (9, 1, dt.date(2027, 2, 1), "matí", (8, 1)),   # ACTIC intermedi comunicació ed.1
    (11, 1, dt.date(2027, 2, 22), "matí", (10, 1)),  # ACTIC intermedi continguts ed.1
    (9, 2, dt.date(2027, 3, 15), "matí", (9, 1)),
    (11, 2, dt.date(2027, 4, 12), "matí", (11, 1)),
    (17, 2, dt.date(2027, 5, 3), "matí", (17, 1)),
    (7, 1, dt.date(2027, 5, 24), "matí", (9, 1)),  # ACTIC avançat
    # ESTHER
    (4, 1, dt.date(2026, 10, 19), "tarda", None),  # Biomagnetisme
    (5, 1, dt.date(2026, 11, 16), "tarda", None),  # Massatge ed.1
    (19, 1, dt.date(2027, 1, 18), "tarda", None),  # Relaxació
    (5, 2, dt.date(2027, 3, 1), "tarda", (5, 1)),  # Massatge ed.2
    # RAMON
    (13, 1, dt.date(2026, 10, 19), "matí", None),  # Coaching
    (18, 1, dt.date(2027, 1, 11), "tarda", None),  # Mindfulness
    (14, 1, dt.date(2027, 2, 15), "matí", (13, 1)),  # Coaching II
    # Sense docent assignat
    (15, 1, dt.date(2026, 10, 19), "tarda", None),  # Català A1
    (16, 1, dt.date(2027, 1, 18), "tarda", (15, 1)),  # Català A2.1
    (12, 1, dt.date(2026, 11, 9), "matí", None),   # Atenció al client
    (6, 1, dt.date(2027, 1, 11), "tarda", None),   # CRM (145 h)
    # CONSORCI - IMPE0110 (LEIRE), mòduls consecutius
    (49, 1, dt.date(2027, 2, 1), "matí", None),
    (50, 1, dt.date(2027, 3, 1), "matí", (49, 1)),
    (51, 1, dt.date(2027, 4, 1), "matí", (50, 1)),
    (52, 1, dt.date(2027, 5, 3), "matí", (51, 1)),
]
assert sorted((p[0], p[1]) for p in PLAN) == sorted(byrow), "falta alguna formació al PLAN"

# ---------------------------------------------------------------- cronograma
wb = openpyxl.load_workbook(F_CRONO)
ws = wb[SHEET]

# Blocs mensuals existents (fila capçalera amb dates)
blocks = {}
for r in range(1, ws.max_row + 1):
    if ws.cell(r, 1).value == "AULA" and isinstance(ws.cell(r, 4).value, dt.datetime):
        d = ws.cell(r, 4).value.date()
        blocks[(d.year, d.month)] = r


def col_of(d):
    return 3 + d.day


def cell_for(d, room):
    hr = blocks[(d.year, d.month)]
    return ws.cell(hr + ROOMS[room], col_of(d))


working, occupied = set(), set()
d = START
while d <= END:
    hr = blocks[(d.year, d.month)]
    kinds = {kind(ws.cell(hr + o, col_of(d))) for o in ROOMS.values()}
    if d.weekday() < 5 and not (kinds & NON_WORK_KINDS):
        working.add(d)
        for room in ROOMS:
            c = cell_for(d, room)
            if kind(c) not in EMPTY_KINDS or c.value not in (None, ""):
                occupied.add((d, room))
    d += dt.timedelta(1)
working = sorted(working)

# Dies ja ocupats per MARIA (IA MARIA a GOOGLE MATINS set.-oct. 2026)
teacher_busy = {}
for d in working:
    if d < dt.date(2026, 11, 1) and (d, ("GOOGLE", "matí")) in occupied:
        teacher_busy.setdefault("MARIA", set()).add(d)


def day_hours(h):
    n = math.ceil(h / 6)
    assert 5 * n <= h <= 6 * n
    k6 = h - 5 * n
    return [6] * k6 + [5] * (n - k6)


PALETTE = ["FFB4C7E7", "FFC6E0B4", "FFF8CBAD", "FFD9D2E9", "FFFFE699", "FFBDD7EE", "FFE2EFDA",
           "FFFCE4D6", "FFB7DEE8", "FFE4DFEC", "FFD0CECE", "FFA9D08E", "FFF4B084", "FF9BC2E6",
           "FFFFD966", "FFC9C9FF", "FFFFC7CE", "FFB3E5C9", "FFE0C3A5", "FFCCE5FF", "FFD5A6BD",
           "FFB6D7A8", "FFFFE5CC", "FFA2C4C9"]
color_by_row = {}

scheduled = {}
for i, (row, ed, target, pref, dep) in enumerate(PLAN):
    c = byrow[(row, ed)]
    hours = day_hours(c["hours"])
    n = len(hours)
    earliest = target
    if dep:
        earliest = max(earliest, scheduled[dep]["days"][-1] + dt.timedelta(1))
    shifts = [pref, "tarda" if pref == "matí" else "matí"]
    if c["teacher"] == "MARIA":
        shifts = ["matí"]
    busy = teacher_busy.setdefault(c["teacher"], set()) if c["teacher"] != "PER ASSIGNAR" else set()
    found = None
    for si, s in enumerate(working):
        if s < earliest:
            continue
        days = working[si:si + n]
        if len(days) < n:
            break
        if any(d in busy for d in days):
            continue
        for shift in shifts:
            for aula in ("GOOGLE", "FIREFOX", "COPILOT"):
                if all((d, (aula, shift)) not in occupied for d in days):
                    found = (days, (aula, shift))
                    break
            if found:
                break
        if found:
            break
    assert found, f"no hi ha lloc per {c['name']}"
    days, room = found
    for d in days:
        occupied.add((d, room))
        busy.add(d)
    color = color_by_row.setdefault(row, PALETTE[len(color_by_row) % len(PALETTE)])
    scheduled[(row, ed)] = dict(c, days=days, room=room, hours_day=hours, color=color)

# ---------------------------------------------------------------- escriure al calendari
thin = Side(style="thin")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def label(s):
    ed = f" ({s['ed']}a ed.)" if s["n_ed"] > 1 else ""
    code = s["code"].split("_")[1] if s["code"].startswith("FC01_") else s["code"].replace("B_", "").replace("_", " ")
    return f"{code} {s['name']}{ed}"


def horari(s, h):
    return ("9:00-15:00" if h == 6 else "9:00-14:00") if s["room"][1] == "matí" else \
           ("15:00-21:00" if h == 6 else "15:00-20:00")


legend_next_col = {}
for key, s in scheduled.items():
    fill = PatternFill("solid", fgColor=s["color"])
    for d, h in zip(s["days"], s["hours_day"]):
        c = cell_for(d, s["room"])
        c.value = h
        c.fill = fill
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.font = Font(name="Calibri", size=11, bold=(d == s["days"][0]))
    # Llegenda a la dreta (una per mes en què apareix el curs)
    for ym in sorted({(d.year, d.month) for d in s["days"]}):
        r = blocks[ym] + ROOMS[s["room"]]
        if r not in legend_next_col:
            last = max([cc.column for cc in ws[r] if cc.value not in (None, "") and cc.column >= 37] + [36])
            legend_next_col[r] = last + 2
        col = legend_next_col[r]
        mdays = [d for d in s["days"] if (d.year, d.month) == ym]
        txt = (f"{label(s)} · {s['teacher']} · {s['room'][0]} {s['room'][1]} "
               f"{horari(s, s['hours_day'][0])} · {s['days'][0]:%d/%m}–{s['days'][-1]:%d/%m} · {s['hours']} h")
        lc = ws.cell(r, col, txt)
        lc.fill = fill
        lc.font = Font(name="Calibri", size=9, bold=(mdays[0] == s["days"][0]))
        legend_next_col[r] = col + 9

# ---------------------------------------------------------------- SET-DES 2027
wc = openpyxl.load_workbook(F_CAL, data_only=True)["Parametres"]
holidays, vacations = {}, set()
section = None
for row in wc.iter_rows(values_only=True):
    vals = [v for v in row if v is not None]
    if not vals:
        continue
    if isinstance(vals[0], str) and vals[0].startswith("FESTIUS"):
        section = "F"
    elif isinstance(vals[0], str) and vals[0].startswith("VACANCES"):
        section = "V"
    elif isinstance(vals[0], dt.datetime):
        if section == "F":
            holidays[vals[0].date()] = f"{vals[1]} ({vals[2]})"
        elif section == "V":
            vacations.add(vals[0].date())

# Festa Nacional d'Espanya: no consta al calendari laboral però és festiu
holidays.setdefault(dt.date(2027, 10, 12), "Festa Nacional d'Espanya (Nacional)")
# Festius locals 04/09 i 15/09: laborables per al centre, a canvi del 25/06 i el 07/12
holidays.pop(dt.date(2027, 9, 4), None)
holidays.pop(dt.date(2027, 9, 15), None)
holidays.setdefault(dt.date(2027, 6, 25), "Festiu local (canvi pel 04/09)")
holidays.setdefault(dt.date(2027, 12, 7), "Festiu local (canvi pel 15/09)")

TEMPLATE_HR = blocks[(2027, 7)]  # JULIOL 2027 com a plantilla de format
TITLE_SRC = {9: blocks[(2026, 9)] - 1, 10: blocks[(2026, 10)] - 1,
             11: blocks[(2026, 11)] - 1, 12: blocks[(2026, 12)] - 1}
MONTHS = {9: "SETEMBRE", 10: "OCTUBRE", 11: "NOVEMBRE", 12: "DESEMBRE"}
max_col = 35  # A..AI
first = blocks[(2027, 8)] + 13  # AGOST 2027 + 13 files
for i, m in enumerate((9, 10, 11, 12)):
    t = first + 13 * i  # fila títol
    for off in range(0, 13):
        src_r, dst_r = TEMPLATE_HR - 1 + off, t + off
        ws.row_dimensions[dst_r].height = ws.row_dimensions[src_r].height
        for cidx in range(1, max_col + 1):
            sc, dc = ws.cell(src_r, cidx), ws.cell(dst_r, cidx)
            if off == 0 and cidx > 1:
                sc = ws.cell(TITLE_SRC[m], cidx)
            dc._style = copy(sc._style)
            dc.value = sc.value if (cidx == 1 and off >= 2) else None
    ws.merge_cells(start_row=t, start_column=1, end_row=t, end_column=34)
    tc = ws.cell(t, 1, f"{MONTHS[m]} 2027")
    tc._style = copy(ws.cell(TITLE_SRC[m], 1)._style)
    hr = t + 1
    for cidx, v in ((1, "AULA"), (2, "INICI"), (3, "FINAL")):
        ws.cell(hr, cidx, v)
    ndays = (dt.date(2027 + (m == 12), m % 12 + 1, 1) - dt.date(2027, m, 1)).days
    worked = 0
    for day in range(1, 32):
        col = 3 + day
        room_rows = range(hr + 1, hr + 10)
        if day > ndays:
            ws.cell(hr, col).value = None
            for rr in room_rows:
                ws.cell(rr, col).fill = PatternFill()
            continue
        d = dt.date(2027, m, day)
        ws.cell(hr, col).value = dt.datetime(2027, m, day)
        if d in holidays:
            f = PatternFill("solid", fgColor=RED)
        elif d.weekday() >= 5:
            f = GREY_2027
        elif d in vacations:
            f = VAC_FILL
        else:
            f = PatternFill()
            worked += 1
        for rr in room_rows:
            ws.cell(rr, col).fill = f
    ws.cell(t, 35).value = worked
    notes = [f"{d:%d/%m} {n}" for d, n in sorted(holidays.items()) if d.month == m]
    vac = sorted(d for d in vacations if d.month == m and d.weekday() < 5 and d not in holidays)
    if vac:
        notes.append(f"Vacances: {vac[0]:%d/%m}–{vac[-1]:%d/%m}")
    if notes:
        nc = ws.cell(t, 37, "Festius: " + " · ".join(notes))
        nc.font = Font(name="Calibri", size=10, italic=True)

# ---------------------------------------------------------------- full resum
if "PLANIFICACIÓ 26-27" in wb.sheetnames:
    del wb["PLANIFICACIÓ 26-27"]
ps = wb.create_sheet("PLANIFICACIÓ 26-27", index=wb.sheetnames.index(SHEET) + 1)
hdr = ["CODI", "NOM FORMACIÓ", "EDICIÓ", "DOCENT", "AULA", "TORN", "HORARI", "DATA INICI",
       "DATA FINAL", "DIES", "HORES PREVISTES", "HORES PROGRAMADES", "DISTRIBUCIÓ"]
ps.append(["CRONOGRAMA 26-27 PROVISIONAL — PLANIFICACIÓ DE FORMACIONS"])
ps.append(["Font: FORMACIONS_26-27_PROVISIONAL.xlsx (hores i docents) · Calendari: full 'CRONO 25-26' "
           "i CALENDARI_LABORAL_2027.xlsx · Criteri: 5-6 h/dia en dies laborables consecutius."])
ps.append([])
ps.append(hdr)
ps["A1"].font = Font(name="Arial", size=14, bold=True)
ps["A2"].font = Font(name="Arial", size=9, italic=True)
head_fill = PatternFill("solid", fgColor="FF1F4E78")
for cidx in range(1, len(hdr) + 1):
    c = ps.cell(4, cidx)
    c.font = Font(name="Arial", bold=True, color="FFFFFFFF")
    c.fill = head_fill
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = BORDER
rows = sorted(scheduled.values(), key=lambda s: (s["days"][0], s["room"][1] != "matí"))
for s in rows:
    n6 = s["hours_day"].count(6)
    n5 = s["hours_day"].count(5)
    dist = " + ".join(x for x in (f"{n6} dies × 6 h" if n6 else "", f"{n5} dies × 5 h" if n5 else "") if x)
    hor = horari(s, 6) if n6 else horari(s, 5)
    if n6 and n5:
        hor += f" ({horari(s, 5)} els dies de 5 h)"
    ps.append([s["code"], s["name"], f"{s['ed']}/{s['n_ed']}", s["teacher"], s["room"][0],
               s["room"][1].upper(), hor, s["days"][0], s["days"][-1], len(s["days"]), s["hours"], None, dist])
    r = ps.max_row
    ps.cell(r, 12).value = sum(s["hours_day"])
    for cidx in range(1, len(hdr) + 1):
        c = ps.cell(r, cidx)
        c.font = Font(name="Arial", size=10)
        c.border = BORDER
        c.alignment = Alignment(vertical="center", wrap_text=cidx in (2, 7, 13))
    ps.cell(r, 1).fill = PatternFill("solid", fgColor=s["color"])
    for cidx in (8, 9):
        ps.cell(r, cidx).number_format = "dd/mm/yyyy"
last = ps.max_row
ps.append([None] * 9 + ["TOTAL", f"=SUM(K5:K{last})", f"=SUM(L5:L{last})"])
for cidx in (10, 11, 12):
    ps.cell(last + 1, cidx).font = Font(name="Arial", bold=True)
ps.append([])
ps.append(["Notes:"])
for note in [
    "Hores d'ADGG0208 (678), FCOS02 (30), CTRH0011 (10) i CTRHI0015 (10) facilitades per l'usuari. "
    "FCOI25 i els codis de les files 31-43 no tenen hores i no s'han programat.",
    "MARIA: només matins (disponibilitat 'Matins lliure // Tardes: 1 formació per mes'). S'han evitat "
    "els dies en què ja fa 'IA MARIA' a GOOGLE MATINS (set.-oct. 2026).",
    "Un docent no té mai dues formacions el mateix dia. Els nivells (bàsic → intermedi → avançat, "
    "Coaching I → II, Català A1 → A2.1 i mòduls IMPE0110) es programen en ordre.",
    "No s'ha tocat cap cel·la ja ocupada del cronograma ni les aules de TARRAGONA / ON LINE.",
    "Setembre-desembre 2027: festius i vacances del CALENDARI_LABORAL_2027 (els festius locals 04/09 i "
    "15/09 hi consten com 'a omplir'). S'hi afegeix el 12/10 com a festiu.",
]:
    ps.append(["• " + note])
    ps.cell(ps.max_row, 1).font = Font(name="Arial", size=9)
widths = [22, 48, 8, 14, 11, 8, 26, 12, 12, 7, 11, 13, 26]
for i, w in enumerate(widths, 1):
    ps.column_dimensions[L(i)].width = w
ps.freeze_panes = "A5"

wb.save(F_OUT)

# ---------------------------------------------------------------- restaurar formes (triangles) perdudes per openpyxl
src = zipfile.ZipFile(F_CRONO)
drawing = src.read("xl/drawings/drawing1.xml")
tmp = tempfile.mktemp(suffix=".xlsx")
shutil.copy(F_OUT, tmp)
with zipfile.ZipFile(tmp) as zin, zipfile.ZipFile(F_OUT, "w", zipfile.ZIP_DEFLATED) as zout:
    names = zin.namelist()
    wbxml = zin.read("xl/workbook.xml").decode()
    rels = zin.read("xl/_rels/workbook.xml.rels").decode()
    # localitzar el fitxer del full SHEET
    rid = re.search(r'<sheet [^>]*name="%s"[^>]*r:id="(rId\d+)"' % re.escape(SHEET), wbxml).group(1)
    target = re.search(r'Id="%s"[^>]*Target="/?(?:xl/)?([^"]+)"' % rid, rels) or \
        re.search(r'Target="/?(?:xl/)?([^"]+)"[^>]*Id="%s"' % rid, rels)
    sheet_path = "xl/" + target.group(1)
    sheet_rels = sheet_path.replace("worksheets/", "worksheets/_rels/") + ".rels"
    for item in names:
        data = zin.read(item)
        if item == sheet_path:
            x = data.decode()
            if "<drawing " not in x:
                x = x.replace("</worksheet>", "")
                ins = '<drawing r:id="rIdShapes1"/>'
                m = re.search(r"<legacyDrawing[^>]*/>", x)
                x = x[:m.start()] + ins + x[m.start():] if m else x + ins
                x += "</worksheet>"
                if 'xmlns:r=' not in x[:500]:
                    x = x.replace("<worksheet ", '<worksheet xmlns:r="http://schemas.openxmlformats.org/'
                                  'officeDocument/2006/relationships" ', 1)
            data = x.encode()
        elif item == sheet_rels:
            x = data.decode().replace(
                "</Relationships>",
                '<Relationship Id="rIdShapes1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                'relationships/drawing" Target="../drawings/shapes1.xml"/></Relationships>')
            data = x.encode()
        elif item == "[Content_Types].xml":
            x = data.decode().replace(
                "</Types>",
                '<Override PartName="/xl/drawings/shapes1.xml" ContentType="application/'
                'vnd.openxmlformats-officedocument.drawing+xml"/></Types>')
            data = x.encode()
        zout.writestr(item, data)
    if sheet_rels not in names:
        zout.writestr(sheet_rels,
                      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns='
                      '"http://schemas.openxmlformats.org/package/2006/relationships"><Relationship '
                      'Id="rIdShapes1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                      'relationships/drawing" Target="../drawings/shapes1.xml"/></Relationships>')
    zout.writestr("xl/drawings/shapes1.xml", drawing)

for s in rows:
    print(f"{s['days'][0]:%d/%m/%Y}-{s['days'][-1]:%d/%m/%Y} {s['room'][0]:8} {s['room'][1]:5} "
          f"{s['teacher']:12} {s['hours']:4}h {len(s['days']):3}d  {label(s)}")
