import math
def calcular_distancia_recta_humano():
    """
    Calcula las coordenadas Y y la distancia entre dos puntos 
    sobre una recta (Y = AX + B) con un formato de salida más natural.
    """
    print("---  Calculadora de Puntos y Distancia en una Recta ---")
    print("Vamos a trabajar con la ecuación de primer grado: Y = AX + B")
    
    try:
        # Peticiones más conversacionales
        A = float(input("\n1. Introduce el coeficiente A (pendiente): "))
        B = float(input("2. Introduce el coeficiente B (ordenada al origen): "))
        X1 = float(input("3. Dame la coordenada X del primer punto (X1): "))
        X2 = float(input("4. Dame la coordenada X del segundo punto (X2): "))
    except ValueError:
        print("\n¡Ojo! Solo se aceptan números. Por favor, reinicia e inténtalo de nuevo.")
        return

    signo_B = "+" if B >= 0 else ""
    print("\n---------------------------------------------------")
    print(f" Entendido La ecuación que usaremos es: Y = {A}X {signo_B}{B}")
    
    Y1 = (A * X1) + B
    Y2 = (A * X2) + B
    Y1_redondeado = round(Y1, 2)
    Y2_redondeado = round(Y2, 2)

    print("\n--- Resultados de las Coordenadas Y ---")
    print(f"Para X1 = {X1}: Y1 = ({A} * {X1}) + {B} = {Y1_redondeado}")
    print(f"Para X2 = {X2}: Y2 = ({A} * {X2}) + {B} = {Y2_redondeado}")
    
    print(f"\nLos puntos de la recta son:")
    print(f"  Punto 1 (P1): ({X1}, {Y1_redondeado})")
    print(f"  Punto 2 (P2): ({X2}, {Y2_redondeado})")
    
    delta_x = X2 - X1
    delta_y = Y2 - Y1  
    
    distancia_cuadrada = (delta_x ** 2) + (delta_y ** 2)
    distancia = math.sqrt(distancia_cuadrada)

    print("\n--- Cálculo de la Distancia ---")
    print("Aplicamos la fórmula de distancia: d = √(ΔX² + ΔY²)")
    print(f"ΔX = {X2} - {X1} = {round(delta_x, 2)}")
    print(f"ΔY = {Y2} - {Y1} = {round(delta_y, 2)}")
    print(f"\nLa distancia entre P1 y P2 es: {distancia_redondeada}")
    print("---------------------------------------------------")
if __name__ == "__main__":
    calcular_distancia_recta_humano()
