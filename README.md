# Skills Hermes — edición pública

Colección exportada del catálogo de skills disponible en una instalación de Hermes. Incluye **560 nombres únicos**, **561 archivos SKILL.md** y los scripts, plantillas y referencias de texto publicables. Graphify aparece en dos ubicaciones; no se han fusionado sus variantes.

Esta es una **copia pública saneada**, no un respaldo idéntico de la instalación ni una certificación de funcionamiento de todas las skills.

## Descarga y navegación

- [Descargar el paquete ZIP](https://github.com/softvibeslab/skillshermes/releases/latest/download/skillshermes-public.zip)
- [Catálogo navegable](CATALOG.md)
- [Catálogo JSON](catalog.json)
- [Omisiones y sanitización](PUBLICATION_REPORT.json)
- [Manifiesto de integridad](manifest.json)

## Contenido

- `skills/`: habilidades organizadas por categoría, con sus recursos de texto.
- Las skills externas de BeGlobal y Nirvana están incluidas como archivos reales; no se requiere resolver enlaces simbólicos de la máquina original.
- Se conservan ambas variantes de Graphify para revisión. Selecciona una si tu cargador no tolera nombres duplicados.

## Uso

1. Descarga y descomprime el paquete en un directorio nuevo.
2. Ejecuta `python3 verify_package.py` desde ese directorio.
3. Revisa el `SKILL.md` de la habilidad que necesitas y copia su carpeta completa a tu directorio de skills de Hermes. Conserva referencias y scripts; no sobrescribas habilidades existentes sin comparar y respaldar antes.

No hay instalador automático ni instalación masiva: algunas skills requieren herramientas, runtimes, proveedores o permisos adicionales. La presencia del archivo no acredita compatibilidad ni configuración. Las rutas `/Users/USERNAME`, identificadores de ejemplo y valores `REDACTED_*` deben adaptarse a tu entorno; no representan accesos funcionales.

## Privacidad y alcance

La publicación pública fue autorizada expresamente con anonimización y exclusión de referencias privadas. Se sustituyeron 16 referencias por avisos, se retiró la sección operativa privada de una skill y se eliminaron valores sensibles detectados. Se excluyeron estado interno, respaldos, cachés y cuatro imágenes/animaciones binarias de ejemplos. El informe enumera las rutas afectadas.

No se exportaron perfiles, memorias, sesiones, archivos `.env`, credenciales de proveedores ni bases de datos de usuarios. Los ejemplos sintéticos de seguridad y fixtures pueden activar detectores de secretos; no deben utilizarse como credenciales reales. La revisión automatizada y focalizada reduce riesgos, pero no constituye una garantía absoluta de ausencia de información sensible.

Solo se comprobó la estructura e integridad del paquete. **No se ejecutaron los scripts de las skills ni se validaron sus dependencias o servicios.** La instalación original no fue modificada.

## Licencias

Esta colección no cambia las licencias de sus componentes ni otorga una licencia global. Conserva avisos, autores y licencias presentes en cada skill. Algunas contienen condiciones específicas —por ejemplo, el puente Nirvana declara SUL-1.0— y otras no incluyen una licencia expresa. Verifica los términos del autor original antes de redistribuir, modificar o dar uso comercial. No supongas que todo el repositorio es MIT.
