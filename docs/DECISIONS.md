# Technical Decisions

## Uso de una arquitectura modular

Se eligió una estructura modular para facilitar:
- Mantenimiento del código
- Testeo independiente de componentes
- Escalabilidad futura

## Uso de CLI

La interfaz de línea de comandos permite centrarse en:
- Lógica de negocio
- Buen diseño de software
- Simplicidad inicial

## Persistencia desacoplada

El sistema de almacenamiento está separado de la lógica principal para permitir cambios futuros
(ej. migrar a otra base de datos) sin reescribir la aplicación.
