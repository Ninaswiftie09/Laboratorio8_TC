import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Ejercicio 3: 50%
# PARTE A:
#
# Primer for (i): recorre desde 1 hasta n/3 → O(n)
# Segundo for (j): incrementa de 4 en 4 → O(n/4) = O(n)
#
# Total: O(n) * O(n) = O(n²)
#
# Por lo tanto, la complejidad de tiempo de este algoritmo es:
#            T(n) = O(n²)


# PARTE B: Implementación y medición de tiempos

def function3(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            _ = "Sequence"  


def main():
    valores_n = [1, 10, 100, 1000, 5000, 10000]
    tiempos = []

    for n in valores_n:
        inicio = time.perf_counter()
        function3(n)
        fin = time.perf_counter()
        duracion = fin - inicio
        tiempos.append(duracion)
        print(f"n = {n:<7} | tiempo = {duracion:.6f} s")

    # Graficar 
    plt.figure(figsize=(7, 4))
    plt.plot(valores_n, tiempos, marker='o', color='orange', linewidth=2)
    plt.title("Ejercicio 3 - Tiempos de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafica_ej3.png", dpi=300)
    print("Gráfica guardada como grafica_ej3.png")


if __name__ == "__main__":
    main()
