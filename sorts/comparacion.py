import matplotlib.pyplot as plt

from selectionSort import main as selection
from bubbleSort import main as bubble
from insertionsort import main as insertion
from quickSort import main as quicksort

def crear_tabla():
    
    largo = [25,50,75,100]
    tiempo_b = bubble(largo)
    tiempo_s = selection(largo)
    tiempo_i = insertion(largo)
    tiempo_q = quicksort(largo)

    plt.figure(figsize=(10,6))

    plt.plot(largo, tiempo_b, label="Bubble Sort", marker="*", color="orange")
    plt.plot(largo, tiempo_s, label="Selection Sort", marker="s", color="red")
    plt.plot(largo, tiempo_i, label="Insertion Sort", marker=".", color="yellow")
    plt.plot(largo, tiempo_q, label="Quick Sort", marker="x", color="green")

    plt.title("Comparacion de velocidad")
    plt.xlabel("Largo de la lista")
    plt.ylabel("Segundos")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

crear_tabla()