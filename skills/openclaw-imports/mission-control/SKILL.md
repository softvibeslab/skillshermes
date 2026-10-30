---
name: mission-control
description: Create and manage tasks in Mission Control via Telegram commands
user-invocable: true
---

# Mission Control

Use this skill to interact with Mission Control task management system through Telegram.

## Available Commands

### Create Task
Create a new task in Mission Control:
```
/mission create <task description>
```
Example: `/mission create Investigar error en el API de usuarios`

### List Tasks
Show all active tasks:
```
/mission list
```

### Task Status
Check the status of a specific task:
```
/mission status <task-id>
```

### Cancel Task
Cancel a running task:
```
/mission cancel <task-id>
```

### Health Check
Check Mission Control status:
```
/mission health
```

## How It Works

When you send a command via Telegram to @rogermac_bot, OpenClaw receives the message and uses this skill to process it.

## Implementation Instructions for OpenClaw Agent

When a Telegram message starts with `/mission`, use the http tool to call Mission Control API:

### Example API Calls

**Create Task:**
```json
{
  "url": "http://localhost:4001/api/tasks",
  "method": "POST",
  "headers": {"Content-Type": "application/json"},
  "body": {
    "description": "Extract from user message after 'create'",
    "priority": "medium"
  }
}
```

**List Tasks:**
```json
{
  "url": "http://localhost:4001/api/tasks",
  "method": "GET"
}
```

**Task Status:**
```json
{
  "url": "http://localhost:4001/api/tasks/{task-id}",
  "method": "GET"
}
```

**Cancel Task:**
```json
{
  "url": "http://localhost:4001/api/tasks/{task-id}",
  "method": "DELETE"
}
```

**Health Check:**
```json
{
  "url": "http://localhost:4001/api/health",
  "method": "GET"
}
```

### Response Format

Mission Control returns JSON. Format it nicely for Telegram:

- Health: Show components.status, components.gateway.connected, components.agents.active_count
- Tasks: List id, description, status, priority for each task
- Errors: Show error message clearly

## Task Flow

1. User sends `/mission <command>` via Telegram
2. OpenClaw agent receives the message
3. Parse command (create/list/status/cancel/health) and arguments
4. Make appropriate HTTP request to http://localhost:4001
5. Format JSON response for Telegram
6. Send response back to user via Telegram

## Error Handling

- If Mission Control is not running (connection refused), inform the user to start it: `cd ~/mission-control && npm run dev`
- If task creation fails (400/500), show the error message from response
- If task ID is invalid (404), report "Task not found" to user
- Always handle network errors gracefully
