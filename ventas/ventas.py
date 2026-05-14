import csv 
import sys

#lee el archivo csv y devuelve una lista de diccionarios (cada uno de un libro)
def leer_ventas (nombre_archivo):
    ventas = []
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
            lector = csv.DictReader(file) # crea un diccionario tomando los elementos de la primera fila en claves
            #lee cada fila del archivo
            for fila in lector:
                venta = {
                        'titulo': fila['titulo'],
                        'genero': fila['genero'],
                        'precio': float(fila['precio']),
                        'cantidad': int(fila['cantidad'])
                    }

                ventas.append(venta)
    
    except FileNotFoundError:
        sys.exit()
    
    
    return ventas

#calcula los ingresos totales por genero
def ingresos_por_genero(ventas):
    ingresos = {}
    
    #recorre las ventas
    for venta in ventas:
        genero = venta["genero"]
        
        #calcula los ingresos x venta
        ingreso = venta["precio"] * venta["cantidad"]
        
        # si el genero ya existe suma el ingreso
        if genero in ingresos.keys():
            ingresos[genero] += ingreso
        
        # si no existe crea la clave 
        else:
            ingresos[genero] = ingreso
        
    return ingresos

# obtiene los ingresos y genera un informe
def generar_informe(nombre_archivo):
    ventas= leer_ventas(nombre_archivo)
    ingresos = ingresos_por_genero(ventas)
    
    #calcula el total de ingresos
    total= (sum(ingresos.values()))
    
    print("Ingresos por genero:")
    for genero, ingreso in ingresos.items():
        print(f"* {genero}: ${ingreso}")
    
    print(f"\nTotal: ${total}")

archivo = sys.argv[1]
generar_informe(nombre_archivo="ventas.csv")