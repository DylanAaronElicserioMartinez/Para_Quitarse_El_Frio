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
