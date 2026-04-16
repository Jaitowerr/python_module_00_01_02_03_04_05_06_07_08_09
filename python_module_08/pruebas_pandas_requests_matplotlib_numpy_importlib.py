#! /usr/bin/env python3

'''
								POETRY
instalar poetry
	curl -sSL https://install.python-poetry.org | python3 -
Comprobar:
	poetry --version
Luego añade Poetry al PATH para que lo encuentre tu terminal:
	bashexport PATH="$HOME/.local/bin:$PATH"
Y para que sea permanente (que no se pierda al cerrar terminal):
	bashecho 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
	source ~/.zshrc

						pip vs Poetry
pip es el instalador básico de Python. Instala paquetes pero no gestiona conflictos entre versiones automáticamente. El requirements.txt es simplemente una lista.
Poetry es una herramienta más avanzada que:

	Gestiona dependencias y resuelve conflictos automáticamente
	Crea su propio entorno virtual solo
	Usa pyproject.toml que es más moderno y estándar

'''

'''
								PANDAS

Es una librería para manipular datos en tablas. Piensa en ella como Excel pero en Python.
'''

import pandas as pd

# Crea una tabla de datos
df = pd.DataFrame({
    "nombre": ["Neo", "Trinity", "Morpheus"],
    "edad": [28, 27, 45]
})

print(df)
#     nombre  edad
# 0      Neo    28
# 1  Trinity    27
# 2  Morpheus   45
print('\n')

'''
								NUMPY

Es una librería para cálculos matemáticos con arrays y matrices. Muy rápida porque está optimizada en C por debajo.

'''

import numpy as np

# Genera 5 números aleatorios entre 0 y 100
datos = np.random.randint(0, 100, 5)
print(datos)  # [23 67 12 89 45]

print(datos.mean())  # media
print(datos.max())   # máximo
print('\n')


# Generar 1000 datos aleatorios entre 0 y 100
data = np.random.randint(0, 100, 1000)

print(f"Datos generados: {len(data)} puntos")
print(f"Primeros 10: {data[:10]}")
print(f"Media: {data.mean():.2f}")
print(f"Máximo: {data.max()}")
print(f"Mínimo: {data.min()}")
print(f"Desviación estándar: {data.std():.2f}")

print()


'''
								REQUESTS

Es una librería para hacer peticiones HTTP de forma sencilla. 
Permite conectarse a APIs externas y obtener datos reales desde internet.
'''

import requests

# Hace una petición GET a una API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(response.status_code)  # 200 = OK
print(response.json())       # datos en formato diccionario


print()

'''
								MATPLOTLIB

Es una librería para hacer gráficas. Toma datos y genera imágenes.
'''

import matplotlib.pyplot as plt

datos = [1, 4, 9, 16, 25]
plt.plot(datos)
plt.savefig("grafica.png")  # guarda la imagen

'''
Para que esto funcione:
# Crea y activa un venv limpio
	python3 -m venv matrix_env
	source matrix_env/bin/activate

# Instala versiones compatibles
		pip install numpy pandas matplotlib

El venv aísla todo del sistema y evita exactamente estos conflictos 🙂
'''






