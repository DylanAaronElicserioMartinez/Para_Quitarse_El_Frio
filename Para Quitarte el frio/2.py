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
