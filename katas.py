"""
Módulo con funciones de las katas de Python.
Este archivo contiene solo las definiciones de funciones sin código ejecutable.
"""

from __future__ import annotations
from functools import reduce
from typing import Dict, List, Tuple, Iterable, Any, Optional
from math import pi


def frecuencias_letras(texto: str) -> dict:
    """
    Recibe una cadena y devuelve un diccionario con la frecuencia de cada letra.
    Los espacios no se cuentan.
    """
    conteo = {}
    for letra in texto:
        if letra == " ":
            continue
        conteo[letra] = conteo.get(letra, 0) + 1
    return conteo


def doblar_lista(numeros: list) -> list:
    """
    Recibe una lista de números y devuelve una nueva lista
    con el doble de cada valor usando map().
    """
    return list(map(lambda x: x * 2, numeros))


def contiene_objetivo(palabras: list, objetivo: str) -> list:
    """
    Recibe una lista de palabras y una palabra objetivo.
    Devuelve una lista con todas las palabras de la lista original
    que contengan la palabra objetivo dentro de ellas.
    """
    return [p for p in palabras if objetivo in p]


def diferencia_listas(lista1: list, lista2: list) -> list:
    """
    Recibe dos listas numéricas y devuelve una nueva lista
    con la diferencia elemento a elemento (lista1 - lista2).
    """
    return list(map(lambda x, y: x - y, lista1, lista2))


def media_y_estado(notas: list, nota_aprobado: float = 5.0) -> tuple:
    """
    Recibe una lista de números (notas) y un valor opcional nota_aprobado.
    Devuelve una tupla con la media de las notas y el estado.
    """
    if not notas:
        raise ValueError("La lista de notas está vacía")
    
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número de manera recursiva.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def tuplas_a_strings(pares: list) -> list:
    """
    Convierte una lista de tuplas en una lista de strings.
    Cada tupla se transforma en el formato 'clave:valor'.
    """
    return list(map(lambda t: f"{t[0]}:{t[1]}", pares))


def filtrar_mascotas_permitidas(mascotas: list) -> list:
    """
    Recibe una lista de nombres de mascotas y devuelve una nueva lista
    excluyendo las prohibidas en España.
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))


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


# Lambda que suma 3 a cada número
sumar_tres = lambda numeros: list(map(lambda x: x + 3, numeros))


def palabras_mas_largas(frase: str, n: int) -> list:
    """
    Recibe una cadena de texto y un número entero n.
    Devuelve una lista con las palabras que tienen longitud > n.
    """
    return list(filter(lambda palabra: len(palabra) > n, frase.split()))


def lista_a_numero(digitos: list) -> int:
    """
    Recibe una lista de dígitos y devuelve el número correspondiente.
    Ejemplo: [5,7,2] -> 572
    """
    return reduce(lambda acc, d: acc * 10 + d, digitos, 0)


def filtrar_mejores_estudiantes() -> list:
    """
    Crea una lista de diccionarios con estudiantes
    y devuelve solo los que tienen calificación >= 90.
    """
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 21, "calificacion": 85},
        {"nombre": "María", "edad": 19, "calificacion": 90},
        {"nombre": "Pedro", "edad": 22, "calificacion": 70}
    ]
    
    mejores = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))
    return mejores


# Lambda que filtra los números impares
filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 != 0, numeros))


def solo_enteros(lista: list) -> list:
    """
    Recibe una lista con enteros y cadenas.
    Devuelve una nueva lista solo con los valores int.
    """
    return list(filter(lambda x: isinstance(x, int), lista))


# Lambda que calcula el cubo de un número
cubo = lambda x: x ** 3


def producto_lista(numeros: list) -> int:
    """
    Recibe una lista de números y devuelve el producto total.
    """
    return reduce(lambda x, y: x * y, numeros, 1)


def concatenar_palabras(palabras: list) -> str:
    """
    Recibe una lista de palabras y devuelve una cadena concatenada.
    """
    return reduce(lambda a, b: a + b, palabras, "")


def diferencia_total(numeros: list) -> int:
    """
    Calcula la diferencia total de los valores de una lista.
    """
    if not numeros:
        return 0
    return reduce(lambda x, y: x - y, numeros)


def contar_caracteres(texto: str) -> int:
    """
    Recibe una cadena de texto y devuelve el número de caracteres.
    """
    return len(texto)


# Lambda que calcula el resto (módulo)
resto = lambda a, b: a % b
