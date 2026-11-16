# Ejercicios 58 a 61 · Unir tablas (en papel)

Foto de la hoja: [ejercicios_58_a_61_hoja.jpeg](ejercicios_58_a_61_hoja.jpeg)

## Ejercicio 58 — Completar una unión

Tabla `vuelos` (izquierda) y tabla `aerolineas` (derecha); unión izquierda con clave `carrier`.

**a) Tabla resultado**

| vuelo | carrier | name |
|-------|---------|------|
| 1 | UA | United Air Lines Inc. |
| 2 | AA | American Airlines Inc. |
| 3 | B6 | JetBlue Airways |
| 4 | UA | United Air Lines Inc. |
| 5 | DL | *(faltante)* |

**b) ¿Cuántas filas tendría si la unión fuera interna?**

3 filas.

**c) ¿Qué vuelo se pierde en la unión interna y por qué?**

Se pierde el vuelo 5, ya que no hay dato que indique su aerolínea (DL no está en la tabla
`aerolineas`).
