# Respaldo verificable de multimedia de WhatsApp en Google Drive

Úsalo para liberar espacio en macOS sin arriesgar el historial de chats.

## Principio

No copies cientos de miles de archivos individualmente a Drive. Empaquétalos en TAR independientes y reanudables, registra cada archivo en SQLite y elimina originales únicamente después de verificar todos los objetos remotos.

## Flujo mínimo

1. Ubica la carpeta `Message/Media` del contenedor compartido de WhatsApp. No incluyas bases de datos, sesiones ni configuración.
2. Haz un inventario SQLite con `path`, `size`, `mtime_ns` y `chunk`.
3. Divide por bytes (por ejemplo, ~6 GB) en TAR independientes; no hagas un TAR único ni volúmenes encadenados.
4. Antes de archivar cada archivo, exige que tamaño y `mtime_ns` sigan iguales. Si cambió, detén ese paquete en vez de respaldar una mezcla incoherente.
5. Verifica localmente el número de miembros del TAR.
6. Calcula MD5 y súbelo con `MediaFileUpload(..., resumable=True)`.
7. Acepta el paquete solo si Drive devuelve el mismo `md5Checksum` y tamaño.
8. Guarda en SQLite `drive_id`, tamaño del archivo, MD5 y `uploaded=1`; borra el TAR local para recuperar espacio.
9. Al completar, sube también el manifiesto y un README de restauración.
10. Marca `all_verified=1` solo cuando todos los paquetes estén verificados.
11. Si se pidió liberar espacio, elimina exclusivamente archivos cuyo tamaño y `mtime_ns` aún coincidan con el manifiesto. Registra borrados y omitidos.

## Operación segura en segundo plano

- Pausa el proceso/extensión de WhatsApp para evitar escrituras durante el inventario y empaquetado.
- Usa `trap` para reanudarlo en `EXIT`, `INT` y `TERM`.
- Envuelve el proceso con `caffeinate` para mantener despierta la Mac.
- Ejecuta como proceso rastreable con notificación al terminar y escribe un log persistente.
- Reanuda consultando `uploaded=0`; nunca repitas paquetes confirmados en Drive.

Esqueleto:

```bash
cleanup() { kill -CONT "$WA_PID" 2>/dev/null || true; }
trap cleanup EXIT INT TERM
kill -STOP "$WA_PID" 2>/dev/null || true
caffeinate -dimsu python3 backup.py --delete-after-verify >> backup.log 2>&1
```

## Verificación final obligatoria

No confíes únicamente en la notificación o el exit code del wrapper: shells y hooks de cierre pueden imprimir errores ajenos.

Comprueba por separado:

- manifiesto: `count(chunks) == sum(uploaded)` y `pending == 0`;
- bandera `all_verified=1`;
- Drive: cantidad esperada de TAR, manifiesto y README presentes;
- todos los objetos tienen tamaño y MD5;
- si hubo borrado: `removed_files`, `removed_bytes` y `skipped_changed_files`;
- WhatsApp ya no está pausado;
- espacio libre real en el volumen de datos.

Si Drive y el manifiesto coinciden, un mensaje incidental del shell después del proceso no invalida el respaldo.