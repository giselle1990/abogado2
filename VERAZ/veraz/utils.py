# tu_app/utils.py

def verificar_supresion_de_datos():
    print("Bienvenido al sistema de verificación de supresión de datos en el Veraz")
    print("Por favor, elija una opción:")
    print("1. Deuda de préstamos (de 2018 para atrás)")
    print("2. Deuda de tarjeta de crédito (de 2020 para atrás)")
    print("3. Deudas telefónicas e internet (de 2021 para atrás)")

    opcion = input("Ingrese el número de la opción elegida: ")

    if opcion == "1":
        anio_limite = 2018
    elif opcion == "2":
        anio_limite = 2020
    elif opcion == "3":
        anio_limite = 2021
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        return

    anio_deuda = int(input("Ingrese el año de la deuda: "))

    if anio_deuda <= anio_limite:
        print("Puede iniciar el trámite de supresión de datos.")
        nombre = input("Ingrese su nombre: ")
        telefono = input("Ingrese su número de teléfono: ")
        email = input("Ingrese su dirección de correo electrónico: ")
        print("Por favor complete el siguiente formulario de contacto:")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Correo electrónico: {email}")
    else:
        print("No es posible hacer el reclamo, ya que la deuda no cumple con el plazo requerido.")
