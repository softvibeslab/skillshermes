# Integración de Telegram con Mission Control

## 🚀 Configuración Completa

La integración está lista. Puedes usar los siguientes comandos directamente en Telegram con tu bot @rogermac_bot.

## 📱 Comandos Disponibles

### 1. Crear Tarea
```
/mission create <descripción de la tarea>
```
**Ejemplos:**
- `/mission create Investigar error en el API de usuarios`
- `/mission create Crear endpoint para autenticación`
- `/mission create Revisar logs del servidor de producción`

### 2. Listar Tareas Activas
```
/mission list
```
Muestra todas las tareas activas con su ID, descripción, estado y prioridad.

### 3. Ver Estado de Tarea
```
/mission status <task-id>
```
**Ejemplo:**
- `/mission status task_1234567890`

### 4. Cancelar Tarea
```
/mission cancel <task-id>
```
**Ejemplo:**
- `/mission cancel task_1234567890`

### 5. Verificar Estado del Sistema
```
/mission health
```
Muestra el estado de Mission Control, conexión con Gateway, número de agentes activos, etc.

## 🔧 Flujo de Trabajo

1. **Envías comando** en Telegram a @rogermac_bot
2. **OpenClaw recibe** el mensaje a través del canal de Telegram
3. **El agente procesa** el comando usando el skill `mission-control`
4. **Se hace la petición HTTP** a Mission Control (localhost:4001)
5. **La respuesta se formatea** y se devuelve a Telegram

## 📊 Estructura de Respuesta

### Crear Tarea
```
✅ Tarea creada exitosamente
📋 ID: task_1234567890
📝 Descripción: Investigar error en el API
📊 Estado: pending
🎯 Prioridad: medium
```

### Listar Tareas
```
📋 **Tareas Activas**

1. **task_1234567890**
   📝 Investigar error en el API
   📊 Estado: in_progress
   🎯 Prioridad: high

2. **task_0987654321**
   📝 Crear endpoint de autenticación
   📊 Estado: pending
   🎯 Prioridad: medium
```

### Health Check
```
✅ **Mission Control Status**

🟢 Gateway: Conectado
🧠 Agentes activos: 11
📊 Tareas pendientes: 0
🕐 Uptime: 15 minutos
```

## 🛠️ Troubleshooting

### Si recibes "Mission Control no está respondiendo":
1. Verifica que Mission Control esté corriendo:
   ```bash
   cd ~/mission-control
   npm run dev
   ```

2. Verifica que esté en el puerto 4001:
   ```bash
   curl http://localhost:4001/api/health
   ```

### Si el bot de Telegram no responde:
1. Verifica que OpenClaw Gateway esté corriendo:
   ```bash
   ./openclaw.mjs status
   ```

2. Revisa los logs de Telegram:
   ```bash
   ./openclaw.mjs logs --follow
   ```

## 🎯 Consejos de Uso

- **Sé específico** en las descripciones de tareas para mejores resultados
- **Usa /mission list** regularmente para ver el progreso
- **Usa /mission health** antes de crear tareas críticas
- **Guarda los IDs de tareas** que te interesan para verificar su estado

## 🔒 Seguridad

- El bot está configurado para responder solo a tu user ID de Telegram
- Mission Control corre localmente en tu máquina (localhost:4001)
- OpenClaw Gateway está en loopback (127.0.0.1:18789)
- Todos los comandos requieren tu autorización explícita

## 🚀 Próximos Pasos

Para mejoras futuras podrías:
- Añadir comandos para priorizar tareas
- Ver el historial de tareas completadas
- Asignar tareas a agentes específicos
- Recibir notificaciones cuando tareas completen
- Añadir comandos para filtrar tareas por estado/prioridad
