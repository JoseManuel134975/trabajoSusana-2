import random

def main():
    """
    Simula el lanzamiento de un número especificado de dados y verifica si se 
    obtiene un valor objetivo.

    Esta función es el punto de entrada del programa. Solicita al usuario el número 
    de dados a lanzar y un valor objetivo que el usuario desea conseguir. Luego, 
    simula el lanzamiento de los dados, mostrando los resultados en la consola, 
    y determina si el jugador ha ganado o perdido.

    Ejemplo de uso:
        Si el usuario ingresa '3' como número de dados y '5' como valor objetivo, 
        el programa tirará 3 dados y mostrará los resultados. Si al menos uno de 
        los dados muestra el número 5, se indicará que el jugador ha ganado.

    Funcionalidad:
        - Si el número de dados es menor que 1, se muestra un mensaje de error.
        - Si el valor objetivo es menor que 1 o mayor que 6, se muestra un mensaje 
          indicando que es imposible conseguir dicho valor.
        - Se utilizan números aleatorios para simular el lanzamiento de dados.
        - Se utiliza la función `randrange` del módulo `random` para obtener un 
          número aleatorio entre 1 y 6 (inclusive).

    Returns:
        None
    """
    print("OBTENER VALOR (2)")
    numero = int(input("Número de dados: "))
    if numero < 1:
        print("¡Imposible!")
    else:
        objetivo = int(input("Valor a conseguir: "))
        if objetivo < 1 or objetivo > 6:
            print(f"¡Imposible conseguir un {objetivo}!")
        else:
            gana = False
            print(f"Dados: ", end="")
            for _ in range(numero):
                dado = random.randrange(1, 7)
                print(f"{dado} ", end="")
                if dado == objetivo:
                    gana = True
            print()
            if gana:
                print("El jugador ha ganado.")
            else:
                print("El jugador ha perdido.")

if __name__ == "__main__":
    main()
