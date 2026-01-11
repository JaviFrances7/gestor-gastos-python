from services.expense_services import ServicioGastos


def ejecutar():
    """
    Función principal de la interfaz de línea de comandos.
    Se encarga de mostrar el menú, pedir datos al usuario
    y mostrar resultados utilizando el ServicioGastos.
    """
    servicio = ServicioGastos()

    while True:
        print("\n--- GESTOR DE GASTOS ---")
        print("1. Añadir gasto")
        print("2. Ver gastos")
        print("3. Ver resumen por categoría")
        print("4. Resetear todos los gastos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_gasto(servicio)

        elif opcion == "2":
            mostrar_gastos(servicio)

        elif opcion == "3":
            mostrar_resumen(servicio)

        elif opcion == "4":
            resetear_gastos(servicio)

        elif opcion == "5":
            print("Saliendo de la aplicación...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


def agregar_gasto(servicio):
    """
    Pide al usuario los datos de un gasto y lo registra.
    """
    try:
        texto_importe = input("Importe: ")
        texto_importe = texto_importe.replace(",", ".")
        importe = float(texto_importe)
        categoria = input("Categoría: ")
        fecha = input("Fecha (DD-MM-YYYY): ")
        descripcion = input("Descripción (opcional): ")

        gasto = servicio.agregar_gasto(
            importe=importe,
            categoria=categoria,
            fecha=fecha,
            descripcion=descripcion,
        )

        print("\nGasto añadido correctamente:")
        print(gasto)

    except Exception as error:
        print(f"\nError al añadir gasto: {error}")


def mostrar_gastos(servicio):
    """
    Muestra todos los gastos registrados.
    """
    gastos = servicio.obtener_gastos()

    if not gastos:
        print("\nNo hay gastos registrados.")
        return

    print("\n--- LISTA DE GASTOS ---")
    for gasto in gastos:
        print(gasto)


def mostrar_resumen(servicio):
    """
    Muestra el resumen total de gastos por categoría.
    """
    resumen = servicio.obtener_resumen()

    if not resumen:
        print("\nNo hay gastos para mostrar.")
        return

    print("\n--- RESUMEN POR CATEGORÍA ---")
    for categoria, total in resumen.items():
        print(f"{categoria}: {total:.2f} €")

def resetear_gastos(servicio):
    """
    Borra todos los gastos tras confirmación del usuario.
    """
    confirmacion = input(
        "¿Seguro que quieres borrar TODOS los gastos? (si/no): "
    ).lower()

    if confirmacion == "si":
        servicio.resetear_gastos()
        print("\nTodos los gastos han sido borrados.")
    else:
        print("\nOperación cancelada.")




         