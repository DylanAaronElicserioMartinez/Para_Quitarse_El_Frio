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

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def filtrar_palabras(lista_palabras, n):

    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Ejemplo de uso:

if __name__ == "__main__":

    lista = ["hola", "mundo", "programación", "Python", "función", "red"]
    
    n = 5
    
    resultado = filtrar_palabras(lista, n)
    
    print(resultado)  # Salida: ['programación', 'Python', 'función']

![image](https://github.com/user-attachments/assets/db42a282-2df7-464f-b198-d25b91a9521e)

![image](https://github.com/user-attachments/assets/89ce4cf0-3eaf-47da-a8da-f396e1429286)

#Codigo 4

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

# Solicitar al usuario que ingrese una cadena

cadena = input("Por favor, ingresa una cadena: ")

# Inicializar un contador para las letras mayúsculas

contador_mayusculas = 0

# Recorrer cada carácter en la cadena

for caracter in cadena:

    # Verificar si el carácter es una letra mayúscula
    
    if caracter.isupper():
    
        contador_mayusculas += 1

# Mostrar el resultado

print(f"La cadena contiene {contador_mayusculas} letras mayúsculas.")

![image](https://github.com/user-attachments/assets/1ca591f3-0193-4b21-8efe-925fa2be7381)

![image](https://github.com/user-attachments/assets/b82aa0d3-54b1-44c3-9c0d-c81e964fa226)

#Codigo 5

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

# Solicitar al usuario que ingrese un número binario

numero_binario = input("Por favor, ingresa un número binario: ")

# Verificar si la entrada es un número binario válido

if all(bit in '01' for bit in numero_binario):

    # Convertir el número binario a entero
    
    numero_entero = int(numero_binario, 2)
    
    # Mostrar el resultado
    
    print(f"El número binario {numero_binario} es igual a {numero_entero} en decimal.")
    
else:

    print("Error: La entrada no es un número binario válido.")

![image](https://github.com/user-attachments/assets/c9055b1b-5e51-497a-b526-bcd52a5dea32)

![image](https://github.com/user-attachments/assets/ec0f9043-6692-4e7f-b881-0aa5a615b5bf)

#Codigo 6

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

# Solicitar el año en curso

año_actual = int(input("Ingrese el año en curso: "))

# Inicializar una lista para almacenar la información de las personas

personas = []

# Ingresar información de tres personas

for i in range(3):

    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: ")
    
    edad = año_actual - año_nacimiento  # Calcular la edad
    
    personas.append((nombre, edad))  # Agregar a la lista

# Imprimir la edad que cumplirán durante el año en curso

print("\nAños que cumplirán durante el año en curso:")

for nombre, edad in personas:

    print(f"{nombre} cumplirá {edad} años.")

![image](https://github.com/user-attachments/assets/f7412c03-149f-451d-b528-ce589612b3da)

![image](https://github.com/user-attachments/assets/adfdcbf0-30b0-4846-815d-29ed8117d49a)

#Codigo 7

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

# Inicializar una lista para almacenar las edades

edades = []

# Solicitar al usuario que ingrese 10 edades

for i in range(10):

    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    
    edades.append(edad)  # Agregar la edad a la lista

# Convertir la lista a una tupla

tupla_edades = tuple(edades)

# Contar cuántas personas tienen edades superiores a 20

cantidad_superiores_20 = sum(1 for edad in tupla_edades if edad > 20)

# Imprimir el resultado

print(f"\nCantidad de personas con edades superiores a 20: {cantidad_superiores_20}")

![image](https://github.com/user-attachments/assets/b3d4df1c-395f-4930-9cf2-bada40937d76)

![image](https://github.com/user-attachments/assets/a787b464-3ba3-40ae-aa75-65dfa19c0eb0)

#Codigo 8

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

# Definir una lista de nombres

nombres = ["Ana", "Luis", "Alberto", "María", "Alejandra", "Pedro", "Antonio", "Laura", "Adriana", "Jorge"]

# Solicitar al usuario que ingrese una letra

letra = input("Ingrese una letra para buscar nombres que comiencen con ella: ").lower()

# Contar cuántos nombres comienzan con la letra proporcionada

cantidad_nombres = sum(1 for nombre in nombres if nombre.lower().startswith(letra))

# Imprimir el resultado

print(f"\nCantidad de nombres que comienzan con la letra '{letra}': {cantidad_nombres}")

![image](https://github.com/user-attachments/assets/6e610fa0-6eb5-40c7-afdd-9129c574b2c1)

![image](https://github.com/user-attachments/assets/7530d665-424d-4e72-8269-8c0ee48f1ab2)

#Codigo 9

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def contar_vocales(palabra):

    # Inicializar un diccionario para contar las vocales
    
    conteo_vocales = {
    
        'a': 0,
        
        'e': 0,
        
        'i': 0,
        
        'o': 0,
        
        'u': 0
        
    }
    
    # Contar las vocales en la palabra
    
    for letra in palabra.lower():  # Convertir la palabra a minúsculas para contar sin distinción
    
        if letra in conteo_vocales:
        
            conteo_vocales[letra] += 1
            
    return conteo_vocales

# Solicitar al usuario que ingrese una palabra

palabra_usuario = input("Ingrese una palabra: ")

# Llamar a la función y obtener el conteo de vocales

resultado = contar_vocales(palabra_usuario)

# Imprimir el resultado

print("\nConteo de vocales:")

for vocal, cantidad in resultado.items():

    print(f"{vocal}: {cantidad}")

![image](https://github.com/user-attachments/assets/57518b66-043b-4bbf-b852-b52abc987232)

![image](https://github.com/user-attachments/assets/c7c4e158-fea2-4155-825f-e7213a1fc804)

#Codigo 10

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def es_bisiesto(año):

    """
    
    Determina si un año es bisiesto.
    
    Un año es bisiesto si es divisible por 4,
    
    pero no por 100, a menos que también sea divisible por 400.
    
    """
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    
        return True
        
    else:
    
        return False

# Solicitar al usuario que ingrese un año

año_usuario = int(input("Ingrese un año: "))

# Llamar a la función y mostrar si el año es bisiesto o no

if es_bisiesto(año_usuario):

    print(f"{año_usuario} es un año bisiesto.")
    
else:

    print(f"{año_usuario} no es un año bisiesto.")

![image](https://github.com/user-attachments/assets/64326a55-3d63-4159-9f61-2bf9025c9d71)

![image](https://github.com/user-attachments/assets/b5976051-0ede-4719-a5d4-9c7f6888b7b9)

