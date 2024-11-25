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