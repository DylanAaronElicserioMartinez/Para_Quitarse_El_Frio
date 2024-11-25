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