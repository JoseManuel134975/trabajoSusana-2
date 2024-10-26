
class Calculadora:
    """
    Clase Calculadora para realizar operaciones matemáticas básicas. Prueba para .yml :)))
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Calculadora.
        """
        self.resultado = 0

    def sumar(self, a, b):
        """
        Suma dos números y devuelve el resultado.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: La suma de a y b.
        """
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        """
        Resta el segundo número del primero y devuelve el resultado.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: La resta de a y b.
        """
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        """
        Multiplica dos números y devuelve el resultado.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: El producto de a y b.
        """
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        """
        Divide el primer número por el segundo y devuelve el resultado.

        Args:
            a (float): El numerador.
            b (float): El denominador.

        Returns:
            float: El resultado de la división de a por b.

        Raises:
            ValueError: Si el denominador es cero.
        """
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        self.resultado = a / b
        return self.resultado


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el valor de uno de sus lados.

    Args:
        lado (float): La longitud de un lado del cuadrado.

    Returns:
        float: El área del cuadrado.
    """
    return lado * lado


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    import math
    return math.pi * radio * radio


# Ejemplos de uso
calc = Calculadora()
print("Suma:", calc.sumar(10, 5))
print("Resta:", calc.restar(10, 5))
print("Multiplicación:", calc.multiplicar(10, 5))
print("División:", calc.dividir(10, 5))

print("Área de un cuadrado de lado 4:", calcular_area_cuadrado(4))
print("Área de un círculo de radio 3:", calcular_area_circulo(3))
