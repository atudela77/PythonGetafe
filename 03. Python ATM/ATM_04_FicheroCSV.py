print("Inicio de programa")
"""
with open("pruebacsv.csv", 'w') as fichero:
    for _ in range(5):
        valor1 = input()
        valor2 = input()
        valor3 = input()
        fichero.write(f"{valor1},{valor2},{valor3}\n")
"""
with open("pruebacsv.csv") as fichero:
    for linea in fichero:
        
        dato = {"nombre": nombre, "oficio": oficio, "ciudad": ciudad}
        
print("fin de programa")
