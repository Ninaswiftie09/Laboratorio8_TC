import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Ejercicio 2: 25%

# PARTE A:
#
# Primer for (i):  de 1 a n → O(n)
# Segundo for (j): rompe al primer ciclo → O(1)
#
# Total: O(n) * O(1) = O(n)
#
# Por lo tanto, la complejidad de tiempo de este algoritmo es:
#            T(n) = O(n)

def function2(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            _ = "Sequence"  
            break  

def main():
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    tiempos = []

    for n in valores_n:
        inicio = time.perf_counter()
        function2(n)
        fin = time.perf_counter()
        duracion = fin - inicio
        tiempos.append(duracion)
        print(f"n = {n:<10} | tiempo = {duracion:.6f} s")

    # Graficar
    plt.figure(figsize=(7, 4))
    plt.plot(valores_n, tiempos, marker='o', color='green', linewidth=2)
    plt.title("Ejercicio 2 - Tiempos de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafica_ej2.png", dpi=300)
    print("Gráfica guardada como grafica_ej2.png")

if __name__ == "__main__":
    main()
