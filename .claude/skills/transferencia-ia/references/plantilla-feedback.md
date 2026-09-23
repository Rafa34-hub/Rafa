# Plantilla de feedback (català, HTML per a Outlook)

Principis:
- Tuteig, to proper i constructiu. Primer el que ha fet bé, després el que pot millorar.
- Citar les tècniques pel número del temari ("tècnica 14").
- Màxim 3–5 millores, les de més impacte per al seu cas.
- Sempre un **prompt millorat** adaptat a Copilot, llest per copiar (en cursiva, amb `<br>` entre línies, usant [claudàtors] per a allò que ha d'omplir).
- Si ha fet servir una eina no corporativa: explicar-ho sense culpabilitzar, amb el motiu concret (dades, accés a la bústia, límits del pla gratuït…).
- Si ha detectat errors de la IA o ha verificat la resposta, reconèixer-ho explícitament: és el que més valorem.
- Si l'alumne ha fet una pregunta al correu (p. ex. "com pujo més de 3 fitxers?"), respondre-la.
- Evitar to d'IA: frases naturals, sense grandiloqüència.

```html
<p>Hola [Nom],</p>
<p>Gràcies pel treball. [1–2 frases sobre el cas triat i per què és útil]. Et deixo els comentaris (els números fan referència a les tècniques del temari de la sessió 1).</p>
<p><b>El que has fet molt bé</b></p>
<ul>
<li>[Tècnica aplicada] (tècnica N).</li>
<li>...</li>
</ul>
<p><b>El que pots millorar</b></p>
<ul>
<li><b>[Títol curt].</b> [Explicació concreta + com fer-ho] (tècnica N).</li>
<li>...</li>
</ul>
<p><b>Proposta de prompt millorat</b></p>
<p><i>Actua com a [rol].<br>
TASCA: ...<br>
FORMAT: ...<br>
[Fonts / criteris / exemple]<br>
Si alguna dada no és clara, pregunta-m'ho / digues-ho en lloc de suposar-la. Respon en català, registre [formal administratiu].</i></p>
<p><b>Valoració</b><br>[Realista/útil? Consell de següent pas].</p>
<p>Una salutació cordial,<br>Rafael</p>
```

## Consells recurrents que han funcionat (curs setembre 2026)
- **Massa coses en un prompt** → dividir en passos (llistat → dades → format).
- **Format de sortida no definit** → indicar-lo (taula, esquema, SmartArt a PowerPoint, fitxes a Word).
- **Criteris normatius** → no demanar que "sàpiga" la norma: donar-li els criteris exactes o adjuntar el text consolidat.
- **Normativa** → adjuntar la versió consolidada i demanar l'article a cada punt; comprovar vigència i modificacions.
- **Converses llargues que s'emboliquen** → "Resumeix totes les especificacions acordades" i començar una conversa nova amb aquest resum.
- **Pregunta que ja porta la resposta** → formular-la neutra o demanar arguments a favor i en contra abans de concloure.
- **Argumentaris a favor d'una opció** → demanar també l'altra cara (riscos, objeccions).
- **Diagrames (genogrames, organigrames)** → primer taula de persones/relacions validada, després el dibuix amb simbologia explícita (millor a PowerPoint amb formes).
- **Límit de fitxers a Copilot** → combinar PDFs amb l'eina corporativa, referenciar fitxers de OneDrive/SharePoint amb "/", o processar per lots i consolidar.
- **Prompts recurrents** → desar-los com a indicació a Copilot o crear un agent.
- **Automatitzacions (Copilot Studio, Power Automate, Python)** → començar amb versió manual i consultar TIC abans d'instal·lar o desplegar.
- **Excel amb hores** → format `[h]:mm` per sumar més de 24 h; provar amb dades fictícies.
