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
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = año_actual - año_nacimiento  # Calcular la edad
    personas.append((nombre, edad))  # Agregar a la lista

# Imprimir la edad que cumplirán durante el año en curso
print("\nAños que cumplirán durante el año en curso:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años.")