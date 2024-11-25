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