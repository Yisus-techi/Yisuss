"""Calculadora básica para aprender Python, Git y GitHub."""


def leer_numero(mensaje):
    """Solicita un número y valida que sea correcto."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número.")


def calcular(operacion, a, b):
    """Realiza la operación seleccionada."""
    if operacion == "1":
        return a + b
    elif operacion == "2":
        return a - b
    elif operacion == "3":
        return a * b
    elif operacion == "4":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b
    elif operacion == "5":
        return a ** b
    else:
        raise ValueError("Operación no válida.")


def main():
    print("=" * 40)
    print("      MI PRIMER PROGRAMA EN PYTHON")
    print("          Calculadora básica")
    print("=" * 40)

    while True:
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("0. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            print("¡Gracias por usar la calculadora!")
            break

        if opcion not in {"1", "2", "3", "4", "5"}:
            print("Opción no válida.")
            continue

        numero1 = leer_numero("Escribe el primer número: ")
        numero2 = leer_numero("Escribe el segundo número: ")

        try:
            resultado = calcular(opcion, numero1, numero2)
            print(f"Resultado: {resultado:g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
