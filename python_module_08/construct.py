'''
sys — información sobre el intérprete de Python que está corriendo ahora mismo. 	
	sys.prefix        # ruta del Python activo ahora (venv o sistema)
	sys.base_prefix   # ruta del Python REAL del sistema (siempre /usr)
	sys.executable    # ruta exacta del binario python que está corriendo
	sys.version       # versión de Python como string "3.10.12 ..."
	sys.path          # lista de rutas donde Python busca módulos

os — interactúa con el sistema operativo. Sí, ficheros y carpetas, pero también variables de entorno (que es lo que usamos aquí). Cuando activas un venv, Linux crea una variable de entorno llamada VIRTUAL_ENV con la ruta, y os.environ.get() la lee.
	os.environ.get("VIRTUAL_ENV")  # variable de entorno que crea Linux al activar venv (None si no hay)
	os.environ.get("HOME")         # carpeta home del usuario
	os.path.basename(ruta)         # extrae solo el nombre final de una ruta
	                               # ej: basename("/home/user/venv") → "venv"
	os.path.exists(ruta)           # True/False si existe esa ruta
	os.getcwd()                    # carpeta donde estás ahora mismo

site — módulo específico de Python que sabe dónde se instalan los paquetes. Cuando haces pip install algo, va a la ruta que site conoce.
	site.getsitepackages()         # lista de rutas donde pip instala paquetes
	site.getusersitepackages()     # ruta de paquetes del usuario (sin sudo)

'''

import sys, os, site

print(sys.prefix)
print(sys.base_prefix)
print(sys.executable)
print()
print(os.environ.get("VIRTUAL_ENV"))
print()
print(site.getsitepackages())

if sys.prefix != sys.base_prefix:
	print('entorno visual conectado')
else:
	print('Enorno visual desconectado')
	print(' - Si no está instalado ejecute \'python3 -m venv venv\'\n'
		'  - Para activar ejecue \'source venv/bin/activate \'\n'
		'   - Para desactivar ejecute \'deactivate\'\n')