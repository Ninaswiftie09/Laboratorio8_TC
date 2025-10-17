import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Ejercicio 1: 25%

# PARTE A:
#
# Primer for (i):   desde n/2 hasta n  →  O(n)
# Segundo for (j):  hasta n - n/2      →  O(n)
# Tercer for (k):   multiplica por 2   →  O(log n)
#
# Total: O(n) * O(n) * O(log n) = O(n^2 * log n)
#
# Por lo tanto, la complejidad de tiempo de este algoritmo es:
#            T(n) = O(n² log n)



def function1(n): 
    # contador para registrar cuántas veces entra al bucle más interno
    contador = 0
    for i in range(n // 2, n + 1):                   # i va desde la mitad hasta n
        for j in range(1, n - n // 2 + 1):           # j recorre hasta que j + n/2 <= n
            k = 1
            while k <= n:                            # este while crece de forma logarítmica
                contador += 1
                k *= 2                               # k toma valores 1, 2, 4, 8,y así sucesivamente
    return contador


# PARTE B: 

def main():
    valores_n = [1, 10, 100, 1000, 10000]
    tiempos = []

    for n in valores_n:
        inicio = time.perf_counter()
        function1(n)
        fin = time.perf_counter()
        duracion = fin - inicio
        tiempos.append(duracion)
        print(f"n = {n:<7}  |  tiempo = {duracion:.6f} s")

    # Graficar
    plt.figure(figsize=(7, 4))
    plt.plot(valores_n, tiempos, marker='o', color='purple', linewidth=2)
    plt.title("Ejercicio 1 - Tiempos de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafica_ej1.png", dpi=300)
    print("Gráfica guardada como grafica_ej1.png")


if __name__ == "__main__":
    main()


