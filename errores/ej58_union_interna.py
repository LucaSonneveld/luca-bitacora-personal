# =============================================================================
# Corrección del ejercicio 58 b) — ¿cuántas filas da la unión interna?
# =============================================================================
# En la hoja (06_unir-tablas) respondí "3 filas". La respuesta correcta es 4.
# Este script arma las dos tablas del ejercicio y hace las dos uniones para
# comprobarlo.

import pandas as pd

vuelos = pd.DataFrame({
    "vuelo":     [1, 2, 3, 4, 5],
    "carrier":   ["UA", "AA", "B6", "UA", "DL"],
    "dest":      ["IAH", "MIA", "SJU", "ORD", "ATL"],
    "dep_delay": [2, -4, 33, 0, -6],
})

aerolineas = pd.DataFrame({
    "carrier": ["UA", "AA", "B6"],
    "name":    ["United Air Lines Inc.", "American Airlines Inc.", "JetBlue Airways"],
})

# Unión izquierda: se quedan todos los vuelos; DL no tiene pareja -> name vacío
izquierda = vuelos.merge(aerolineas, on="carrier", how="left")
print("Unión izquierda:", len(izquierda), "filas")
print(izquierda[["vuelo", "carrier", "name"]], "\n")

# Unión interna: solo los vuelos cuya aerolínea está en la tabla aerolineas
interna = vuelos.merge(aerolineas, on="carrier", how="inner")
print("Unión interna:", len(interna), "filas")
print(interna[["vuelo", "carrier", "name"]])

assert len(interna) == 4

# Por qué son 4 y no 3:
#   la tabla aerolineas tiene 3 filas (UA, AA, B6), pero eso no es lo que se
#   cuenta. Se cuentan los VUELOS que encuentran pareja: 1 (UA), 2 (AA),
#   3 (B6) y 4 (UA). UA aparece dos veces en vuelos y las dos encuentran
#   pareja. Solo se pierde el vuelo 5 (DL), que no está en aerolineas.
