#! /usr/bin/env python3

# =============================================================================
# APUNTES PYDANTIC - Space Env
# =============================================================================
# Pydantic es una librería de validación de datos para Python.
# Cuando creas un objeto, valida tipos y restricciones automáticamente.
# =============================================================================

import json
from datetime import datetime as dt
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


# =============================================================================
# 1. BASEMODEL — la clase madre de todo modelo Pydantic
# =============================================================================
# Heredar de BaseModel activa la validación automática de tipos.
# No necesitas __init__, Pydantic lo genera solo.
# Métodos más usados:
#   model_dump()         → convierte el objeto a diccionario Python
#   model_dump_json()    → convierte el objeto a string JSON
#   model_validate()     → crea un objeto desde un diccionario
#   model_json_schema()  → devuelve el esquema JSON del modelo
#   model_fields         → diccionario con info de los campos definidos

class EstacionSimple(BaseModel):
    nombre: str
    tripulacion: int


print()
print()

print("=" * 60)
print("1. BASEMODEL BÁSICO")
print("=" * 60)

estacion = EstacionSimple(nombre="Mir", tripulacion=3)

print("Objeto Pydantic:      ", estacion)
print("Tipo del objeto:      ", type(estacion))
print("model_dump():         ", estacion.model_dump())
print("Tipo de model_dump(): ", type(estacion.model_dump()))
print("model_dump_json():    ", estacion.model_dump_json())
print("model_fields:         ", EstacionSimple.model_fields)


# =============================================================================
# 2. COERCIÓN DE TIPOS — Pydantic intenta convertir tipos compatibles
# =============================================================================
# "3" (str) → 3 (int) funciona porque es convertible
# "hola" (str) → int FALLA porque no es convertible

print()
print()
print("=" * 60)
print("2. COERCIÓN DE TIPOS")
print("=" * 60)

estacion_coercion = EstacionSimple(nombre="Mir", tripulacion="3")
print("tripulacion='3' (str) se convierte a int: ",
      estacion_coercion.tripulacion)
print("Tipo resultado:                            ",
      type(estacion_coercion.tripulacion))


# =============================================================================
# 3. VALIDATIONERROR Y e.errors() — capturar errores de validación
# =============================================================================
# Cuando la validación falla, Pydantic lanza ValidationError.
# e.errors() → lista de diccionarios, uno por cada error.
# Cada diccionario tiene:
#   'loc'   → tupla indicando qué campo falló
#   'msg'   → mensaje legible del error
#   'type'  → tipo de error interno de Pydantic
#   'input' → el valor que se intentó asignar

print()
print()
print("=" * 60)
print("3. VALIDATIONERROR Y e.errors()")
print("=" * 60)

try:
    mala = EstacionSimple(nombre="Mir", tripulacion="no soy un numero")
except ValidationError as e:
    print("Lista de errores:     ", e.errors())
    print()
    print("Primer error completo:", e.errors()[0])
    print()
    print("  loc:  ", e.errors()[0]["loc"])
    print("  msg:  ", e.errors()[0]["msg"])
    print("  type: ", e.errors()[0]["type"])
    print("  input:", e.errors()[0]["input"])


# =============================================================================
# 4. FIELD — restricciones sobre los campos
# =============================================================================
# Field(...) → campo OBLIGATORIO (los ... significan "sin valor por defecto")
# Field(default=X) → campo opcional con valor por defecto X
#
# Restricciones para strings:
#   min_length=N  → mínimo N caracteres
#   max_length=N  → máximo N caracteres
#
# Restricciones para números:
#   ge=N  → mayor o igual que N  (greater or equal)
#   le=N  → menor o igual que N  (less or equal)
#   gt=N  → estrictamente mayor  (greater than)
#   lt=N  → estrictamente menor  (less than)
#
# description="texto" → documentación del campo (aparece en el schema JSON)

class EstacionConField(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    nombre: str = Field(..., min_length=1, max_length=50)
    tripulacion: int = Field(..., ge=1, le=20)
    nivel_energia: float = Field(..., ge=0.0, le=100.0)
    es_operacional: bool = True
    notas: Optional[str] = Field(default=None, max_length=200)


print()
print()
print("=" * 60)
print("4. FIELD — restricciones")
print("=" * 60)

# Caso válido
valida = EstacionConField(
    station_id="ISS001",
    nombre="Estacion Internacional",
    tripulacion=6,
    nivel_energia=85.5,
    notas="Todo nominal"
)
print("Estación válida:      ", valida.model_dump())

# Caso inválido: tripulacion > 20
print()
print()
try:
    invalida = EstacionConField(
        station_id="BAD01",
        nombre="Rota",
        tripulacion=999,
        nivel_energia=50.0
    )
except ValidationError as e:
    print("Error tripulacion > 20:")
    print("  msg:", e.errors()[0]["msg"])

# Caso inválido: station_id demasiado corta
print()
print()
try:
    invalida2 = EstacionConField(
        station_id="AB",
        nombre="Corta",
        tripulacion=5,
        nivel_energia=50.0
    )
except ValidationError as e:
    print("Error station_id < 3 chars:")
    print("  msg:", e.errors()[0]["msg"])

# Caso con notas=None (campo Optional)
sin_notas = EstacionConField(
    station_id="SIN01",
    nombre="Sin notas",
    tripulacion=3,
    nivel_energia=50.0
    # ,notas = 'asdadasdasd'
)
print()
print()
print("Campo Optional sin valor: notas =", sin_notas.notas)


# =============================================================================
# 5. DATETIME — Pydantic convierte strings a datetime automáticamente
# =============================================================================
# Si el campo es datetime, Pydantic acepta:
#   - un objeto datetime de Python
#   - un string ISO 8601: "2024-01-15T10:30:00"
#   - un timestamp Unix (int o float)

class EventoEspacial(BaseModel):
    nombre: str
    fecha: datetime


print()
print()
print()
print("=" * 60)
print("5. DATETIME — conversión automática")
print("=" * 60)

# Desde string ISO
evento1 = EventoEspacial(nombre="Lanzamiento", fecha="2024-01-15T10:30:00")
print("String → envento1 → datetime:  ", evento1.fecha)
print("Tipo → envento1:      ", type(evento1.fecha))

# Desde objeto datetime
evento2 = EventoEspacial(nombre="Aterrizaje", fecha=dt(2024, 6, 1, 8, 0, 0))
print("datetime → evento2 → datetime:", evento2.fecha)


# =============================================================================
# 6. model_validate() — crear objeto desde diccionario
# =============================================================================
# Útil cuando recibes datos de una API o un JSON ya parseado.

print()
print()
print("=" * 60)
print("6. model_validate() — desde diccionario")
print("=" * 60)

datos = {
    "station_id": "VAL01",
    "nombre": "Validada",
    "tripulacion": 4,
    "nivel_energia": 90.0
}

desde_dict = EstacionConField.model_validate(datos)
print("Creada desde dict:", desde_dict.model_dump())


# =============================================================================
# 7. model_json_schema() — esquema JSON del modelo
# =============================================================================
# Devuelve un diccionario que describe la estructura del modelo.
# Muy útil para documentar APIs automáticamente.

print()
print()
print("=" * 60)
print("7. model_json_schema()")
print("=" * 60)

schema = EstacionConField.model_json_schema()
print(json.dumps(schema, indent=2))
