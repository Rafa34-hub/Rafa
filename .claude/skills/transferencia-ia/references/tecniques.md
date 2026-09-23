# Temari de referència — Taller d'IA multimodel aplicada a la gestió i la productivitat (EAPC)

Font: `sessio1_eapc.ppsx` i `sessio2_eapc.ppsx` (correu "Material curs", setembre 2026). Si el temari del curs actual canvia, prevaleix el del correu.

## Estructura bàsica d'un prompt
- **Objectiu** — què ha de fer la IA.
- **Context** — per què, a qui afecta, situació de fons.
- **Expectatives** — format, to, extensió.
- El prompt perfecte no surt a la primera: és una **conversa iterativa**.

## Les 20 tècniques (citar-les pel número al feedback)

### Bloc I — bàsiques
1. Sigues directe i clar.
2. Especifica a qui va dirigit (l'audiència).
3. Fes servir instruccions en positiu (no "No facis X", sinó "Fes Y").
4. Estructura el prompt amb claredat (capçaleres, separadors, etiquetes simples: INSTRUCCIÓ / TEXT / CONTEXT, ///).
5. Fes servir exemples per guiar la resposta (2–3 exemples del resultat).
6. Divideix tasques complexes en passos senzills (conversa guiada).

### Bloc II — per afinar
7. Demana explicacions adaptades a diferents nivells.
8. Explica per què la resposta importa (urgència/importància real, no recompenses fictícies).
9. Destaca els requisits prioritaris amb èmfasi clar ("HAS DE…").
10. Demana que "parli com un humà" (to natural, proper).
11. Fes servir "pensa pas a pas" (si cal).
12. Demana imparcialitat i evitar estereotips.
13. Deixa que la IA et faci preguntes abans de respondre.

### Bloc III — avançades
14. Assigna un rol al model (senzill, sense sobrecarregar-lo).
15. Destaca la prioritat amb èmfasi, no amb repetició.
16. Comença tu la resposta (indica com ha de començar).
17. Demana informació completa / corregeix sense canviar l'estil.
18. Defineix les fonts d'informació (quines usar o excloure; documents adjunts).
19. Especifica idioma o dialecte (i registre: català, formal administratiu).
20. Dona permís per dir "no ho sé" (reduir al·lucinacions).

## Seguretat, ètica i ús d'eines (sessió 1 i 2)
- **Regla d'or:** "Si aquesta informació sortís publicada demà, em suposaria un problema?" → si sí, només Copilot Chat corporatiu i, si cal, amb autorització.
- **Classificació de dades:** pública · administrativa interna (Copilot) · confidencial contractes · dades personals RGPD (només Copilot + autorització) · categoria especial art. 9 (salut, etc.: pràcticament prohibit) · credencials (mai).
- **Anonimitzar** sempre és una opció; el dubte es resol preguntant abans.
- **Verifica sempre** (al·lucinacions; cas real TSJ Galícia: 24 citacions inventades).
- **La decisió final és humana**: qui signa respon.
- **Copilot Chat és l'eina corporativa aprovada** per a dades internes; ChatGPT/Claude/Gemini només amb dades públiques o fictícies i amb compte personal no per a dades internes. DeepSeek/Qwen/Grok: no recomanats.
- **Prototipar sí, desplegar en producció no** sense passar pel circuit d'IT i seguretat.
- Transparència (AI Act, agost 2026): indicar quan un contingut s'ha generat amb IA, especialment cap a la ciutadania.
