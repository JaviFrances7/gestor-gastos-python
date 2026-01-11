# Data Model

## Entidad principal: Gasto

Un gasto representa una salida de dinero realizada por el usuario.

### Atributos

- Importe  
  Cantidad numérica mayor que cero.

- Categoría  
  Clasificación del gasto (ej. alimentación, transporte, ocio).

- Fecha  
  Fecha en la que se realizó el gasto.

- Descripción  
  Texto opcional que proporciona contexto adicional.

## Validaciones

- El importe debe ser un número positivo.
- La fecha debe tener un formato válido.
- La categoría no puede estar vacía.

## Consideraciones

- El modelo está diseñado para ser fácilmente extensible.
- Se podrían añadir nuevos campos sin afectar la estructura general.
