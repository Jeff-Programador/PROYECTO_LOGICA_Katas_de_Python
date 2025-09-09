
# # PROYECTO LÓGICA: Katas de Python

from __future__ import annotations
from functools import reduce
from typing import Dict, List, Tuple, Iterable, Any, Optional
from math import pi

#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(texto: str) -> dict:
    """
    Recibe una cadena y devuelve un diccionario con la frecuencia de cada letra.
    Los espacios no se cuentan.
    """
    conteo = {}
    for letra in texto:
        if letra == " ":   # ignoramos espacios
            continue
        # sumamos 1 si ya estaba, o la inicializamos en 1
        conteo[letra] = conteo.get(letra, 0) + 1
    return conteo


# Ejemplo de uso
print(frecuencias_letras("hola hola"))
# Salida: {'h': 2, 'o': 2, 'l': 2, 'a': 2}


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doblar_lista(numeros: list) -> list:
    """
    Recibe una lista de números y devuelve una nueva lista
    con el doble de cada valor usando map().
    """
    return list(map(lambda x: x * 2, numeros))


# Ejemplo de uso
print(doblar_lista([1, 2, 3, 4]))
# Salida: [2, 4, 6, 8]


 
#  3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


def contiene_objetivo(palabras: list, objetivo: str) -> list:
    """
    Recibe una lista de palabras y una palabra objetivo.
    Devuelve una lista con todas las palabras de la lista original
    que contengan la palabra objetivo dentro de ellas.
    """
    return [p for p in palabras if objetivo in p]


# Ejemplo de uso
lista = ["gato", "perro", "ratón", "gatito", "lagarto"]
print(contiene_objetivo(lista, "gato"))
# Salida: ['gato']


 
#  4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()


def diferencia_listas(lista1: list, lista2: list) -> list:
    """
    Recibe dos listas numéricas y devuelve una nueva lista
    con la diferencia elemento a elemento (lista1 - lista2).
    Si las listas tienen distinta longitud, se recorta a la más corta.
    """
    return list(map(lambda x, y: x - y, lista1, lista2))


# Ejemplo de uso
a = [10, 20, 30]
b = [1, 2, 3]
print(diferencia_listas(a, b))
# Salida: [9, 18, 27]


 
#  5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.


def media_y_estado(notas: list, nota_aprobado: float = 5.0) -> tuple:
    """
    Recibe una lista de números (notas) y un valor opcional nota_aprobado (por defecto 5).
    Devuelve una tupla con la media de las notas y el estado ("aprobado" o "suspenso").
    """
    if not notas:  # comprobamos que la lista no esté vacía
        raise ValueError("La lista de notas está vacía")

    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# Ejemplo de uso
print(media_y_estado([4, 6, 8]))
# Salida: (6.0, 'aprobado')

print(media_y_estado([2, 3, 4], nota_aprobado=5))
# Salida: (3.0, 'suspenso')


 
#  6. Escribe una función que calcule el factorial de un número de manera recursiva


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número de manera recursiva.
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n in (0, 1):  # caso base
        return 1
    return n * factorial(n - 1)  # llamada recursiva


# Ejemplo de uso
print(factorial(5))  # 120
print(factorial(0))  # 1


 
#  7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()


def tuplas_a_strings(pares: list) -> list:
    """
    Convierte una lista de tuplas en una lista de strings.
    Cada tupla se transforma en el formato 'clave:valor'.
    """
    return list(map(lambda t: f"{t[0]}:{t[1]}", pares))


# Ejemplo de uso
datos = [("a", 1), ("b", 2), ("c", 3)]
print(tuplas_a_strings(datos))
# Salida: ['a:1', 'b:2', 'c:3']


 
#  8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


def dividir_seguro():
    """
    Pide dos números al usuario e intenta dividirlos.
    Maneja errores si la entrada no es numérica o si se divide por cero.
    """
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        resultado = a / b  # aquí puede saltar ZeroDivisionError
    except ValueError:
        print("❌ Error: Debes introducir números válidos.")
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir entre cero.")
    else:
        print(f"✅ División exitosa. Resultado: {resultado}")


# Ejemplo de uso
dividir_seguro()


 
#  9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


def filtrar_mascotas_permitidas(mascotas: list) -> list:
    """
    Recibe una lista de nombres de mascotas y devuelve una nueva lista
    excluyendo las prohibidas en España.
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))


# Ejemplo de uso
lista = ["Perro", "Gato", "Mapache", "Tigre", "Canario"]
print(filtrar_mascotas_permitidas(lista))
# Salida: ['Perro', 'Gato', 'Canario']


 
#  10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


# Definimos una excepción personalizada
class ListaVaciaError(Exception):
    """Excepción lanzada cuando la lista está vacía."""
    pass


def promedio_seguro(numeros: list) -> float:
    """
    Recibe una lista de números y devuelve su promedio.
    Si la lista está vacía, lanza ListaVaciaError.
    """
    if not numeros:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    return sum(numeros) / len(numeros)


# Ejemplo de uso con manejo de error
try:
    print(promedio_seguro([2, 4, 6]))  # Promedio normal
    print(promedio_seguro([]))         # Provoca excepción
except ListaVaciaError as e:
    print(f"❌ Error capturado: {e}")


 
#  11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# 


def pedir_edad():
    """
    Pide al usuario que introduzca su edad.
    Maneja errores si la entrada no es numérica o si está fuera del rango 0–120.
    """
    try:
        entrada = input("Introduce tu edad: ")
        edad = int(entrada)  # aquí puede fallar si no es numérico
        if not (0 <= edad <= 120):
            raise ValueError("Edad fuera del rango permitido (0–120).")
    except ValueError:
        print("❌ Error: Debes introducir un número válido entre 0 y 120.")
    else:
        print(f"✅ Edad registrada correctamente: {edad} años")


# Ejemplo de uso
pedir_edad()


 
#  12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()


def longitudes_palabras():
    """
    Pide al usuario una frase y devuelve una lista con la longitud de cada palabra.
    Usa la función map().
    """
    frase = input("Introduce una frase: ")
    return list(map(len, frase.split()))


# Ejemplo de uso
print(longitudes_palabras())


 
#  13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()


def pares_mayus_minus():
    """
    Pide al usuario un conjunto de caracteres y devuelve
    una lista de tuplas con cada letra en (MAYÚSCULA, minúscula).
    No se repiten letras.
    Usa la función map().
    """
    entrada = input("Introduce un conjunto de caracteres: ")
    unicos = sorted(set(entrada))  # eliminamos repetidos y ordenamos
    return list(map(lambda c: (c.upper(), c.lower()), unicos))


# Ejemplo de uso
print(pares_mayus_minus())


 
#  14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()


def palabras_por_letra():
    """
    Pide al usuario una lista de palabras (separadas por espacios) y una letra.
    Devuelve las palabras que comiencen con esa letra usando filter().
    """
    palabras = input("Introduce una lista de palabras separadas por espacios: ").split()
    letra = input("Introduce la letra por la que deben empezar: ")

    return list(filter(lambda p: p.startswith(letra), palabras))


# Ejemplo de uso
print(palabras_por_letra())


 
#  15. Crea una función lambda que sume 3 a cada número de una lista dada.


# Función lambda que recibe una lista y devuelve otra lista con +3 en cada número
sumar_tres = lambda numeros: list(map(lambda x: x + 3, numeros))

# Ejemplo de uso
print(sumar_tres([1, 2, 3, 4]))
# Salida: [4, 5, 6, 7]


 
#  16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()


def palabras_mas_largas(frase: str, n: int) -> list:
    """
    Recibe una cadena de texto y un número entero n.
    Devuelve una lista con las palabras de la frase que tienen longitud > n.
    Usa filter().
    """
    return list(filter(lambda palabra: len(palabra) > n, frase.split()))


# Ejemplo de uso
print(palabras_mas_largas("Hola a todos en la clase de Python", 3))
# Salida: ['Hola', 'todos', 'clase', 'Python']


 
#  17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()


def lista_a_numero(digitos: list) -> int:
    """
    Recibe una lista de dígitos y devuelve el número correspondiente.
    Usa reduce() para combinar los dígitos.
    Ejemplo: [5,7,2] -> 572
    """
    return reduce(lambda acc, d: acc * 10 + d, digitos, 0)


# Ejemplo de uso
print(lista_a_numero([5, 7, 2]))  # 572
print(lista_a_numero([1, 2, 3, 4]))  # 1234


 
#  18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()


def filtrar_mejores_estudiantes():
    """
    Crea una lista de diccionarios con estudiantes (nombre, edad, calificación)
    y devuelve solo los que tienen calificación >= 90 usando filter().
    """
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 21, "calificacion": 85},
        {"nombre": "María", "edad": 19, "calificacion": 90},
        {"nombre": "Pedro", "edad": 22, "calificacion": 70}
    ]

    mejores = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))
    return mejores


# Ejemplo de uso
print(filtrar_mejores_estudiantes())


 
#  19. Crea una función lambda que filtre los números impares de una lista dada.
# 


# Función lambda que filtra los números impares de una lista
filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 != 0, numeros))

# Ejemplo de uso
print(filtrar_impares([1, 2, 3, 4, 5, 6, 7]))
# Salida: [1, 3, 5, 7]


 
#  20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()


def solo_enteros(lista: list) -> list:
    """
    Recibe una lista con enteros y cadenas.
    Devuelve una nueva lista solo con los valores int.
    Usa filter().
    """
    return list(filter(lambda x: isinstance(x, int), lista))


# Ejemplo de uso
datos = [1, "dos", 3, "cuatro", 5, "6", 7]
print(solo_enteros(datos))
# Salida: [1, 3, 5, 7]


 
#  21. Crea una función que calcule el cubo de un número dado mediante una función lambda


# Función lambda que calcula el cubo de un número
cubo = lambda x: x ** 3

# Ejemplo de uso
print(cubo(2))   # 8
print(cubo(5))   # 125


 
#  22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .


def producto_lista(numeros: list) -> int:
    """
    Recibe una lista de números y devuelve el producto total de sus valores.
    Usa reduce().
    """
    return reduce(lambda x, y: x * y, numeros, 1)


# Ejemplo de uso
print(producto_lista([2, 3, 4]))   # 24
print(producto_lista([5, 10]))     # 50
print(producto_lista([]))          # 1 (producto vacío)


 
#  23. Concatena una lista de palabras.Usa la función reduce() .
# 


def concatenar_palabras(palabras: list) -> str:
    """
    Recibe una lista de palabras y devuelve una cadena
    con todas ellas concatenadas.
    Usa reduce().
    """
    return reduce(lambda a, b: a + b, palabras, "")


# Ejemplo de uso
print(concatenar_palabras(["Hola", " ", "mundo", "!"]))
# Salida: Hola mundo!


 
#  24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .


def diferencia_total(numeros: list) -> int:
    """
    Calcula la diferencia total de los valores de una lista
    usando reduce(). La operación es: a1 - a2 - a3 - ...
    Si la lista está vacía, devuelve 0.
    """
    if not numeros:
        return 0
    return reduce(lambda x, y: x - y, numeros)


# Ejemplo de uso
print(diferencia_total([10, 2, 3]))   # 10 - 2 - 3 = 5
print(diferencia_total([50, 20, 5]))  # 50 - 20 - 5 = 25
print(diferencia_total([]))           # 0


 
#  25. Crea una función que cuente el número de caracteres en una cadena de texto dada


def contar_caracteres(texto: str) -> int:
    """
    Recibe una cadena de texto y devuelve el número de caracteres que contiene.
    """
    return len(texto)


# Ejemplo de uso
print(contar_caracteres("Hola mundo estamos usando python"))   # 32 (sin contar el espacio son 9)
print(contar_caracteres(""))             # 0


 
#  26. Crea una función lambda que calcule el resto de la división entre dos números dados


# Función lambda que calcula el resto (módulo) de la división
resto = lambda a, b: a % b

# Ejemplo de uso
print(resto(10, 4))   # 2
print(resto(25, 4))   # 1
print(resto(19, 5))    # 4


 
#  27. Crea una función que calcule el promedio de una lista de números.
# 


from typing import Optional

def promedio(numeros: list) -> Optional[float]:
    """
    Recibe una lista de números y devuelve su promedio (media aritmética).
    Si la lista está vacía, devuelve None.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)


# Ejemplo de uso
print(promedio([2, 4, 6, 8]))   # 5.0
print(promedio([10, 20]))       # 15.0
print(promedio([]))             # None



# Ejemplo de uso
print(promedio([2, 4, 6, 8]))   # 5.0
print(promedio([10, 20]))       # 15.0
print(promedio([]))             # None


 
#  28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# 


def primer_duplicado(lista: list):
    """
    Recibe una lista y devuelve el primer elemento duplicado que encuentre.
    Si no hay duplicados, devuelve None.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# Ejemplo de uso
print(primer_duplicado([1, 2, 3, 2, 5, 6]))   # 2
print(primer_duplicado([10, 20, 30, 40]))     # None


 
#  29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.


def enmascarar(variable) -> str:
    """
    Convierte una variable en cadena de texto y enmascara todos los caracteres
    con '#' excepto los últimos cuatro.
    """
    texto = str(variable)  # convertimos a string
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


# Ejemplo de uso
print(enmascarar(123456789))    # ##6789
print(enmascarar("contraseña")) # ##eña
print(enmascarar("1234"))       # 1234


 
#  30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


def son_anagramas(palabra1: str, palabra2: str) -> bool:
    """
    Determina si dos palabras son anagramas.
    Ignora mayúsculas, minúsculas y espacios.
    """
    # Normalizamos: todo en minúsculas y sin espacios
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    # Son anagramas si las letras ordenadas coinciden
    return sorted(p1) == sorted(p2)


# Ejemplo de uso
print(son_anagramas("Roma", "Amor"))      # True
print(son_anagramas("Riesgo", "Sergio"))  # True
print(son_anagramas("Hola", "Adiós"))     # False


 
#  31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción


def buscar_nombre():
    """
    Pide al usuario una lista de nombres y luego un nombre para buscar.
    Si el nombre está en la lista, lo indica. Si no, lanza una excepción.
    """
    try:
        nombres = input("Introduce una lista de nombres separados por espacios: ").split()
        nombre_buscar = input("Introduce el nombre que quieres buscar: ")

        if nombre_buscar in nombres:
            print(f"✅ El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"❌ El nombre '{nombre_buscar}' no está en la lista.")
    except ValueError as e:
        print(e)


# Ejemplo de uso
buscar_nombre()


 
#  32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


def puesto_empleado(nombre_completo: str, empleados: list) -> str:
    """
    Recibe un nombre completo y una lista de empleados en formato [(nombre, puesto), ...].
    Devuelve el puesto si el nombre está en la lista, de lo contrario un mensaje de error.
    """
    for nombre, puesto in empleados:
        if nombre == nombre_completo:
            return puesto
    return f"❌ La persona '{nombre_completo}' no trabaja aquí."


# Ejemplo de uso
empleados = [
    ("Ana Pérez", "Desarrolladora"),
    ("Luis Gómez", "Diseñador"),
    ("Marta López", "Gerente")
]

print(puesto_empleado("Luis Gómez", empleados))   # Diseñador
print(puesto_empleado("Pedro Ruiz", empleados))   # ❌ La persona 'Pedro Ruiz' no trabaja aquí.


 
#  33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.


# Función lambda que suma elementos correspondientes de dos listas
suma_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo de uso
print(suma_listas([1, 2, 3], [4, 5, 6]))
# Salida: [5, 7, 9]


 
#  34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# 
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método
# 
# info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# 
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol. """


class Arbol:
    """
    Árbol con:
      - tronco: longitud entera (inicia en 1)
      - ramas: lista de longitudes (cada rama inicia en 1)
    Métodos:
      - crecer_tronco()
      - nueva_rama()
      - crecer_ramas()
      - quitar_rama(pos)
      - info_arbol() -> dict
    """
    def __init__(self):
        self.tronco = 1              # 1) tronco inicia en 1
        self.ramas = []              #    sin ramas inicialmente

    def crecer_tronco(self):
        # 2) aumenta tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # 3) agrega una rama nueva de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4) aumenta en 1 cada rama existente
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, pos: int):
        """
        5) elimina la rama en la posición 'pos' (índice 0-based).
        Si en tu enunciado 'posición 2' significa la segunda rama,
        entonces pos=1.
        """
        if not (0 <= pos < len(self.ramas)):
            raise IndexError("Posición de rama inválida")
        self.ramas.pop(pos)

    def info_arbol(self) -> dict:
        # 6) devuelve información del árbol
        return {
            "tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes_ramas": list(self.ramas)
        }


# Caso de uso (pasos 1–7)
if __name__ == "__main__":
    arbol = Arbol()           # 1. Crear un árbol.
    arbol.crecer_tronco()     # 2. Crecer tronco +1  -> tronco = 2
    arbol.nueva_rama()        # 3. Añadir nueva rama -> ramas = [1]
    arbol.crecer_ramas()      # 4. Crecen ramas +1   -> ramas = [2]
    arbol.nueva_rama()        # 5. Añadir nueva rama -> ramas = [2, 1]
    arbol.nueva_rama()        #    Añadir otra rama  -> ramas = [2, 1, 1]
    arbol.quitar_rama(1)      # 6. Retirar rama en posición 2 (índice 1) -> ramas = [2, 1]
    print(arbol.info_arbol()) # 7. Obtener info
    # Salida ejemplo: {'tronco': 2, 'num_ramas': 2, 'longitudes_ramas': [2, 1]}


 
#  36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# 
# Código a seguir:
# 
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. PROYECTO LÓGICA: Katas de Python 3
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".
# 


class UsuarioBanco:
    """
    Representa a un usuario de banco con:
      - nombre (str)
      - saldo (float)
      - tiene_cc (bool) -> indica si tiene cuenta corriente
    Métodos:
      - retirar_dinero(cantidad)
      - transferir_dinero(origen, cantidad)
      - agregar_dinero(cantidad)
    """
    def __init__(self, nombre: str, saldo: float, tiene_cc: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cc = tiene_cc

    def retirar_dinero(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad

    def transferir_dinero(self, origen: "UsuarioBanco", cantidad: float):
        if not self.tiene_cc or not origen.tiene_cc:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if origen.saldo < cantidad:
            raise ValueError(f"{origen.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        origen.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad

    def __str__(self):
        return f"{self.nombre} → Saldo: {self.saldo}"


# Caso de uso
if __name__ == "__main__":
    # 1. Crear usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # 2. Agregar 20 unidades a Bob
    bob.agregar_dinero(20)  # Bob = 70
  
    
    # 3. Transferir 70 unidades desde Bob a Alicia (máximo permitido)
    alicia.transferir_dinero(bob, 70)
   

    # 4. Retirar 50 unidades de Alicia
    alicia.retirar_dinero(50)

    # Mostrar resultados
    print(alicia)  # Alicia → Saldo: 120
    print(bob)     # Bob → Saldo: 0


 
#  37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# 
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# 
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto


def contar_palabras(texto: str) -> dict:
    """
    Cuenta cuántas veces aparece cada palabra en el texto.
    Devuelve un diccionario {palabra: cantidad}.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
    """
    Reemplaza todas las ocurrencias de palabra_original por palabra_nueva.
    """
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto: str, palabra: str) -> str:
    """
    Elimina todas las ocurrencias de una palabra del texto.
    """
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto: str, opcion: str, *args):
    """
    Procesa el texto según la opción especificada:
    - "contar": devuelve un diccionario con la frecuencia de palabras
    - "reemplazar": requiere palabra_original y palabra_nueva
    - "eliminar": requiere palabra a eliminar
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Debes proporcionar palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Debes proporcionar la palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


# Caso de uso
texto = "hola mundo hola python mundo"

print("👉 Opción contar:")
print(procesar_texto(texto, "contar"))
# {'hola': 2, 'mundo': 2, 'python': 1}

print("\n👉 Opción reemplazar:")
print(procesar_texto(texto, "reemplazar", "mundo", "universo"))
# "hola universo hola python universo"

print("\n👉 Opción eliminar:")
print(procesar_texto(texto, "eliminar", "hola"))
# "mundo python mundo"


 
#  38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


def momento_del_dia():
    """
    Pide una hora al usuario (0-23) y devuelve si es de día, tarde o noche.
    """
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if not (0 <= hora <= 23):
            raise ValueError("La hora debe estar entre 0 y 23.")
        
        if 6 <= hora < 12:
            print("☀️ Es de día (mañana).")
        elif 12 <= hora < 20:
            print("🌇 Es la tarde.")
        else:
            print("🌙 Es de noche.")
    except ValueError as e:
        print(f"❌ Error: {e}")


# Ejemplo de uso
momento_del_dia()


 
#  39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente


def calificacion_texto():
    """
    Pide una calificación numérica (0-100) al usuario
    y devuelve la calificación en texto:
    - 0 - 69: insuficiente
    - 70 - 79: bien
    - 80 - 89: muy bien
    - 90 - 100: excelente
    """
    try:
        nota = int(input("Introduce la calificación del alumno (0-100): "))
        if not (0 <= nota <= 100):
            raise ValueError("La nota debe estar entre 0 y 100.")
        
        if nota <= 69:
            print("❌ Insuficiente")
        elif nota <= 79:
            print("✔️ Bien")
        elif nota <= 89:
            print("👍 Muy bien")
        else:
            print("🌟 Excelente")
    except ValueError as e:
        print(f"❌ Error: {e}")


# Ejemplo de uso
calificacion_texto()


 
#  40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).


import math

def area_figura(figura: str, datos: tuple) -> float:
    """
    Calcula el área de una figura geométrica.
    - figura puede ser: "rectangulo", "circulo" o "triangulo".
    - datos es una tupla con los valores necesarios:
        * rectangulo -> (base, altura)
        * circulo    -> (radio,)
        * triangulo  -> (base, altura)
    """
    figura = figura.lower()

    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'.")


# Ejemplos de uso
print("Área rectángulo 3x4:", area_figura("rectangulo", (3, 4)))  # 12
print("Área círculo radio 2:", area_figura("circulo", (2,)))     # ~12.566
print("Área triángulo base 6 altura 3:", area_figura("triangulo", (6, 3)))  # 9


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.


def calcular_precio_final():
    """
    Calcula el monto final de una compra aplicando un cupón de descuento si es válido.
    """
    try:
        # 1. Precio original
        precio = float(input("Introduce el precio original del artículo: "))
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        # 2. Preguntar si tiene cupón
        respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # 3. Si tiene cupón, pedir valor
        if respuesta in ("sí", "si", "s"):
            valor_cupon = float(input("Introduce el valor del cupón: "))
            if valor_cupon > 0:
                if valor_cupon >= precio:
                    print("🎉 El cupón cubre todo el precio, el artículo es GRATIS.")
                else:
                    precio_final = precio - valor_cupon
                    print(f"✅ Precio final con descuento: {precio_final:.2f} €")
            else:
                print("❌ El cupón no es válido. Precio sin descuento.")
                print(f"Precio final: {precio:.2f} €")
        elif respuesta in ("no", "n"):
            print(f"Precio final (sin descuento): {precio:.2f} €")
        else:
            print("❌ Respuesta no válida. Debes contestar sí o no.")

    except ValueError as e:
        print(f"❌ Error: {e}")


# Ejemplo de uso
calcular_precio_final()



