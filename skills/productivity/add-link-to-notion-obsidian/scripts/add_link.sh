#!/bin/bash

# Script to add a link or image to both Notion and Obsidian
# Usage: ./add_link.sh "https://example.com" or ./add_link.sh "/path/to/image.jpg"

set -euo pipefail

# Get the input (URL or file path)
INPUT="$1"

if [ -z "$INPUT" ]; then
  echo "Error: Please provide a URL or file path"
  exit 1
fi

# Determine if it's a URL or file path
if [[ "$INPUT" =~ ^https?:// ]]; then
  CONTENT_TYPE="Link"
  DESCRIPTION="$INPUT"
else
  # Check if file exists
  if [ ! -f "$INPUT" ]; then
    echo "Error: File not found: $INPUT"
    exit 1
  fi
  CONTENT_TYPE="Image"
  DESCRIPTION="$INPUT"
fi

# Ask for confirmation
echo "¿Quieres guardar este $CONTENT_TYPE en Notion y Obsidian?"
echo "$DESCRIPTION"
read -p "Responde 'sí' o 'no': " CONFIRMATION

if [[ "$CONFIRMATION" != "sí" ]] && [[ "$CONFIRMATION" != "si" ]] && [[ "$CONFIRMATION" != "yes" ]] && [[ "$CONFIRMATION" != "y" ]]; then
  echo "Operación cancelada."
  exit 0
fi

# Get Notion API key from environment
NOTION_API_KEY="${NOTION_API_KEY:-}"
if [ -z "$NOTION_API_KEY" ]; then
  echo "Error: NOTION_API_KEY not found in environment"
  exit 1
fi

# Get Obsidian vault path
OBSIDIAN_VAULT_PATH="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"
if [ ! -d "$OBSIDIAN_VAULT_PATH" ]; then
  echo "Error: Obsidian vault not found at $OBSIDIAN_VAULT_PATH"
  exit 1
fi

# Get Notion database ID from memory or prompt
NOTION_DB_ID="${NOTION_DEFAULT_DB_ID:-}"
if [ -z "$NOTION_DB_ID" ]; then
  echo "Please provide your Notion database ID:"
  read NOTION_DB_ID
fi

# Create timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
DATE_ONLY=$(date +"%Y-%m-%d")

# Create Notion page
echo "Creating Notion page..."
NOTION_RESPONSE=$(curl -s -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d "{
    \"parent\": {\"database_id\": \"$NOTION_DB_ID\"},
    \"properties\": {
      \"Name\": {
        \"title\": [
          {
            \"text\": {
              \"content\": \"$DESCRIPTION\"
            }
          }
        ]
      },
      \"URL\": {
        \"url\": \"$INPUT\"
      },
      \"Added\": {
        \"date\": {
          \"start\": \"$DATE_ONLY\"
        }
      },
      \"Type\": {
        \"select\": {
          \"name\": \"$CONTENT_TYPE\"
        }
      }
    }
  }" | jq -r '.id // empty')

if [ -z "$NOTION_RESPONSE" ]; then
  echo "Error: Failed to create Notion page"
  curl -s -X POST "https://api.notion.com/v1/pages" \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d "{
      \"parent\": {\"database_id\": \"$NOTION_DB_ID\"},
      \"properties\": {
        \"Name\": {
          \"title\": [
            {
              \"text\": {
                \"content\": \"$DESCRIPTION\"
              }
            }
          ]
        },
        \"URL\": {
          \"url\": \"$INPUT\"
        },
        \"Added\": {
          \"date\": {
            \"start\": \"$DATE_ONLY\"
          }
        },
        \"Type\": {
          \"select\": {
            \"name\": \"$CONTENT_TYPE\"
          }
        }
      }
    }"
  exit 1
fi

echo "Notion page created successfully: $NOTION_RESPONSE"

# Create Obsidian note
echo "Creating Obsidian note..."

# Sanitize filename from URL or use timestamp
if [[ "$INPUT" =~ ^https?:// ]]; then
  # Extract domain and path for filename
  FILENAME=$(echo "$INPUT" | sed 's/https\?:\/\///' | tr '/:' '-' | cut -c1-50)
  if [ -z "$FILENAME" ]; then
    FILENAME="link_$DATE_ONLY"
  fi
else
  # Use basename for file
  FILENAME=$(basename "$INPUT" | sed 's/\.[^.]*$//')
  if [ -z "$FILENAME" ]; then
    FILENAME="image_$DATE_ONLY"
  fi
fi

# Ensure filename is valid
FILENAME=$(echo "$FILENAME" | tr -cd '[:alnum:]_-.')
if [ -z "$FILENAME" ]; then
  FILENAME="item_$DATE_ONLY"
fi

NOTE_PATH="$OBSIDIAN_VAULT_PATH/Inbox/${FILENAME}.md"

# Create Inbox directory if it doesn't exist
mkdir -p "$OBSIDIAN_VAULT_PATH/Inbox"

# Create note content
if [ "$CONTENT_TYPE" = "Image" ]; then
  # For images, use relative path from vault
  RELATIVE_PATH="${INPUT#$OBSIDIAN_VAULT_PATH/}"
  cat > "$NOTE_PATH" << EOF
# $DESCRIPTION

![Image]($RELATIVE_PATH)

Added: $TIMESTAMP
EOF
else
  # For links
  cat > "$NOTE_PATH" << EOF
# $DESCRIPTION

[$DESCRIPTION]($INPUT)

Added: $TIMESTAMP
EOF
fi

echo "Obsidian note created: $NOTE_PATH"

echo "✅ Successfully saved to both Notion and Obsidian!"