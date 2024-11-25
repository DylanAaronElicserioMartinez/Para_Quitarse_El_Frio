print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
def max_in_list(numbers):
    if not numbers:
        raise ValueError("La lista no puede estar vacía.")  # Lanza una excepción si la lista está vacía

    max_number = numbers[0]  # Inicializa el máximo con el primer número de la lista
    for number in numbers[1:]:  # Itera a través de los números restantes
        if number > max_number:  # Si el número actual es mayor que el máximo encontrado
            max_number = number  # Actualiza el máximo
    return max_number  # Devuelve el máximo encontrado

# Ejemplo de uso:
try:
    lista_de_numeros = [3, 5, 1, 8, 2]
    maximo = max_in_list(lista_de_numeros)
    print(f"El número máximo en la lista es: {maximo}")
except ValueError as e:
    print(e)