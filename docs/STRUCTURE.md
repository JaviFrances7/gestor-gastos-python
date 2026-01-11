# Project Structure

La estructura del proyecto está diseñada para reflejar la arquitectura de la aplicación y facilitar su crecimiento.

## Estructura propuesta

- `main.py`
  Punto de entrada de la aplicación.

- `ui/`
  Maneja la interacción con el usuario (CLI).

- `services/`
  Contiene la lógica de negocio y procesamiento de gastos.

- `data/`
  Maneja la persistencia y acceso a los datos.

- `models/`
  Define las entidades del dominio (por ejemplo, gasto).

- `tests/`
  Contiene pruebas unitarias y de integración.

- `docs/`
  Documentación adicional del proyecto.

## Principios aplicados

- Separación de responsabilidades
- Bajo acoplamiento entre módulos
- Alta cohesión interna
