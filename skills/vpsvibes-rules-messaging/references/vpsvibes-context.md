# VPSVibes: localizador de integración

Instancia solicitada: https://vpsvibes.softvibes.cloud/.
Ubicación observada del servidor: /opt/vps-status-dashboard.
Servicio: vps-status-dashboard.service. Backend Python y frontend index.html.
Revalidar estos datos antes de operar; no son garantía de estado actual.

## Fuentes

- Leer README.md, app.py, index.html y profile-inventory.py del proyecto real.
- El colector publica /run/vps-status-hermes-profiles.json; es inventario, no almacenamiento durable de reglas.
- Plan local de diseño: /Users/USERNAME/Documents/SoftvibesLab/vpsvibes-planning/PLAN-reglas-mensajes.md.
- Si el plan no está disponible en otro host, usar esta skill para redescubrir contratos; no suponer que el módulo fue implementado.

## Restricciones

Preservar separación del web y /root/.hermes. No traer tokens al navegador.
Usar snapshots SQLite vía backup API si aparece una DB operativa.
Importar configuración efectiva de recursos, no reproducir valores históricos como hechos.
El aviso manual de Pepito es una plantilla de caso de uso, no un job que se deba reenviar.

## Verificación

Revisar HTTPS y autenticación por separado; 401 solo acredita rechazo anónimo.
Comprobar UI → API → persistencia → worker → recibo antes de declarar operativo.
Skills instaladas, automatizaciones programadas y preferencias aplicadas son estados distintos.
