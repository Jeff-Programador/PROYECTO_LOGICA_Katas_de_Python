# PROYECTO_LOGICA_Katas_de_Python
Este proyecto consiste en la resolución de una serie de katas en Python orientadas a practicar la lógica de programación y afianzar conocimientos básicos de Python. Se incluyen ejercicios sobre tipos de datos, estructuras, condicionales, iteraciones, funciones, programación orientada a objetos, uso de módulos estándar y buenas prácticas.


Objetivo del proyecto
Resolver una colección de katas de Python para demostrar dominio de:
Tipos de datos y funciones incorporadas.  
Estructuras de datos y sus métodos.  
Condicionales e iteraciones.  
Funciones.  
POO (Clases).  
Uso de módulos/librerías del temario.  
Buenas prácticas (nombres claros, docstrings, type hints, manejo de errores, pruebas básicas).  

Cómo ejecutar
# 1) (Opcional) crear entorno virtual  
python -m venv .venv  
source .venv/bin/activate # Windows: .venv\Scripts\activate  

# 2) (Opcional) instalar pytest si usarás tests
pip install -r requirements.txt  

# 3) Ejecutar el archivo con ejemplos de uso
python katas.py  

# 4) (Opcional) correr pruebas
pytest -q  


Buenas prácticas usadas

Docstrings (PEP 257) y type hints (PEP 484).  
Nombrado descriptivo, funciones puras cuando procede.  
Uso de map, filter, reduce y lambda cuando aporta valor.  
Manejo explícito de excepciones y creación de excepción personalizada.  
Casos de uso al final de katas.py bajo if __name__ == "__main__":.  
Comentarios breves en los pasos más complejos.  


# 5) Lista de katas incluidas

Cada enunciado va como comentario justo encima de la función/ejercicio en katas.py.  
Frecuencias de letras (sin espacios)  
Doblar cada número con map  
Filtrar palabras que contengan un objetivo  
Diferencia elemento a elemento de dos listas con map  
Media y aprobado/suspenso (tupla)  
Factorial recursivo  
Convertir lista de tuplas en lista de strings con map  
División con manejo de excepciones (input del usuario)  
Filtrar mascotas prohibidas en España con filter  
Excepción personalizada si lista vacía al calcular promedio  
Validación robusta de edad (0–120) con excepciones  
Longitud por palabra con map  
Lista de tuplas (mayúscula, minúscula) sin repetidos  
Empiezan por letra específica con filter  
lambda que suma 3 a cada número  
Palabras más largas que n con filter  
De dígitos a número con reduce  
Lista de dicts de estudiantes y filter por calificación ≥ 90  
lambda que filtra impares  
Filtrar int de una lista mixta  
Cubo con lambda  
Producto total con reduce  
Concatenar palabras con reduce  
Diferencia total con reduce  
Contar caracteres de una cadena  
lambda resto (mod) de dos números  
Promedio de números  
Primer duplicado en una lista  
Enmascarar cadena con # salvo últimos cuatro  
¿Son anagramas?  
Buscar nombre en lista (input + excepción si no está)  
Buscar nombre completo en empleados (devuelve puesto o mensaje)  
lambda suma elemento a elemento de dos listas  
Clase Arbol con métodos solicitados  
Clase UsuarioBanco con operaciones y validaciones  
procesar_texto (contar, reemplazar, eliminar) llamando a subfunciones  
Día/tarde/noche según hora ingresada  
Calificación en texto según nota numérica  
Área de figura (rectángulo/círculo/triángulo)  
Descuento con cupón (condicionales)  


