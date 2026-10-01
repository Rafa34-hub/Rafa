# Handoff — Migración a Claude Team + GitHub corporativo

**Multimèdia Tarragona · Documento para continuar en la cuenta Claude Team**
Fecha: 1 de octubre de 2026
De: sesión en cuenta Pro personal (Gmail) → a cuenta Team corporativa (`gerencia@multimediatarragona.com`)

---

## 1. Contexto de partida

- Empresa: **Multimèdia Tarragona SL** — centro de formación (EAPC, ICIQ, estibadores, ADGG0408, docentes).
- Equipo estable: 4 personas (Rafa, socia, Montse Pérez, Vanesa González, Ana Marín).
- Motivo de la migración: cumplimiento RGPD (DPA, art. 28) — las cuentas Pro personales no lo incluían.
- Decisión tomada: Claude Team Standard anual, 4 asientos, dominio `multimediatarragona.com` (Microsoft 365 / Exchange).
- Referencia completa: documento `migracion-claude-team-multimedia-tarragona.md` subido como contexto inicial a esta conversación.

---

## 2. Estado actual (completado ✅)

### Claude Team
- ✅ Cuenta Team creada con `gerencia@multimediatarragona.com`.
- ✅ 4 asientos Standard contratados (anual).
- ✅ Equipo invitado al workspace (socia como Owner, resto Member).

### GitHub
- ✅ Organización **Multimedia-Tarragona-SL** creada como *business or institution*.
- ✅ Dominio `multimediatarragona.com` verificado vía TXT (añadido por Dynasoft).
- ✅ Email del contacto: `gerencia@multimediatarragona.com`.
- ✅ Cuenta fantasma `MULTIMEDIATARRAGONA` eliminada de la organización.
- ✅ Invitaciones enviadas a: socia (Owner), Montse (Member), Vanesa (Member), Ana (Member).
- ✅ Logado como `MultimediaGerencia` (cuenta de administración de la organización).

### Documentos preparados
- ✅ **Guía de 1 página Claude Code + GitHub para el equipo** (en catalán), lista para distribuir. Guardada en el repo `Rafa34-hub/Rafa`, rama `claude/brave-albattani-4v32b4`, archivo `guia-claude-code-equipo.md`.

---

## 3. Pendiente a corto plazo (próximos días)

### GitHub — configuración de seguridad
- [ ] **Member privileges** (`settings/member_privileges`):
  - Base permissions = `Read`.
  - Desactivar creación de repos públicos (solo privados).
  - Desactivar forking.
  - Desactivar Pages creation.
  - Activar Integration access requests.
- [ ] **Avisar al equipo por WhatsApp** de que activen 2FA en GitHub con Microsoft Authenticator antes de aceptar la invitación.
- [ ] **Activar 2FA obligatorio** en la organización (`settings/security` → "Require two-factor authentication for everyone"). Hacerlo DESPUÉS de que el equipo haya activado 2FA.
- [ ] **Perfil de la organización** (`settings/profile`): logo, display name con acento, URL web, descripción, Tarragona.

### Claude Team — configuración del workspace
- [ ] `claude.ai/admin-settings/organization`: nombre, logo, dominios permitidos, "Invite only", "Approve one-by-one".
- [ ] `claude.ai/admin-settings/privacy`: confirmar "No model training on your content".
- [ ] `claude.ai/admin-settings/connectors`: política de conectores (Google Drive, MS 365, etc.) + allowlist desktop extensions.
- [ ] **Team instructions** (hasta 3.000 chars): texto ya redactado disponible en el histórico de esta conversación (RGPD, catalán/castellano, EAPC/ICIQ, no categorías especiales art. 9, etc.).

### Reembolso Pro de la socia
- [ ] Antes del día 14 desde su contratación (margen 14 días derecho desistimiento UE).
- [ ] Argumentario ya redactado en el histórico de esta conversación (Directiva 2011/83/UE).
- [ ] Vía: chat de soporte en claude.ai → "Refund Request".

### Pro personal de Rafa (Gmail)
- [ ] Cancelar renovación en Settings → Billing (para que no cobre día 12 del mes que viene).
- [ ] Mantenerla activa hasta día 12 para completar migración manual de proyectos.

---

## 4. Pendiente a medio plazo (semanas)

### Migración manual de proyectos (de Pro personal → Team)
Orden de prioridad (los 8 críticos):
1. EAPC 2026 LOT 2
2. Simulador EAPC
3. EPAC 2026
4. Conforcat 2026
5. ICIQ 2026 IA
6. ADGG0408
7. MILLORAR PLA IGUALTAT
8. Marketing digital

**Procedimiento por proyecto** (20-40 min cada uno):
1. Copiar Project instructions → `.md` local.
2. Descargar archivos de Project knowledge.
3. Para chats críticos: pedir a Claude *"Resume este chat para retomarlo en otra cuenta: contexto, decisiones, siguientes pasos"* → guardar resumen.
4. En Team: crear proyecto con mismo nombre, pegar instructions, subir archivos, pegar resumen histórico como contexto.

**Antes de empezar**: lanzar export de datos (`claude.ai/settings/data-privacy-controls` → Export data) para tener backup ZIP de todo.

**Proyectos que NO se migran** (se quedan en Pro personal / mueren):
- UDIMA (Psicología del Aprendizaje, Social, Fundamentos, Métodos, AC1, AC2, EC1, EAC2, AEC-2).
- Casa contenedores.
- Ortografía (si es personal).

### Estructura inicial de repositorios en GitHub (crear bajo demanda, no de golpe)
**Fase 1 — semana 1** (crear solo estos 3):
1. `onboarding-equip` → documentación interna del equipo (mover ahí la guía de 1 página).
2. `manual-ia-intern` → manual de uso de IA (alfabetización AI Act art. 4).
3. El proyecto activo más urgente (ej. `eapc-2026-lot2`).

**Nomenclatura**: minúsculas, guiones, sin espacios ni acentos. Patrón `cliente-año-tema` o `tema-descriptor`.

**Teams de GitHub a crear** (para gestionar permisos por grupo):
- `@all-staff` → acceso de lectura a todo.
- `@admins` → Rafa + socia → acceso Admin.
- `@coordinacio-academica` → Montse (+ docentes puntuales) → escritura en repos formativos.
- `@comercial-informacio` → Vanesa → escritura en marketing/web.
- `@suport-pedagogic` → Ana → escritura en materiales didácticos.

### Alta temporal de docente colaborador (2 meses)
- [ ] Crear buzón `nom-cognom@multimediatarragona.com` en Exchange.
- [ ] Dar de alta en Claude Team (asiento 5, Standard).
- [ ] Dar de alta en GitHub org como Member, acceso solo al repo del curso.
- [ ] Agendar recordatorio Outlook: 1 semana antes del final → "revisar materiales antes de baja".
- [ ] Agendar recordatorio Outlook: día de baja → "dar de baja Claude + GitHub + reducir asiento a 4".

### Compliance RGPD / AI Act
- [ ] Actualizar Registro de Actividades de Tratamiento (art. 30) con Anthropic PBC como encargado.
- [ ] Actualizar política de privacidad de Multimèdia Tarragona.
- [ ] Descargar y archivar copia del DPA de Anthropic.
- [ ] Evaluar necesidad de EIPD (censo 6.000 personas, ICIQ con perfilado).
- [ ] Cláusula tipo para contratos con docentes colaboradores.

---

## 5. Pendiente a largo plazo (meses)

### Formación interna del equipo
- [ ] Formación de uso de Claude Code para administración (Montse + chicas): cambiar flujo chat → Claude Code.
- [ ] Manual interno de uso de IA (13-15 secciones + anexos).
- [ ] Módulo obligatorio de alfabetización IA en el plan *Forma't per Formar*.

### Formación extensible al alumnado
- [ ] Cursos sobre implementación de CRM con IA, usando Claude como herramienta única.
- [ ] Investigar: licencias de estudiantes de Anthropic, acreditación como centro formador de Claude.

### Proyecto estratégico — segundo cerebro corporativo
- [ ] Pendiente de planificar en sesión dedicada: diseño de un *second brain* corporativo para Multimèdia Tarragona (centralizar conocimiento, procedimientos, históricos de clientes, materiales reutilizables).

### Seguridad avanzada (opcional)
- [ ] Evaluar SSO SAML con Microsoft Entra ID (ya tenéis Microsoft 365).
- [ ] MFA condicional (IP oficina, dispositivos compliant).
- [ ] "Require SSO for Claude" en `claude.ai/admin-settings/identity`.

---

## 6. Reglas de oro consolidadas

### GitHub
- Repos siempre **privados**.
- Un repositorio por proyecto, nunca por persona.
- Nunca commitear: datos personales (alumnos, DNIs, correos), contraseñas, API keys.
- Datos personales → SharePoint/OneDrive, nunca GitHub.
- Siempre revisar PR antes de merge.
- Branches cortas (una tarea = una branca = un PR = merge).

### Claude Team
- Cuentas corporativas siempre, nunca personales para trabajo de empresa.
- Nunca subir datos categoría especial art. 9 RGPD sin base jurídica.
- Proyectos de empresa compartidos; estudios personales privados.
- Chats dentro de proyectos compartidos siguen siendo privados por defecto.

---

## 7. URLs importantes

### Claude Team
- Admin: `claude.ai/admin-settings`
- Miembros: `claude.ai/admin-settings/members`
- Facturación: `claude.ai/admin-settings/billing`
- Privacy: `claude.ai/admin-settings/privacy`

### GitHub organización
- Organización: `https://github.com/Multimedia-Tarragona-SL`
- Settings: `https://github.com/organizations/Multimedia-Tarragona-SL/settings/profile`
- People: `https://github.com/orgs/Multimedia-Tarragona-SL/people`
- Nuevo repo: `https://github.com/organizations/Multimedia-Tarragona-SL/repositories/new`
- Member privileges: `https://github.com/organizations/Multimedia-Tarragona-SL/settings/member_privileges`
- Security: `https://github.com/organizations/Multimedia-Tarragona-SL/settings/security`

---

## 8. Siguiente paso recomendado al abrir la nueva conversación

**Opción A — Terminar setup**:
*"Hola Claude, continúo desde la cuenta Team corporativa. Lee este documento como contexto. Vamos a terminar el setup de GitHub y Claude Team según el apartado 3 (pendiente a corto plazo). Empecemos por los Member privileges de GitHub."*

**Opción B — Migración de proyectos**:
*"Hola Claude, continúo desde la cuenta Team corporativa. Lee este documento. Vamos a iniciar la migración manual de proyectos de mi antigua cuenta Pro personal (apartado 4). Empecemos por EAPC 2026 LOT 2."*

**Opción C — Segundo cerebro corporativo**:
*"Hola Claude, continúo desde la cuenta Team corporativa. Lee este documento. Quiero planificar el proyecto de segundo cerebro corporativo (apartado 5). Dedícame una sesión completa para diseñarlo."*

---

*Documento generado el 1 de octubre de 2026 para continuar la implementación de la migración desde la nueva cuenta Claude Team corporativa de Multimèdia Tarragona.*
