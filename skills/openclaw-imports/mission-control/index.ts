#!/usr/bin/env node

/**
 * Mission Control Skill for OpenClaw
 * Integrates Telegram commands with Mission Control API
 */

const http = require('http');

const MISSION_CONTROL_URL = 'http://localhost:4001';

interface MissionResponse {
  success: boolean;
  data?: any;
  error?: string;
}

function httpRequest(method: string, path: string, body?: any): Promise<MissionResponse> {
  return new Promise((resolve) => {
    const url = new URL(path, MISSION_CONTROL_URL);
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    const req = http.request(url, options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          resolve({ success: res.statusCode === 200, data: parsed });
        } catch {
          resolve({ success: res.statusCode === 200, data });
        }
      });
    });

    req.on('error', (error) => {
      resolve({ success: false, error: error.message });
    });

    if (body) {
      req.write(JSON.stringify(body));
    }
    req.end();
  });
}

async function createTask(description: string): Promise<string> {
  const response = await httpRequest('POST', '/api/tasks', {
    description,
    priority: 'medium'
  });

  if (!response.success) {
    return `❌ Error al crear tarea: ${response.error || 'Desconocido'}`;
  }

  const task = response.data;
  return `✅ Tarea creada exitosamente\n` +
         `📋 ID: ${task.id}\n` +
         `📝 Descripción: ${task.description}\n` +
         `📊 Estado: ${task.status}`;
}

async function listTasks(): Promise<string> {
  const response = await httpRequest('GET', '/api/tasks');

  if (!response.success) {
    return `❌ Error al obtener tareas: ${response.error || 'Desconocido'}`;
  }

  const tasks = response.data;
  if (!tasks || tasks.length === 0) {
    return '📋 No hay tareas activas';
  }

  let message = '📋 **Tareas Activas**\n\n';
  tasks.forEach((task: any, index: number) => {
    message += `${index + 1}. **${task.id}**\n`;
    message += `   📝 ${task.description}\n`;
    message += `   📊 Estado: ${task.status}\n`;
    message += `   🎯 Prioridad: ${task.priority}\n\n`;
  });

  return message;
}

async function getTaskStatus(taskId: string): Promise<string> {
  const response = await httpRequest('GET', `/api/tasks/${taskId}`);

  if (!response.success) {
    return `❌ Error al obtener tarea: ${response.error || 'Tarea no encontrada'}`;
  }

  const task = response.data;
  return `📋 **Tarea ${task.id}**\n\n` +
         `📝 Descripción: ${task.description}\n` +
         `📊 Estado: ${task.status}\n` +
         `🎯 Prioridad: ${task.priority}\n` +
         `🕐 Creada: ${new Date(task.createdAt).toLocaleString('es-ES')}\n` +
         `📈 Progreso: ${task.progress || 0}%`;
}

async function cancelTask(taskId: string): Promise<string> {
  const response = await httpRequest('DELETE', `/api/tasks/${taskId}`);

  if (!response.success) {
    return `❌ Error al cancelar tarea: ${response.error || 'Desconocido'}`;
  }

  return `✅ Tarea ${taskId} cancelada exitosamente`;
}

async function checkHealth(): Promise<string> {
  const response = await httpRequest('GET', '/api/health');

  if (!response.success) {
    return '❌ Mission Control no está respondiendo';
  }

  const health = response.data;
  return `✅ **Mission Control Status**\n\n` +
         `🟢 Gateway: ${health.gateway ? 'Conectado' : 'Desconectado'}\n` +
         `🧠 Modelo: ${health.model || 'No disponible'}\n` +
         `📊 Tareas activas: ${health.activeTasks || 0}\n` +
         `🕐 Uptime: ${health.uptime || 'Desconocido'}`;
}

function parseCommand(text: string): { command: string; args: string[] } {
  const parts = text.trim().split(/\s+/);
  const command = parts[0].replace('/', '').toLowerCase();
  const args = parts.slice(1);
  return { command, args };
}

export async function handleMissionControlCommand(message: string): Promise<string> {
  const { command, args } = parseCommand(message);

  try {
    switch (command) {
      case 'create':
        if (!args.length) {
          return '❌ Uso: /mission create <descripción de la tarea>';
        }
        return await createTask(args.join(' '));

      case 'list':
        return await listTasks();

      case 'status':
        if (!args.length) {
          return '❌ Uso: /mission status <task-id>';
        }
        return await getTaskStatus(args[0]);

      case 'cancel':
        if (!args.length) {
          return '❌ Uso: /mission cancel <task-id>';
        }
        return await cancelTask(args[0]);

      case 'health':
        return await checkHealth();

      default:
        return `❌ Comando desconocido: ${command}\n\n` +
               `Comandos disponibles:\n` +
               `• /mission create <descripción>\n` +
               `• /mission list\n` +
               `• /mission status <id>\n` +
               `• /mission cancel <id>\n` +
               `• /mission health`;
    }
  } catch (error) {
    return `❌ Error procesando comando: ${error.message}`;
  }
}

// For direct testing
if (require.main === module) {
  const command = process.argv[2];
  if (command) {
    handleMissionControlCommand(command).then(console.log).catch(console.error);
  } else {
    console.log('Usage: node index.ts "/mission <command>"');
  }
}
