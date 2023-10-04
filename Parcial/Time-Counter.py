from timeit import default_timer

#funcion de prueba
def sampleFunction(n):
    return n
    
#Punto 1
inicio_A = default_timer()
sampleFunction(20)
fin_A = default_timer()

print("Tiempo de ejecucion: ")
print(fin_A - inicio_A, "segundos")

#Punto 2
inicio_B = default_timer()
sampleFunction(30)
fin_B = default_timer()

print("Tiempo de ejecucion: ")
print(fin_B - inicio_B, "segundos")

#Punto 3
inicio_C = default_timer()
sampleFunction(40)
fin_C = default_timer()

print("Tiempo de ejecucion: ")
print(fin_C - inicio_C, "segundos")
