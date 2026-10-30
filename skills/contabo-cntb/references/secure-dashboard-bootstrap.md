# Bootstrap seguro de observabilidad web de un VPS

## Separar accesos

- La API del proveedor permite inventario; no concede acceso SSH al huésped ni autenticación web.
- Una página HTML no es un canal seguro para recibir contraseñas por sí sola. HTTPS, identidad autorizada, backend y almacenamiento deben verificarse antes de aceptar secretos.
- Preferir bootstrap SSH: el usuario escribe su contraseña en su propia terminal. Preparar una llave dedicada y obtener aprobación explícita antes de agregarla al servidor; explicar permisos y revocación. No copiar llaves privadas a formularios ni enviar la contraseña administrativa por correo.
- El código temporal de acceso web es distinto de la contraseña del VPS. Confirmar cuál solicita el usuario. Configurar y probar un mecanismo real de OTP/identidad antes de prometer correo automático.

## Descubrimiento antes de publicar

1. Confirmar destino del VPS desde inventario autorizado y compararlo con el destino SSH; no heredar una IP de ejemplos o de afirmaciones previas del asistente.
2. Probar SSH sin interacción: `ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=10 USER@HOST ...`. Un rechazo de autenticación prueba conectividad, no acceso. Una llave de host desconocida debe verificarse por un canal fiable; no desactivar su validación.
3. Consultar NS del dominio y A/AAAA/CNAME del subdominio. Distinguir proveedor DNS, hosting y proveedor de identidad. Tener cloudflared instalado no prueba autenticación ni control de la zona.
4. Inspeccionar únicamente presencia de certificados y nombres de variables de credenciales, no sus valores. Usar integraciones existentes autorizadas antes de pedir configuración nueva.
5. Un listado de sitios de hosting no es un listado de registros DNS. No crear un sitio como sustituto de crear DNS. Si no hay vía autorizada para editar DNS, proporcionar el registro exacto al usuario.
6. No sobrescribir registros existentes, mover nameservers ni tocar correo incidentalmente. Explicar el impacto y obtener autorización específica si fuese necesario.

## Dependencias y verificación

- Resolver primero acceso SSH, inventario del huésped y mecanismo de autenticación; no mantener un ciclo de preguntas sobre dominio sin desbloquear la instalación.
- Reutilizar servicios y reverse proxy existentes. Empezar con observación; no añadir consola remota ni controles destructivos.
- Para exposición directa, verificar destino A/AAAA, TLS, protección del origen y rutas/API. Para túneles, verificar tanto la política de identidad como que el origen no permita eludirla.
- Probar denegación sin autenticar y acceso con la identidad permitida, incluyendo API y métricas. No exponer exportadores, prompts, conversaciones, tokens o configuración.
- DNS resuelto no equivale a despliegue; TLS válido no equivale a autenticación. Entregar URL como operativa solo tras comprobar estas capas.
- Mostrar métricas reales y su frescura; dato ausente o antiguo no es estado saludable. Procesos compartidos no permiten atribución exacta de memoria por agente sin instrumentación.
- Al añadir un alias Caddy, preservar propietario/grupo/modo de un fragmento existente y validar también como el usuario del servicio (`runuser -u caddy -- caddy validate --config /etc/caddy/Caddyfile`). Validar como root no detecta fragmentos ilegibles para Caddy. Recargar, no reiniciar; respaldar y revertir solo archivos propios si falla.
- Para módulos /proc, conservar aislamiento/capabilities del dashboard. Reportar permisos insuficientes sin habilitar acceso a entornos privados. Muestrear en caché, no en cada petición; publicar únicamente etiquetas sanitizadas y evidencia explícita o inferida, nunca cmdline/environ completos. Si comm identifica Hermes, un lanzador Python no debe sobrescribir esa clasificación. Añadir fixture de regresión.
- Verificar autenticación con credenciales existentes solo en memoria, sin imprimirlas. En pruebas de navegador de SPA con hash, navegar a la sección y esperar visibilidad antes de capturar; elementos renderizados pueden estar ocultos. Probar escritorio/móvil, errores JS, API fresca y rechazo 401 sin credenciales.

## Reporte de avance

Separar siempre: CLI instalado / API autenticada / SSH autorizado / DNS configurado / aplicación desplegada / HTTPS verificado / acceso protegido / correo probado. No describir una propuesta o formulario estático como un dashboard seguro ya publicado.
