# Architecture Overview

## Enfoque general

La aplicación sigue una arquitectura modular basada en la separación de responsabilidades.
Cada módulo tiene una única función clara, lo que facilita el mantenimiento, el testing y la escalabilidad.

La lógica de negocio se mantiene desacoplada de la interfaz de usuario y de la persistencia de datos.

## Capas principales

### 1. Interfaz de usuario (CLI)

Responsable de:
- Mostrar opciones al usuario
- Recoger entradas desde la terminal
- Mostrar resultados

No contiene lógica de negocio ni acceso directo a datos.

### 2. Lógica de negocio

Responsable de:
- Validar datos
- Procesar gastos
- Aplicar reglas del dominio (cálculos, resúmenes)

No depende de la interfaz ni del método de almacenamiento.

### 3. Persistencia de datos

Responsable de:
- Guardar los gastos
- Recuperar información almacenada

Puede ser reemplazada en el futuro sin afectar al resto del sistema.

## Flujo de la aplicación

1. El usuario interactúa con la interfaz CLI.
2. La interfaz delega las acciones a la lógica de negocio.
3. La lógica de negocio consulta o persiste datos.
4. Los resultados vuelven a la interfaz para ser mostrados al usuario.
