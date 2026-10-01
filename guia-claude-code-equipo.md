# Guia ràpida — Claude Code + GitHub

**Multimèdia Tarragona · Ús intern de l'equip**

---

## 1 · El primer dia: connecta GitHub (una sola vegada, 2 min)

1. Entra a **claude.ai/code** amb el teu correu corporatiu (`@multimediatarragona.com`).
2. Et sortirà un botó **"Connect GitHub"** → clica.
3. T'enviarà a GitHub. Inicia sessió amb el teu compte corporatiu de GitHub (el que vas crear amb el teu correu `@multimediatarragona.com`).
4. GitHub et preguntarà a quin compte donar accés → tria **Multimedia-Tarragona-SL** (mai el teu personal).
5. A "Which repositories?" → tria **Only select repositories** i marca els que necessitis. Si tens dubtes, demana-li al Rafa.
6. **Install & Authorize**. Fet. Ja no cal repetir-ho.

---

## 2 · Com funciona Claude Code (concepte)

Claude Code **no desa res al teu ordinador ni al núvol de Claude**. Treballa dins un contenidor temporal que:

- **Clona** un repositori de GitHub.
- Fa els canvis que li demanis.
- **Puja** els canvis a GitHub en una branca nova + obre un *Pull Request*.
- Quan tanques la sessió, el contenidor desapareix. **L'únic que queda és el que hagi pujat a GitHub.**

**Regla d'or**: si no està a GitHub, no existeix.

---

## 3 · Iniciar una sessió nova

1. A claude.ai/code → **New session**.
2. Tria el repositori:
   - **Existent** → tria'l de la llista (`Multimedia-Tarragona-SL/<nom>`).
   - **Nou** → digues-li a Claude: *"Crea un repositori nou anomenat `nom-del-projecte` a l'organització Multimedia-Tarragona-SL"*.
3. Explica-li què vols: *"Prepara els materials del mòdul X", "Genera una web amb aquests continguts", "Analitza aquest PDF i treu-ne un resum"*.
4. Quan acabis o vulguis desar una fita: *"Fes commit i push dels canvis"*.
5. Revisa el Pull Request a GitHub, aprova'l i fusiona'l (**merge**).

---

## 4 · Reglas d'or (NO negociables)

| ✅ Sí | ❌ No |
|---|---|
| Revisar sempre el PR abans de fer merge | Fer merge sense mirar què canvia |
| Repositoris **privats** sempre | Crear repositoris públics |
| Un projecte = un repositori | Mesclar diversos projectes en un repo |
| Branques curtes (una tasca = una branca) | Acumular dies de feina sense fer merge |
| Dades anonimitzades si cal pujar-les | Pujar **mai** llistats d'alumnes, correus, DNIs, CIFs, dades de salut, etc. |
| Si Claude genera una clau/API key: moure-la fora del repo | Deixar contrasenyes o tokens al codi |
| En cas de dubte, preguntar al Rafa | Inventar-se com fer-ho |

---

## 5 · Nomenclatura de repositoris

Format recomanat: `client-any-tema` o `tema-descriptor`.

Exemples:
- `eapc-2026-lot2`
- `iciq-2026-ia`
- `conforcat-2026`
- `adgg0408-materials`
- `marketing-digital`
- `manual-ia-intern`

Minúscules, guions (`-`), sense espais ni accents.

---

## 6 · Dades personals i RGPD

**Mai pugis a GitHub** (encara que sigui un repo privat):

- Llistats d'alumnat (noms, DNIs, correus, telèfons).
- Respostes de qüestionaris amb identificació.
- Dades de categories especials (salut, ideologia, religió, etc.).
- Correus electrònics de clients.
- Contrasenyes, API keys, tokens.

Si has de treballar amb aquestes dades, fes-ho **al xat de Claude.ai Team** (que té DPA i no entrena models), no a Claude Code + GitHub.

---

## 7 · Si alguna cosa falla

- **"No veig cap repositori"** → la teva cuenta de Claude no està connectada a l'organització de GitHub, o no tens accés al repo concret. Demana al Rafa que t'hi afegeixi.
- **"Claude Code ha esborrat alguna cosa que no volia"** → no et preocupis, el PR mostra tots els canvis. Rebutja el PR i torna-ho a fer.
- **"He fet merge d'alguna cosa malament"** → GitHub permet revertir qualsevol merge. Avisa al Rafa.
- **Dubtes sobre un repositori concret** → millor preguntar que suposar.

---

## 8 · Resum de la pantalla d'una sessió

```
┌─────────────────────────────────────────────────┐
│  Multimedia-Tarragona-SL / nom-del-repo         │  ← repositori actiu
├─────────────────────────────────────────────────┤
│                                                 │
│   [Xat amb Claude — li demanes feines aquí]     │
│                                                 │
│   [Claude et mostra els canvis que fa]          │
│                                                 │
├─────────────────────────────────────────────────┤
│  Branca: claude/nom-de-la-branca                │
│  [Commit] [Push] [Open PR]                      │
└─────────────────────────────────────────────────┘
```

---

**Dubtes?** Pregunta al Rafa abans de fer res de què no estiguis segur/a.

*Versió 1.0 · octubre 2026*
