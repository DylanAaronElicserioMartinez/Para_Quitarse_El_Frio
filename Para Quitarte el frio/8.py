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