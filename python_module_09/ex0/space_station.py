#! /usr/bin/env python3

from pydantic import BaseModel

'''
BaseModel
Field(...) → para añadir restricciones (mínimo, máximo, longitud...)
Optional → para campos que pueden ser None
datetime → tipo de Python para fechas y horas

model.model_dump() → convierte tu objeto a diccionario
e.errors() → cuando falla la validación, te da los errores detallados
'''
class MiModelo(BaseModel):
    nombre: str
    edad: int
    


if __name__ == '__main__':
    pass