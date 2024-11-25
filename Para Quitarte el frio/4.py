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