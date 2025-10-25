"""
Tests básicos para las katas de Python.
Solo prueba funciones que no requieren input() del usuario.
"""
import pytest
import katas


class TestKata1:
    """Tests para frecuencias_letras"""
    
    def test_frecuencias_basico(self):
        resultado = katas.frecuencias_letras("hola hola")
        assert resultado == {'h': 2, 'o': 2, 'l': 2, 'a': 2}
    
    def test_frecuencias_sin_espacios(self):
        resultado = katas.frecuencias_letras("a b c")
        assert resultado == {'a': 1, 'b': 1, 'c': 1}


class TestKata2:
    """Tests para doblar_lista"""
    
    def test_doblar_lista_basico(self):
        resultado = katas.doblar_lista([1, 2, 3, 4])
        assert resultado == [2, 4, 6, 8]
    
    def test_doblar_lista_vacia(self):
        resultado = katas.doblar_lista([])
        assert resultado == []


class TestKata3:
    """Tests para contiene_objetivo"""
    
    def test_contiene_objetivo_encontrado(self):
        lista = ["gato", "perro", "ratón", "gatito", "lagarto"]
        resultado = katas.contiene_objetivo(lista, "gato")
        # Note: "gato" is not a substring of "gatito" (which is "g-a-t-i-t-o")
        # nor "lagarto" (which is "l-a-g-a-r-t-o"), so only exact "gato" matches
        assert resultado == ["gato"]
    
    def test_contiene_objetivo_no_encontrado(self):
        lista = ["perro", "ratón"]
        resultado = katas.contiene_objetivo(lista, "gato")
        assert resultado == []


class TestKata4:
    """Tests para diferencia_listas"""
    
    def test_diferencia_listas_basico(self):
        
        a = [10, 20, 30]
        b = [1, 2, 3]
        resultado = katas.diferencia_listas(a, b)
        assert resultado == [9, 18, 27]


class TestKata5:
    """Tests para media_y_estado"""
    
    def test_media_aprobado(self):
        
        media, estado = katas.media_y_estado([4, 6, 8])
        assert media == 6.0
        assert estado == "aprobado"
    
    def test_media_suspenso(self):
        
        media, estado = katas.media_y_estado([2, 3, 4], nota_aprobado=5)
        assert media == 3.0
        assert estado == "suspenso"


class TestKata6:
    """Tests para factorial"""
    
    def test_factorial_5(self):
        
        assert katas.factorial(5) == 120
    
    def test_factorial_0(self):
        
        assert katas.factorial(0) == 1


class TestKata7:
    """Tests para tuplas_a_strings"""
    
    def test_tuplas_a_strings_basico(self):
        
        datos = [("a", 1), ("b", 2), ("c", 3)]
        resultado = katas.tuplas_a_strings(datos)
        assert resultado == ['a:1', 'b:2', 'c:3']


class TestKata9:
    """Tests para filtrar_mascotas_permitidas"""
    
    def test_filtrar_mascotas(self):
        
        lista = ["Perro", "Gato", "Mapache", "Tigre", "Canario"]
        resultado = katas.filtrar_mascotas_permitidas(lista)
        assert resultado == ['Perro', 'Gato', 'Canario']


class TestKata10:
    """Tests para promedio_seguro y ListaVaciaError"""
    
    def test_promedio_normal(self):
        
        resultado = katas.promedio_seguro([2, 4, 6])
        assert resultado == 4.0
    
    def test_lista_vacia_error(self):
        
        with pytest.raises(katas.ListaVaciaError):
            katas.promedio_seguro([])


class TestKata15:
    """Tests para lambda sumar_tres"""
    
    def test_sumar_tres(self):
        
        resultado = katas.sumar_tres([1, 2, 3, 4])
        assert resultado == [4, 5, 6, 7]


class TestKata16:
    """Tests para palabras_mas_largas"""
    
    def test_palabras_mas_largas(self):
        
        resultado = katas.palabras_mas_largas("Hola a todos en la clase de Python", 3)
        assert resultado == ['Hola', 'todos', 'clase', 'Python']


class TestKata17:
    """Tests para lista_a_numero"""
    
    def test_lista_a_numero_572(self):
        
        assert katas.lista_a_numero([5, 7, 2]) == 572
    
    def test_lista_a_numero_1234(self):
        
        assert katas.lista_a_numero([1, 2, 3, 4]) == 1234


class TestKata18:
    """Tests para filtrar_mejores_estudiantes"""
    
    def test_filtrar_mejores(self):
        
        resultado = katas.filtrar_mejores_estudiantes()
        assert len(resultado) == 2
        assert resultado[0]["nombre"] == "Ana"
        assert resultado[1]["nombre"] == "María"


class TestKata19:
    """Tests para lambda filtrar_impares"""
    
    def test_filtrar_impares(self):
        
        resultado = katas.filtrar_impares([1, 2, 3, 4, 5, 6, 7])
        assert resultado == [1, 3, 5, 7]


class TestKata20:
    """Tests para solo_enteros"""
    
    def test_solo_enteros(self):
        
        datos = [1, "dos", 3, "cuatro", 5, "6", 7]
        resultado = katas.solo_enteros(datos)
        assert resultado == [1, 3, 5, 7]


class TestKata21:
    """Tests para lambda cubo"""
    
    def test_cubo_2(self):
        
        assert katas.cubo(2) == 8
    
    def test_cubo_5(self):
        
        assert katas.cubo(5) == 125


class TestKata22:
    """Tests para producto_lista"""
    
    def test_producto_lista_234(self):
        
        assert katas.producto_lista([2, 3, 4]) == 24
    
    def test_producto_lista_vacia(self):
        
        assert katas.producto_lista([]) == 1


class TestKata23:
    """Tests para concatenar_palabras"""
    
    def test_concatenar_palabras(self):
        
        resultado = katas.concatenar_palabras(["Hola", " ", "mundo", "!"])
        assert resultado == "Hola mundo!"


class TestKata24:
    """Tests para diferencia_total"""
    
    def test_diferencia_total(self):
        
        assert katas.diferencia_total([10, 2, 3]) == 5
    
    def test_diferencia_total_vacia(self):
        
        assert katas.diferencia_total([]) == 0


class TestKata25:
    """Tests para contar_caracteres"""
    
    def test_contar_caracteres(self):
        
        resultado = katas.contar_caracteres("Hola mundo")
        assert resultado == 10


class TestKata26:
    """Tests para lambda resto"""
    
    def test_resto(self):
        
        assert katas.resto(10, 4) == 2
        assert katas.resto(25, 4) == 1
