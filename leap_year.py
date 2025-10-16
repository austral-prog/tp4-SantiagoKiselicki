def es_bisiesto(year):
    es_bisiesto_check = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return es_bisiesto_check
def programa_bisiesto_humanizado():
    print("Detector de Años Bisiestos")
    print("Vamos a verificar si un año cumple con la regla de César y Gregorio.")
    try:
        año_ingresado = int(input("Por favor, introduce el año que deseas verificar:"))
    except ValueError:
        print("\n¡Error! Solo puedo procesar números enteros. Intenta de nuevo.")
        return
    resultado = es_bisiesto(año_ingresado)
    print("Resultado del Análisis")
    if resultado:
        print(f"¡El año {año_ingresado} es bisiesto!")
        print("Esto significa que ese año tuvo 366 días.")
    else:
        print(f"El año {año_ingresado} no es bisiesto.")
        print("Este año tuvo los 365 días regulares.")
if name == "main":
    programa_bisiesto_humanizado()
