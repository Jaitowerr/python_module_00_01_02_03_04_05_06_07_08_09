#! /usr/bin/env python3

'''
APUNTES PYDANTIC - Space Env
=============================
BaseModel: clase madre de la que heredan todos los modelos Pydantic.
           Se encarga de validar tipos automáticamente al crear el objeto.
'''

from pydantic import BaseModel


class EstacionPrueba(BaseModel):
    nombre: str
    tripulacion: int


# Creamos un objeto válido
estacion = EstacionPrueba(nombre="Mir", tripulacion=3)
print(estacion)
print(type(estacion))
print()

# ¿Qué pasa si paso un tipo incorrecto?
# estacion_mal = EstacionPrueba(nombre="Mir", tripulacion="no soy un numero")
# print(estacion_mal)


'''
...
Coerción de tipos: Pydantic intenta convertir el valor al tipo esperado.
                   "3" (str) → 3 (int) funciona
                   "hola" (str) → int FALLA
'''

estacion_string = EstacionPrueba(nombre="Mir", tripulacion="3")
print(estacion_string)
print()


'''
...
model_dump(): convierte el objeto Pydantic a diccionario Python normal.
              útil para serializar, guardar o pasar datos a otras funciones.
'''
print(estacion.model_dump())
print(type(estacion.model_dump()))
print()



'''
...
e.errors(): devuelve una lista de diccionarios con el detalle de cada error.
            cada dict tiene: loc (campo), msg (mensaje), type, input (valor recibido)
'''
try:
    estacion_mal = EstacionPrueba(nombre="Mir", tripulacion="no soy un numero")
except Exception as e:
    print(e.errors())
    print()

try:
    estacion_mal = EstacionPrueba(nombre="Mir", tripulacion="no soy un numero")
except Exception as e:
    errores = e.errors()
    print(type(errores))        # tipo de la lista
    print(type(errores[0]))     # tipo del primer elemento
    print(errores[0])           # el elemento en sí
print()














