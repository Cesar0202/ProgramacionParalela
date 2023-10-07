import time
import subprocess

def medir_tiempo(script_nombre):
    start_time = time.time()
    subprocess.call(['python', script_nombre])
    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    return tiempo_ejecucion

tiempo_hilos = medir_tiempo('hilos.py')
tiempo_datos = medir_tiempo('datos.py')
tiempo_tareas = medir_tiempo('tareas.py')

print(f'Tiempo de ejecución de hilos.py: {tiempo_hilos} segundos')
print(f'Tiempo de ejecución de datos.py: {tiempo_datos} segundos')
print(f'Tiempo de ejecución de tareas.py: {tiempo_tareas} segundos')