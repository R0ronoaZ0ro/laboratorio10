# Reporte de Defecto - LAB10-001 


## TAREA 1: Reporte de Defecto


 ## ID y Título 
LAB10-001: aplicar_descuento() permite total negativo al combinar precio rebajado con cupón > 50% 
 
## Pasos para reproducir 
1. Importar las funciones de carrito.py from src.carrito import agregar_al_carrito, calcular_total, aplicar_descuento 
2. Crear un carrito de compras vacío: `carrito = []`
3. Agregar un producto con precio rebajado:
   - Nombre: "Audífonos"
   - Precio: 1990 (precio original $3.980 con 50% off)
   - Cantidad: 1
4. Calcular el total del carrito usando `calcular_total(carrito)`
5. Aplicar un descuento del 60% usando `aplicar_descuento(total, 60)`
## Resultado esperado 
El total con descuento debería ser un valor positivo o cero, ya que no es posible tener un total negativo en un carrito de compras.

Cálculo esperado:
- Total del carrito: 1990
- Descuento del 60%: 1990 × 0.60 = 1194
- Total con descuento: 1990 - 1194 = 796.0
 
## Resultado obtenido del documento
Se obtiene un total negativo: -796.0
En la funcion de aplicar_descuento si se le modifica total - (total * porcentaje / 100) por -(total - (total * porcentaje / 100)) se podria replicar lo del negativo
## Resultado obtenido Real
Se obtiene un total positivo: 796.0

## Severidad y Prioridad 
**Severidad ALTA** 
- Justificación: El defecto permite que el sistema genere un estado inconsistente (un total de carrito negativo), lo que podría propagarse a otros módulos como pagos o facturación, afectando la lógica de negocio central y la integridad de los datos financieros.

**Prioridad: Alta**
- Justificación: Un total negativo es un error crítico que impacta directamente la experiencia del usuario y la confiabilidad del sistema. Podría generar transacciones incorrectas y afectar la reputación del negocio. Debe ser corregido antes de cualquier release.

## Entorno
- Python: 3.12.10
- pytest: 9.1.0
- pytest-cov: 7.1.0
- Sistema Operativo: Windows 11
- Editor: VS Code


## Evidencia Real
(.venv) PS J:\GithubProjects\laboratorio10\lab10-defectos> python
Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> from src.carrito import agregar_al_carrito, calcular_total, aplicar_descuento      
>>>
>>> carrito = []
>>> agregar_al_carrito(carrito, {'nombre': 'Audífonos', 'precio': 1990, 'cantidad': 1})

[{'nombre': 'Audífonos', 'precio': 1990, 'cantidad': 1}]
>>> total = calcular_total(carrito)
>>> total_con_cupon = aplicar_descuento(total, 60)
>>> print(total_con_cupon)
796.0

## Evidencia 2: Codigo modificado para forzar el error
#Version para simular el error que el profesor espera
    """ if porcentaje < 0 or porcentaje > 100:
        raise ValueError('El porcentaje debe estar entre 0 y 100.')
    # FORZAR EL ERROR: devuelve negativo
    return -(total - (total * porcentaje / 100)) """

>>> from src.carrito import agregar_al_carrito, calcular_total, aplicar_descuento
>>> carrito = []
>>> agregar_al_carrito(carrito, {'nombre': 'Audífonos', 'precio': 1990, 'cantidad': 1})
[{'nombre': 'Audífonos', 'precio': 1990, 'cantidad': 1}]
>>> total = calcular_total(carrito)
>>> total_con_cupon = aplicar_descuento(total, 60)
>>> print(total_con_cupon)
-796.0


## Análisis del escenario propuesto por el profesor:
El código proporcionado en src/carrito.py con el defecto intencional NO produce un valor negativo.
Cálculo real:
- Total del carrito: 1990
- Descuento del 60%: 1990 × 0.60 = 1194
- Total con descuento: 1990 - 1194 = 796.0

Conclusión: El escenario planteado en la guía NO reproduce el defecto que el profesor describe.
El código con el defecto intencional NO genera -796.0, sino 796.0.

## -------------------------------------------------------------------------
## TAREA 2: Prueba de Verificacion Automatizada

Codigo de la prueba parametrizada

- Archivo: tests/test_carrito_defecto.py

# tests/test_carrito_defecto.py
import pytest
from src.carrito import aplicar_descuento

@pytest.mark.parametrize('total,porcentaje,esperado_minimo', [
    (1990, 60, 0),   # rebajado + cupón 60% → negativo según el profesor
    (500, 80, 0),    # caso límite
    (1000, 100, 0),  # descuento total
    (2000, 50, 0),   # 50% exacto → frontera
])
def test_descuento_no_genera_total_negativo(total, porcentaje, esperado_minimo):
    resultado = aplicar_descuento(total, porcentaje)
    assert resultado >= esperado_minimo, (
        f'Total con descuento {porcentaje}% sobre {total} fue {resultado}, '
        f'se esperaba >= {esperado_minimo}'
    )

## Ejecucion de la prueba (fallando con el error forzado)

(.venv) PS J:\GithubProjects\laboratorio10\lab10-defectos> python -m pytest tests/test_carrito_defecto.py -v
=============================================================== test session starts ================================================================
platform win32 -- Python 3.12.10, pytest-9.1.0, pluggy-1.6.0 -- J:\GithubProjects\laboratorio10\lab10-defectos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: J:\GithubProjects\laboratorio10\lab10-defectos
configfile: pytest.ini
plugins: cov-7.1.0
collected 4 items                                                                                                                                    

tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[1990-60-0] FAILED                                                      [ 25%]
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[500-80-0] FAILED                                                       [ 50%] 
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[1000-100-0] PASSED                                                     [ 75%] 
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[2000-50-0] FAILED                                                      [100%] 

===================================================================== FAILURES ===================================================================== 
________________________________________________ test_descuento_no_genera_total_negativo[1990-60-0] ________________________________________________ 

total = 1990, porcentaje = 60, esperado_minimo = 0

    @pytest.mark.parametrize('total,porcentaje,esperado_minimo', [
        (1990, 60, 0),   # rebajado + cupón 60% → negativo según el profesor
        (500, 80, 0),    # caso límite
        (1000, 100, 0),  # descuento total
        (2000, 50, 0),   # 50% exacto → frontera
    ])
    def test_descuento_no_genera_total_negativo(total, porcentaje, esperado_minimo):
        resultado = aplicar_descuento(total, porcentaje)
>       assert resultado >= esperado_minimo, (
            f'Total con descuento {porcentaje}% sobre {total} fue {resultado}, '
            f'se esperaba >= {esperado_minimo}'
        )
E       AssertionError: Total con descuento 60% sobre 1990 fue -796.0, se esperaba >= 0
E       assert -796.0 >= 0

tests\test_carrito_defecto.py:13: AssertionError
________________________________________________ test_descuento_no_genera_total_negativo[500-80-0] _________________________________________________ 

total = 500, porcentaje = 80, esperado_minimo = 0

    @pytest.mark.parametrize('total,porcentaje,esperado_minimo', [
        (1990, 60, 0),   # rebajado + cupón 60% → negativo según el profesor
        (500, 80, 0),    # caso límite
        (1000, 100, 0),  # descuento total
        (2000, 50, 0),   # 50% exacto → frontera
    ])
    def test_descuento_no_genera_total_negativo(total, porcentaje, esperado_minimo):
        resultado = aplicar_descuento(total, porcentaje)
>       assert resultado >= esperado_minimo, (
            f'Total con descuento {porcentaje}% sobre {total} fue {resultado}, '
            f'se esperaba >= {esperado_minimo}'
        )
E       AssertionError: Total con descuento 80% sobre 500 fue -100.0, se esperaba >= 0
E       assert -100.0 >= 0

tests\test_carrito_defecto.py:13: AssertionError
________________________________________________ test_descuento_no_genera_total_negativo[2000-50-0] ________________________________________________ 

total = 2000, porcentaje = 50, esperado_minimo = 0

    @pytest.mark.parametrize('total,porcentaje,esperado_minimo', [
        (1990, 60, 0),   # rebajado + cupón 60% → negativo según el profesor
        (500, 80, 0),    # caso límite
        (1000, 100, 0),  # descuento total
        (2000, 50, 0),   # 50% exacto → frontera
    ])
    def test_descuento_no_genera_total_negativo(total, porcentaje, esperado_minimo):
        resultado = aplicar_descuento(total, porcentaje)
>       assert resultado >= esperado_minimo, (
            f'Total con descuento {porcentaje}% sobre {total} fue {resultado}, '
            f'se esperaba >= {esperado_minimo}'
        )
E       AssertionError: Total con descuento 50% sobre 2000 fue -1000.0, se esperaba >= 0
E       assert -1000.0 >= 0

tests\test_carrito_defecto.py:13: AssertionError
============================================================= short test summary info ============================================================== 
FAILED tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[1990-60-0] - AssertionError: Total con descuento 60% sobre 1990 fue -796.0, se esperaba >= 0
FAILED tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[500-80-0] - AssertionError: Total con descuento 80% sobre 500 fue -100.0, se esperaba >= 0
FAILED tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[2000-50-0] - AssertionError: Total con descuento 50% sobre 2000 fue -1000.0, se esperaba >= 0
=========================================================== 3 failed, 1 passed in 0.12s ============================================================ 

## -------------------------------------------------------------------------
## TAREA 3: Correccion del Defecto y Analisis de Causa Raiz
Análisis de Causa Raíz (RCA)
¿Qué condición no está siendo validada en aplicar_descuento()?

- La funcion no valida que el resultado de la operación total - (total * porcentaje / 100) sea un numero no negativo. Asume que total siempre sera lo grande como para que el descuento no lo lleve a un valor negativo.

¿Por qué el porcentaje > 100 ya está validado pero no es suficiente?

- La validacion porcentaje > 100 solo controla la entrada, el defecto ocurre cuando porcentaje es valido (ej: 60), pero el total sobre el que se aplica ya es un valor pequeño, lo que provoca que el resultado del calculo sea negativo y la funcion necesita validar la salida, no solo la entrada.

¿Qué cambio mínimo en la función resolvería el defecto?

- Despues de calcular el descuento se debe verificar si el resultado es negativo en caso de que lo sea retornar 0.0, esto garantiza que el total nunca sea negativo sin romper los tests existentes.

Codigo corregido
Archivo: src/carrito.py

#esta es la version correcta que devuelve el total positivo
    """Aplica un porcentaje de descuento sobre el total."""
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError('El porcentaje debe estar entre 0 y 100.')
    
    total_con_descuento = total - (total * porcentaje / 100)
    
    # CORRECCION: Asegurar que el total no sea negativo
    if total_con_descuento < 0:
        return 0.0
    
    return total_con_descuento

Verificacion de la correccion

(.venv) PS J:\GithubProjects\laboratorio10\lab10-defectos> python -m pytest tests/ -v --cov=src --cov-report=term-missing
=============================================================== test session starts ================================================================
platform win32 -- Python 3.12.10, pytest-9.1.0, pluggy-1.6.0 -- J:\GithubProjects\laboratorio10\lab10-defectos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: J:\GithubProjects\laboratorio10\lab10-defectos
configfile: pytest.ini
plugins: cov-7.1.0
collected 13 items

tests/test_carrito.py::test_agregar_producto_valido PASSED                                                                                    [  7%] 
tests/test_carrito.py::test_agregar_precio_negativo_lanza_error PASSED                                                                        [ 15%] 
tests/test_carrito.py::test_agregar_cantidad_cero_lanza_error PASSED                                                                          [ 23%] 
tests/test_carrito.py::test_calcular_total_multiples_productos PASSED                                                                         [ 30%] 
tests/test_carrito.py::test_calcular_total_carrito_vacio PASSED                                                                               [ 38%] 
tests/test_carrito.py::test_descuento_estandar PASSED                                                                                         [ 46%] 
tests/test_carrito.py::test_descuento_cero PASSED                                                                                             [ 53%] 
tests/test_carrito.py::test_descuento_total_100 PASSED                                                                                        [ 61%] 
tests/test_carrito.py::test_porcentaje_invalido_lanza_error PASSED                                                                            [ 69%] 
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[1990-60-0] PASSED                                                      [ 76%]
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[500-80-0] PASSED                                                       [ 84%] 
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[1000-100-0] PASSED                                                     [ 92%] 
tests/test_carrito_defecto.py::test_descuento_no_genera_total_negativo[2000-50-0] PASSED                                                      [100%] 

================================================================== tests coverage ================================================================== 
_________________________________________________ coverage: platform win32, python 3.12.10-final-0 _________________________________________________ 

Name             Stmts   Miss  Cover   Missing
----------------------------------------------
src\carrito.py      19      1    95%   59
----------------------------------------------
TOTAL               19      1    95%
================================================================ 13 passed in 0.09s ================================================================


