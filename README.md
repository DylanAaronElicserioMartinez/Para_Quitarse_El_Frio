# Para_Quitarse_El_Frio
Actividad en clase

#Codigo 1

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

![image](https://github.com/user-attachments/assets/45be63f8-6d06-4b0b-82a7-5403b633a595)

![image](https://github.com/user-attachments/assets/d20e96f0-8f46-40bb-a3c7-75859a5b75cf)

#Codigo 2

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def mas_larga(lista_palabras):

    if not lista_palabras:  # Verifica si la lista está vacía
    
        return None
        
    palabra_larga = lista_palabras[0]  # Inicializa con la primera palabra
    
    for palabra in lista_palabras:
    
        if len(palabra) > len(palabra_larga):  # Compara longitudes
        
            palabra_larga = palabra
            
    return palabra_larga

# Ejemplo de uso

palabras = ["hola", "mundo", "programación", "Python"]

resultado = mas_larga(palabras)

print(f"La palabra más larga es: '{resultado}'")  # Debería imprimir "programación"

![image](https://github.com/user-attachments/assets/b17d0a4e-d696-4181-889d-f569a0adba64)

![image](https://github.com/user-attachments/assets/8b023489-bf4a-4041-8f2a-e97c17598b1f)

#Codigo 3



