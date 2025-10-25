# PROYECTO_LOGICA_Katas_de_Python
Este proyecto consiste en la resolución de una serie de katas en Python orientadas a practicar la lógica de programación y afianzar conocimientos básicos de Python. Se incluyen ejercicios sobre tipos de datos, estructuras, condicionales, iteraciones, funciones, programación orientada a objetos, uso de módulos estándar y buenas prácticas.


## Objetivo del proyecto
Resolver una colección de katas de Python para demostrar dominio de:
- Tipos de datos y funciones incorporadas.  
- Estructuras de datos y sus métodos.  
- Condicionales e iteraciones.  
- Funciones.  
- POO (Clases).  
- Uso de módulos/librerías del temario.  
- Buenas prácticas (nombres claros, docstrings, type hints, manejo de errores, pruebas básicas).  

## Estructura del proyecto

- `katas.py` - Módulo con las funciones de las katas (sin código ejecutable)
- `PROYECTO LÓGICA Katas de Python.py` - Archivo original con ejemplos y código ejecutable
- `test_katas.py` - Tests unitarios con pytest
- `requirements.txt` - Dependencias del proyecto
- `.gitignore` - Archivos a ignorar en git

## Cómo ejecutar
```bash
# 1) (Opcional) crear entorno virtual  
python -m venv .venv  
source .venv/bin/activate # Windows: .venv\Scripts\activate  

# 2) Instalar dependencias
pip install -r requirements.txt  

# 3) Ejecutar el archivo con ejemplos de uso
python "PROYECTO LÓGICA Katas de Python.py"  

# 4) Ejecutar las funciones desde el módulo
python -c "import katas; print(katas.factorial(5))"

# 5) Correr pruebas
pytest -v
```


## Buenas prácticas usadas

- Docstrings (PEP 257) y type hints (PEP 484).  
- Nombrado descriptivo, funciones puras cuando procede.  
- Uso de map, filter, reduce y lambda cuando aporta valor.  
- Manejo explícito de excepciones y creación de excepción personalizada.  
- Casos de uso al final de katas.py bajo if __name__ == "__main__":.  
- Comentarios breves en los pasos más complejos.
- Tests unitarios con pytest.
- Separación de código ejecutable y funciones reutilizables.


## Lista de katas incluidas

Cada enunciado va como comentario justo encima de la función/ejercicio en el archivo original.  

1. Frecuencias de letras (sin espacios)  
2. Doblar cada número con map  
3. Filtrar palabras que contengan un objetivo  
4. Diferencia elemento a elemento de dos listas con map  
5. Media y aprobado/suspenso (tupla)  
6. Factorial recursivo  
7. Convertir lista de tuplas en lista de strings con map  
8. División con manejo de excepciones (input del usuario)  
9. Filtrar mascotas prohibidas en España con filter  
10. Excepción personalizada si lista vacía al calcular promedio  
11. Validación robusta de edad (0–120) con excepciones  
12. Longitud por palabra con map  
13. Lista de tuplas (mayúscula, minúscula) sin repetidos  
14. Empiezan por letra específica con filter  
15. lambda que suma 3 a cada número  
16. Palabras más largas que n con filter  
17. De dígitos a número con reduce  
18. Lista de dicts de estudiantes y filter por calificación ≥ 90  
19. lambda que filtra impares  
20. Filtrar int de una lista mixta  
21. Cubo con lambda  
22. Producto total con reduce  
23. Concatenar palabras con reduce  
24. Diferencia total con reduce  
25. Contar caracteres de una cadena  
26. lambda resto (mod) de dos números  
27. Promedio de números  
28. Primer duplicado en una lista  
29. Enmascarar cadena con # salvo últimos cuatro  
30. ¿Son anagramas?  
31. Buscar nombre en lista (input + excepción si no está)  
32. Buscar nombre completo en empleados (devuelve puesto o mensaje)  
33. lambda suma elemento a elemento de dos listas  
34. Clase Arbol con métodos solicitados  
35. Clase UsuarioBanco con operaciones y validaciones  
36. procesar_texto (contar, reemplazar, eliminar) llamando a subfunciones  
37. Día/tarde/noche según hora ingresada  
38. Calificación en texto según nota numérica  
39. Área de figura (rectángulo/círculo/triángulo)  
40. Descuento con cupón (condicionales)  

