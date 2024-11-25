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