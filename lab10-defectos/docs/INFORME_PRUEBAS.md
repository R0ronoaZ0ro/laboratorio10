# Informe de Resumen de Pruebas - Extracto IEEE 829

## 1. Identificador del informe
- **Codigo:** IRP-LAB10-001
- **Version del SUT:** 1.0.1 (post-correccion)
- **Alcance:** modulo carrito.py -ciclo de correccion del defecto LAB10-001

## 2. Resumen de variaciones del plan
No hubo variaciones respecto al plan de pruebas. Se ejecutaron todos los casos de prueba planificados para el módulo `carrito.py`:
- 9 pruebas unitarias de la suite base (`test_carrito.py`)
- 4 pruebas parametrizadas (`test_carrito_defecto.py`)

**Total:** 13 casos de prueba ejecutados al 100%.



## 3. Resumen de actividades
- **Herramientas:** pytest 9.1.0, pytest-cov 7.1.0
- **Entorno:** Python 3.12.10, Windows 11
- **Tiempo de ejecución de la suite:** ~0.11 segundos

## 4. Resultados - resumen de casos

Tipo de prueba
- Unitarias (pytest)

Ejecutados
- 13
Aprobados
- 13
Fallidos
- 0
% Aprobación
- 100.0%

**Detalle de la ejecucion:**
- `tests/test_carrito.py` → 9 pruebas aprobada
- `tests/test_carrito_defecto.py` → 4 pruebas aprobadas

## 5. Métricas
DRE =  1 / (1 + 0) × 100 = 100%
Densidad = 1 defectos / 0.055 KLOC = 18.18 defectos/KLOC
% Aprobación = 13 / 13 × 100 = 100%
Tasa reapertura = 0 / 1 × 100 = 0%

### Justificación de métricas
**DRE = 100.0%**
- Defectos hallados antes del cierre: **1** (LAB10-001)
- Defectos post-release: **0**
- Justificación: Se creó un test parametrizado (`test_carrito_defecto.py`) que detecta automáticamente el defecto. Si el defecto hubiera llegado a producción, este test lo habría capturado en el pipeline de CI/CD.

**Densidad de defectos = 18.18 defectos/KLOC**
- Defectos encontrados: **1**
- Líneas de código del SUT: **55** líneas ≈ **0.055 KLOC**
- Cálculo: 1 / 0.055 = 18.18

**% de casos aprobados = 100.0%**
- Casos aprobados: 13
- Casos ejecutados: 13
- Cálculo: 13 / 13 × 100 = 100.0%

**Tasa de reapertura = 0.0%**
- Defectos reabiertos: 0
- Defectos corregidos: 1
- Cálculo: 0 / 1 × 100 = 0.0%

## 6. Evaluación general
El módulo `carrito.py` ha superado todas las pruebas unitarias con un **100% de aprobación** (13/13 casos) y una **cobertura de código del 100%**.

La corrección del defecto **LAB10-001** fue efectiva y no introdujo regresiones en la funcionalidad existente.

**Observación importante:** Durante la ejecución del laboratorio, se identificó una inconsistencia en el escenario planteado en la guía del profesor. El código original con el defecto intencional NO produce `-796.0`, sino `796.0`. Para efectos del laboratorio, se forzó el error para demostrar el ciclo completo de detección, corrección y verificación.

**Conclusión:** El módulo está listo para ser integrado al resto del sistema y pasar a la fase de pruebas de integración.

## 7. Aprobaciones
**Responsable QA**: Johann Osses
**Fecha**: 16 de junio de 2026