#! /usr/bin/env python3
import sys
import os
import site

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


print('=== SYS ===')
print('  - prefix:       ', sys.prefix)
print('  - base_prefix:  ', sys.base_prefix)
print('  - executable:   ', sys.executable)
print('  - version:      ', sys.version)
print('  - path:         ', sys.path)

print()
print('=== OS ===')
print('  - VIRTUAL_ENV:  ', os.environ.get("VIRTUAL_ENV"))
print('  - HOME:         ', os.environ.get("HOME"))
print('  - basename:     ',
      os.path.basename(os.environ.get("VIRTUAL_ENV", "/no/venv")))
print('  - exists venv:  ', os.path.exists(sys.prefix))
print('  - getcwd:       ', os.getcwd())

print()
print('=== SITE ===')
print('  - getsitepackages:     ', site.getsitepackages())
print('  - getusersitepackages: ', site.getusersitepackages())
