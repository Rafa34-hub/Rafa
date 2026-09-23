---
name: transferencia-ia
description: Corrige los trabajos de transferencia de los cursos de IA de la Escola d'Administració Pública de Catalunya (EAPC) que imparte Rafael (Multimèdia Tarragona). Lee las entregas del buzón docent@multimediatarragona.com en Outlook, evalúa cada prompt y conversación según las técnicas de prompting del temario, redacta feedback constructivo en catalán como borrador de respuesta, y genera una tabla de notas de 0 a 10. Úsala cuando el usuario escriba /transferencia-ia o pida corregir, puntuar o dar feedback a trabajos de transferencia de un curso de IA de la EAPC.
---

# /transferencia-ia — Corrección de trabajos de transferencia (cursos de IA · EAPC)

## Contexto fijo

- **Docente:** Rafael (firma los correos como "Rafael"; el alumnado le escribe como Rafael/Rafel/Rafa).
- **Buzón:** `docent@multimediatarragona.com` (Exchange / Outlook). Se accede con el conector **Microsoft 365**, que debe estar conectado con esa cuenta. Comprueba siempre con `get_me` que la cuenta es `docent@…`; si es otra (p. ej. `gerencia@…`), para y pide al usuario que reconecte el conector con docent@ en claude.ai → Configuración → Conectores y abra una sesión nueva.
- **Alumnado:** personal de la Generalitat (normalmente `@gencat.cat`, `@atc.cat`…). Los correos de `@multimediatarragona.com` suelen ser de otros cursos (p. ej. Excel): **ignóralos** salvo que el usuario diga lo contrario.
- **Tarea que se les pidió:** una consulta enfocada a su trabajo real usando el máximo de técnicas de prompting vistas en clase, enviando por correo el prompt y la conversación (normalmente en un adjunto).
- **Herramienta obligatoria del alumnado: Microsoft 365 Copilot Chat (cuenta corporativa).** Usar ChatGPT/Claude/Gemini con cuenta personal es un punto a corregir siempre, más aún si hay datos personales o sensibles.
- **Idioma del feedback: siempre catalán**, tuteo, tono cercano, constructivo y concreto.

## Flujo de trabajo

### 1. Localizar las entregas
1. `get_me` → verificar cuenta docent@.
2. `outlook_email_search` en `Inbox` (ordenado, 25 por página, pagina si hace falta) acotando por fechas del curso si el usuario las da.
3. Buscar también el correo del propio docente con el temario (asunto típico "Material curs", con adjuntos `sessio1_*.ppsx`, `sessio2_*.ppsx`). **Léelo con `read_resource`**: si el temario ha cambiado respecto a `references/tecniques.md`, usa el del correo y avisa al usuario.
4. Hacer la lista de entregas: remitente, fecha, adjuntos. Detectar:
   - Alumnos con **más de un correo** (juntarlos en una sola corrección y responder en el hilo más reciente; al otro, una línea remitiendo al feedback).
   - Correos que **no son entrega** (disculpas, dudas de asistencia…) → listarlos como "no presentado".
5. Enseñar la lista al usuario antes de seguir solo si hay dudas (cursos mezclados, remitentes raros).

### 2. Leer cada entrega
- `read_resource` del mensaje y de cada adjunto relevante (docx, pdf). Ignorar imágenes inline de firmas (`image00X`).
- Si un adjunto falla ("text extraction failed") o es muy grande, avisa al usuario: puede pasar capturas de pantalla o pegar el texto. No inventes el contenido.
- Si la salida es enorme se guarda en fichero: extrae con `python3`/`json` solo lo necesario (los prompts y fragmentos clave).
- Anota para cada alumno: puesto/unidad (de la firma), caso de uso, prompt(s) literal(es), iteraciones, herramienta usada (Copilot, Claude, ChatGPT… — fíjate en nombres de fichero, "Copilot said", "BizChat", "Plan Free"), datos introducidos y errores de la IA que el alumno detectó o no.

### 3. Evaluar
Usa `references/tecniques.md` (las 20 técnicas numeradas) y `references/rubrica.md` (criterios y nota 0–10). Para cada alumno identifica:
- Técnicas aplicadas (con número).
- Técnicas ausentes que más mejorarían su caso (máx. 3–5, las más útiles, no una lista exhaustiva).
- Riesgos: herramienta no corporativa, datos personales/sensibles, datos normativos no verificados, alucinaciones no detectadas, instalación de software sin TIC.
- Si el caso es realista y aplicable a su día a día.

Reglas de rigor:
- No afirmes hechos normativos o técnicos que no puedas verificar; formula con prudencia ("comprova…", "potser segons els vostres criteris…").
- Señala errores de la IA que el alumno no vio (denominaciones, referencias normativas dudosas, umbrales mal aplicados).
- Reconoce explícitamente el pensamiento crítico cuando exista (detectar errores, pedir justificaciones, verificar vigencia).

### 4. Redactar el feedback (borradores)
- Plantilla y ejemplos en `references/plantilla-feedback.md`. Estructura fija: saludo → agradecimiento + valoración breve del caso → **El que has fet molt bé** → **El que pots millorar** → **Proposta de prompt millorat** (listo para copiar, adaptado a Copilot) → **Valoració** → firma "Una salutació cordial,<br>Rafael".
- HTML permitido por Outlook: `p, ul, li, b, i, br, h1-h6, table`. Nada de `span`, `blockquote`, imágenes ni comentarios.
- Crear cada correo con `outlook_create_reply_draft` (body + bodyType `html`) sobre el mensaje del alumno.
- **Nunca enviar sin el visto bueno explícito del usuario.** Al terminar, resumir en una tabla: alumno · puntos clave del feedback, y avisar de incidencias (adjuntos ilegibles, no presentados, dudas).
- Para rehacer un borrador: crear uno nuevo con `outlook_create_reply_draft` y eliminar el viejo con `outlook_delete_draft` (`outlook_update_draft` con body reemplaza también la cita del original).

### 5. Enviar (solo con aprobación)
- `outlook_send_draft` para cada borrador aprobado.
- **Limitación conocida:** los borradores de respuesta que citan un correo con imágenes en la firma cuentan como "con adjuntos" y el conector no puede enviarlos (`draft_has_attachments`). Cuando pase, ofrece dos opciones al usuario:
  1. Que los envíe él desde la carpeta Borradores de Outlook (se mantienen en el hilo) — recomendado.
  2. Que los envíes tú con `outlook_send_mail` como correo nuevo ("RE: <asunto>") al mismo destinatario, y luego borres los borradores.
- Tras enviar, verifica con `outlook_email_search` (`recipient`) que no queda ningún alumno sin respuesta, incluidos los que enviaron dos correos.

### 6. Tabla de notas
Cuando el usuario la pida (o al final, ofreciéndola), genera en el chat una tabla markdown con la rúbrica de `references/rubrica.md`:
`# · Alumne · Tècniques (4) · Iteració (2) · Cas realista (2) · Copilot i dades (2) · Nota · Justificació breu`, ordenada de mayor a menor, con los no presentados al final, la media del grupo y 2–3 observaciones generales (técnica más y menos usada, cuántos no usaron Copilot). Deja claro que es una propuesta y que el docente ajusta la nota. Ofrece exportarla a Excel.

## Checklist final
- [ ] Cuenta docent@ verificada
- [ ] Temario leído (o `references/tecniques.md` confirmado vigente)
- [ ] Todas las entregas leídas (adjuntos incluidos) o incidencias comunicadas
- [ ] Un borrador en catalán por alumno, sin enviar
- [ ] Resumen al usuario + incidencias + no presentados
- [ ] Envío solo tras aprobación; verificación posterior de que nadie queda sin respuesta
- [ ] Tabla de notas si se pide
