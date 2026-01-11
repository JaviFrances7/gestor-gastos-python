**💰 Gestor de Gastos en Python (CLI)**

Proyecto personal desarrollado en Python que permite gestionar gastos personales desde la línea de comandos.
El objetivo de este proyecto es poner en práctica los fundamentos de Python, la programación orientada a objetos y una estructura de proyecto clara.

---

🎯 Objetivo del proyecto

Este proyecto está orientado a:

- Practicar Python básico e intermedio

- Aprender a estructurar un proyecto más allá de un solo archivo

- Separar responsabilidades (modelo, lógica, persistencia y UI)

- Crear una aplicación funcional y realista para un portfolio junior

---

🚀 Funcionalidades

Añadir gastos con:

- importe

- categoría

- fecha (formato DD-MM-YYYY)

- descripción opcional

- Ver todos los gastos guardados

- Ver el total gastado por categoría

- Resetear todos los gastos (pensado para uso mensual)

---

🧱 Estructura del proyecto

El proyecto está dividido en carpetas según su responsabilidad:

```
gestor-gastos/
│
├── main.py                # Archivo principal (arranque de la app)
├── requirements.txt
│
├── models/                # Modelos y validaciones
│   └── expense.py
│
├── data/                  # Gestión de datos (JSON)
│   └── repository.py
│
├── services/              # Lógica de negocio
│   └── expense_services.py
│
├── ui/                    # Interfaz de usuario (CLI)
│   └── cli.py
│
└── docs/                  # Documentación del proyecto
```

---

🧠 Cómo funciona la aplicación

- La CLI se encarga de pedir datos al usuario y mostrar resultados

- El servicio gestiona la lógica de la aplicación

- El repositorio guarda y lee los datos desde un archivo JSON

- El modelo valida los datos y garantiza que un gasto siempre sea válido

Cada parte tiene una responsabilidad concreta.

---

📅 Gestión de fechas

- El usuario introduce la fecha en formato DD-MM-YYYY

- Internamente se convierten a objetos date

- Los datos se guardan en formato estándar (YYYY-MM-DD)

- El sistema acepta ambos formatos para evitar errores con datos antiguos

---

▶️ Cómo ejecutar el proyecto

1️⃣ Clonar el repositorio

git clone https://github.com/JaviFrances7/gestor-gastos.git
cd gestor-gastos

2️⃣ Ejecutar la aplicación

python main.py

---

🧪 Ejemplo de uso

--- GESTOR DE GASTOS ---

1. Añadir gasto
2. Ver gastos
3. Ver resumen por categoría
4. Salir
5. Resetear todos los gastos

Ejemplo de entrada:

Importe: 12,5
Categoría: comida
Fecha (DD-MM-YYYY): 25-12-2025
Descripción: cena

---

🛠️ Tecnologías utilizadas

- Python 3

- JSON para persistencia de datos

- Programación orientada a objetos

- Línea de comandos (CLI)

---

📈 Posibles mejoras futuras

- Gestión de gastos por mes

- Exportar gastos a CSV

- Añadir tests automáticos

- Interfaz gráfica o web

- Validaciones más avanzadas

---

👤 Autor

Proyecto desarrollado por Javier Frances

GitHub: JaviFrances7

LinkedIn: https://es.linkedin.com/in/javier-frances-sanz
