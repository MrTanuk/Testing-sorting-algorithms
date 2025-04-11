import csv
import time
import numpy as np
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

class SparePart:
    def __init__(self, partId, name, compatibility, price, stock):
        self.partId = partId
        self.name = name
        self.compatibility = compatibility
        self.price = float(price)
        self.stock = int(stock)
        self.entryDate = datetime.now()

    def getPrice(self): return self.price
    def getStock(self): return self.stock
    def getName(self): return self.name
    def getCompatibility(self): return self.compatibility

def loadSpareParts():
    """Load spare parts data from CSV file"""
    spareParts = []
    try:
        with open('spare_parts.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                spareParts.append(SparePart(
                    row['id'],
                    row['name'],
                    row['compatibility'],
                    row['price'],
                    row['stock']
                ))
        return spareParts
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] Ejecute 'python generate_csv.py' primero.")
        exit()

# Sorting Algorithms
def quickSort(arr):
    """QuickSort implementation for price sorting"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.getPrice() < pivot.getPrice()]
    middle = [x for x in arr if x.getPrice() == pivot.getPrice()]
    right = [x for x in arr if x.getPrice() > pivot.getPrice()]
    
    return quickSort(left) + middle + quickSort(right)

def insertionSort(arr):
    """Insertion sort for stock sorting"""
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and arr[j].getStock() > current.getStock():
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

def mergeSort(arr):
    """Merge sort for name sorting"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].getName() < right[j].getName():
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# UI Functions
def showTable(title, data):
    """Display data in a table with Spanish headers"""
    table = Table(title=title)
    table.add_column("ID", style="cyan")
    table.add_column("Nombre", style="magenta")
    table.add_column("Precio", style="green")
    table.add_column("Stock", style="yellow")
    table.add_column("Compatibilidad", style="blue")
    
    for item in data[:10]:
        table.add_row(
            str(item.partId),
            item.name,
            f"${item.price:.2f}",
            str(item.stock),
            item.compatibility
        )
    console.print(table)

def showPerformanceChart(algorithms, times):
    """Display performance comparison chart"""
    # Avoid zero values for sqrt calculation
    times = [max(t, 0.0001) for t in times]
    sqrtTimes = np.sqrt(times)
    maxSqrt = max(sqrtTimes)
    
    console.print("\n[bold]Comparación de Rendimiento[/bold]")
    for algo, t, sqrtT in zip(algorithms, times, sqrtTimes):

        barLength = int((sqrtT / maxSqrt) * 40)
        console.print(f"{algo.ljust(14)} {'█' * barLength} ({t:.5f}s)")
    print("")

def bubbleSort(arr):
    """for compatibility (by vehicle brand)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Extract vehicle make (1st word)
            brand1 = arr[j].getCompatibility().split()[0]
            brand2 = arr[j+1].getCompatibility().split()[0]
            
            if brand1 > brand2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Main Application
def mainMenu():
    """Main application menu"""
    spareParts = loadSpareParts()
    
    while True:
        console.print("\n[bold cyan]=== Gestión de Inventario - CarFix ===[/bold cyan]")
        console.print("1. Ordenar por precio (QuickSort)")
        console.print("2. Ordenar por stock (InsertionSort)")
        console.print("3. Ordenar por nombre (MergeSort)")
        console.print("4. Ordenar por compatibilidad (BubbleSort)")
        console.print("5. Comparar rendimiento")
        console.print("6. Salir")
        option = input("\nSeleccione una opción: ")
        
        if option == "1":
            sortedParts = quickSort(spareParts.copy())
            showTable("Repuestos ordenados por precio", sortedParts)

        elif option == "2":
            sortedParts = insertionSort(spareParts.copy())
            showTable("Repuestos ordenados por stock", sortedParts)

        elif option == "3":
            sortedParts = mergeSort(spareParts.copy())
            showTable("Repuestos ordenados alfabéticamente", sortedParts)

        elif option == "4":
            sortedParts = bubbleSort(spareParts.copy())
            showTable("Repuestos ordenados por compatibilidad (marca)", sortedParts)

        elif option == "5":
            # Performance comparison with 2500 items
            largeData = spareParts * 5
            start = time.time()
            quickSort(largeData.copy())
            qsTime = time.time() - start
            
            start = time.time()
            mergeSort(largeData.copy())
            msTime = time.time() - start
            
            start = time.time()
            insertionSort(largeData.copy())
            insTime = time.time() - start

            start = time.time()
            bubbleSort(largeData.copy())
            bsTime = time.time() - start
            
            showPerformanceChart(
                ["QuickSort", "MergeSort", "InsertionSort", "BubbleSort"],
                [qsTime, msTime, insTime, bsTime]
            )
        elif option == "6":
            break

if __name__ == "__main__":
    mainMenu()
