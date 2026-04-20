#! /usr/bin/env python3

# ============================================================
# PRUEBAS - Programación Funcional en Python (Módulo 10)
# ============================================================
# Temas: lambdas, higher-order functions, closures, functools, decoradores
# Cada sección tiene un caso simple y uno más complejo
# ============================================================


# ============================================================
# 1. LAMBDAS - Funciones anónimas
# ============================================================
print("=" * 50)
print("1. LAMBDAS")
print("=" * 50)

# --- Simple ---
# Una lambda que multiplica por 2
doble = lambda x: x * 2
print("Simple - doble(5):", doble(5))
# Salida: Simple - doble(5): 10

# --- Complejo ---
# Una lambda con varios parámetros usada para ordenar una lista de diccionarios
magos = [
    {"nombre": "Alex", "nivel": 5},
    {"nombre": "Jordan", "nivel": 2},
    {"nombre": "Riley", "nivel": 8},
]
magos_ordenados = sorted(magos, key=lambda mago: mago["nivel"])
print("Complejo - magos ordenados por nivel:")
for mago in magos_ordenados:
    print(f"  {mago['nombre']}: nivel {mago['nivel']}")
# Salida:
#   Jordan: nivel 2
#   Alex: nivel 5
#   Riley: nivel 8


# ============================================================
# 2. HIGHER-ORDER FUNCTIONS - map, filter, reduce
# ============================================================
print("\n" + "=" * 50)
print("2. HIGHER-ORDER FUNCTIONS (map, filter)")
print("=" * 50)

hechizos = [10, 25, 3, 47, 8, 30]

# --- Simple con map ---
# map aplica una función a CADA elemento de la lista
# Devuelve un map object, hay que convertirlo a lista
hechizos_dobles = list(map(lambda x: x * 2, hechizos))
print("map - hechizos dobles:", hechizos_dobles)
# Salida: map - hechizos dobles: [20, 50, 6, 94, 16, 60]

# --- Simple con filter ---
# filter devuelve solo los elementos donde la función devuelve True
hechizos_potentes = list(filter(lambda x: x > 20, hechizos))
print("filter - hechizos > 20:", hechizos_potentes)
# Salida: filter - hechizos > 20: [25, 47, 30]

# --- Complejo: combinar map y filter ---
# Primero filtramos los mayores de 10, luego los elevamos al cuadrado
resultado = list(map(lambda x: x ** 2, filter(lambda x: x > 10, hechizos)))
print("Complejo - (mayores de 10) al cuadrado:", resultado)
# Salida: Complejo - (mayores de 10) al cuadrado: [625, 2209, 900]


# ============================================================
# 3. CLOSURES - Funciones que recuerdan su entorno
# ============================================================
print("\n" + "=" * 50)
print("3. CLOSURES")
print("=" * 50)

# --- Simple ---
# La función interior recuerda la variable 'base' aunque
# la función exterior ya haya terminado de ejecutarse
def crear_multiplicador(base):
    def multiplicar(x):
        return x * base      # 'base' viene del entorno exterior, se "recuerda"
    return multiplicar       # devolvemos la función, no la llamamos

por_tres = crear_multiplicador(3)
por_diez = crear_multiplicador(10)

print("Simple - por_tres(7):", por_tres(7))    # 7 * 3 = 21
print("Simple - por_diez(4):", por_diez(4))    # 4 * 10 = 40
# Salida:
# Simple - por_tres(7): 21
# Simple - por_diez(4): 40

# --- Complejo ---
# Un contador que recuerda cuántas veces ha sido llamado
# (usa lista para poder modificar el valor — los closures no pueden
#  reasignar variables externas directamente sin 'nonlocal')
def crear_contador(nombre_mago):
    count = [0]     # truco: usamos lista para poder modificar el valor
    def contar():
        count[0] += 1
        return f"{nombre_mago} ha lanzado {count[0]} hechizo(s)"
    return contar

hechizos_alex = crear_contador("Alex")
hechizos_jordan = crear_contador("Jordan")

print("Complejo -", hechizos_alex())
print("Complejo -", hechizos_alex())
print("Complejo -", hechizos_jordan())
print("Complejo -", hechizos_alex())
# Salida:
# Complejo - Alex ha lanzado 1 hechizo(s)
# Complejo - Alex ha lanzado 2 hechizo(s)
# Complejo - Jordan ha lanzado 1 hechizo(s)
# Complejo - Alex ha lanzado 3 hechizo(s)


# ============================================================
# 4. FUNCTOOLS - Herramientas funcionales
# ============================================================
print("\n" + "=" * 50)
print("4. FUNCTOOLS")
print("=" * 50)

from functools import reduce, partial, lru_cache

# --- reduce: aplica una función acumulativamente ---
# reduce(f, [a, b, c, d]) => f(f(f(a, b), c), d)
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda acc, x: acc + x, numeros)
print("reduce - suma de [1,2,3,4,5]:", suma_total)
# Salida: reduce - suma de [1,2,3,4,5]: 15

# --- partial: "congela" algunos argumentos de una función ---
def potencia(base, exponente):
    return base ** exponente

cuadrado = partial(potencia, exponente=2)   # exponente siempre será 2
cubo = partial(potencia, exponente=3)

print("partial - cuadrado(5):", cuadrado(5))   # 5^2 = 25
print("partial - cubo(3):", cubo(3))           # 3^3 = 27
# Salida:
# partial - cuadrado(5): 25
# partial - cubo(3): 27

# --- lru_cache: guarda resultados de llamadas anteriores (memoización) ---
# Sin cache, calcularía fibonacci desde cero cada vez (muy lento para números grandes)
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("lru_cache - fibonacci(10):", fibonacci(10))
print("lru_cache - fibonacci(30):", fibonacci(30))
# Salida:
# lru_cache - fibonacci(10): 55
# lru_cache - fibonacci(30): 832040


# ============================================================
# 5. DECORADORES - Modificar comportamiento de funciones
# ============================================================
print("\n" + "=" * 50)
print("5. DECORADORES")
print("=" * 50)

# --- Simple ---
# Un decorador que imprime un mensaje antes y después de la función
def anunciar(func):
    def wrapper(*args, **kwargs):       # *args y **kwargs para aceptar cualquier argumento
        print(f"  >> Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"  >> Finalizado: {func.__name__}")
        return resultado
    return wrapper

@anunciar
def lanzar_hechizo(nombre):
    print(f"  ✨ ¡{nombre} lanzado!")

print("Simple - decorador anunciar:")
lanzar_hechizo("Fireball")
# Salida:
#   >> Ejecutando: lanzar_hechizo
#   ✨ ¡Fireball lanzado!
#   >> Finalizado: lanzar_hechizo

# --- Complejo ---
# Un decorador con PARÁMETROS que limita cuántas veces se puede llamar una función
def limite_usos(max_usos):
    def decorador(func):
        usos = [0]
        def wrapper(*args, **kwargs):
            if usos[0] >= max_usos:
                print(f"  ⛔ {func.__name__} ha alcanzado el límite de {max_usos} usos")
                return None
            usos[0] += 1
            print(f"  [Uso {usos[0]}/{max_usos}]")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@limite_usos(3)
def hechizo_raro(nombre_mago):
    print(f"  🔮 {nombre_mago} usa el hechizo raro!")

print("\nComplejo - decorador con parámetros:")
hechizo_raro("Alex")
hechizo_raro("Jordan")
hechizo_raro("Riley")
hechizo_raro("Alex")   # Este ya no puede usarse
# Salida:
#   [Uso 1/3]
#   🔮 Alex usa el hechizo raro!
#   [Uso 2/3]
#   🔮 Jordan usa el hechizo raro!
#   [Uso 3/3]
#   🔮 Riley usa el hechizo raro!
#   ⛔ hechizo_raro ha alcanzado el límite de 3 usos

print("\n" + "=" * 50)
print("FIN DE PRUEBAS")
print("=" * 50)