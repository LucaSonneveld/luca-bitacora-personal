# ❌ Errores y correcciones

Errores que encontré en mis ejercicios, qué estaba mal y cómo se corrige.

| Ejercicio | Qué puse | Correcto | Archivo |
|-----------|----------|----------|---------|
| [58 b) — Unir tablas](../06_unir-tablas/) | La unión interna tiene **3 filas** | Tiene **4 filas** | [`ej58_union_interna.py`](ej58_union_interna.py) |

## Ejercicio 58 b) — ¿Cuántas filas da la unión interna?

**El error:** conté las filas de la tabla `aerolineas` (UA, AA, B6 = 3) en vez de contar los
vuelos que encuentran pareja.

**La corrección:** en una unión se cuentan las filas de la tabla de vuelos que encuentran su
clave en la otra tabla. Encuentran pareja los vuelos 1 (UA), 2 (AA), 3 (B6) y **4 (UA)**: UA
aparece dos veces y las dos se aparean. Solo se pierde el vuelo 5 (DL). Resultado: **4 filas**.

**Lo que aprendí:** una clave repetida en la tabla izquierda genera una fila por cada repetición.
El tamaño del resultado depende de cuántas filas encuentran pareja, no de cuántas filas tiene la
tabla de la derecha.

El script `ej58_union_interna.py` arma las dos tablas y hace las dos uniones con pandas
(`merge`) para comprobarlo.
