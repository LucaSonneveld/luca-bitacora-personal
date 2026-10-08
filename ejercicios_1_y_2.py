# =============================================================================
# Tránsito y calidad del aire, junio de 2024 — Ejercicios 1 y 2 resueltos
# Versión en Python (pandas + matplotlib)
# =============================================================================
#
# Se puede correr entero (python ejercicios_1_y_2.py) o por bloques: cada
# "# %%" es una celda en VS Code o Spyder.
#
# Paquetes (instalar una sola vez):
#   pip install pandas numpy matplotlib
# =============================================================================

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)   # que no corte columnas al imprimir
pd.set_option("display.width", 140)

RUTA = "clases/clase10/transito_aire_junio2024.csv"

COL_OSCURO = "#5C3A21"
COL_GRIS   = "#BFBFBF"


# =============================================================================
# PREPARACIÓN: la tabla datos (lo mismo que la Parte 2 del script de clase)
# =============================================================================
# %%
aire = pd.read_csv(RUTA)

# El archivo rotula la hora como UTC, pero ya es hora de Montevideo: se lee
# tal cual y se le saca la zona horaria, sin convertirla.
aire["hora"] = pd.to_datetime(aire["hora"])
if aire["hora"].dt.tz is not None:
    aire["hora"] = aire["hora"].dt.tz_localize(None)

datos = aire.copy()
datos["h"] = datos["hora"].dt.hour
datos["dia"] = datos["hora"].dt.date

# dayofweek: lunes = 0 ... domingo = 6, así que el fin de semana es >= 5
datos["tipo_dia"] = np.where(datos["hora"].dt.dayofweek >= 5,
                             "fin de semana", "lunes a viernes")

# pd.cut parte la hora en intervalos y ya devuelve las franjas en orden
datos["franja"] = pd.cut(datos["h"], bins=[-1, 5, 11, 17, 23],
                         labels=["madrugada", "mañana", "tarde", "noche"])

datos["hora_pico"] = np.where(datos["h"].isin([7, 8, 9, 17, 18, 19]),
                              "hora pico", "resto")

# transform("mean") da el promedio de la estación en cada fila, sin reducir filas
datos["transito_rel"] = (datos["transito"]
                         / datos.groupby("estacion")["transito"].transform("mean"))
datos["log_pm25"] = np.log(datos["pm25"])


# =============================================================================
# EJERCICIO 1. FALTANTES
# =============================================================================
# En clase se contó columna por columna con sum(is.na(...)) dentro de
# summarise. Acá se hace al revés: se arma una tabla de verdadero/falso del
# mismo tamaño que datos (isna) y se suma por estación de una sola vez.
# Así entran todas las columnas, sin tener que nombrarlas una por una.
# %%
columnas = ["transito", "no2", "pm25",                        # originales
            "franja", "tipo_dia", "transito_rel", "log_pm25"]  # nuevas

faltantes = (datos[columnas]
             .isna()
             .groupby(datos["estacion"])
             .sum())
faltantes.insert(0, "filas", datos.groupby("estacion").size())
print(faltantes)

# Control extra: isna() no detecta los infinitos. Si algún pm25 valiera 0,
# log(0) daría -inf, que no es un faltante pero tampoco es un número usable.
infinitos = np.isinf(datos[["transito_rel", "log_pm25"]]).sum()
print("\nValores infinitos en las variables nuevas:")
print(infinitos)

# Comprobación automática de lo que se espera
assert (faltantes["log_pm25"] == faltantes["pm25"]).all(), \
    "log_pm25 debería faltar exactamente donde falta pm25"
assert faltantes[["franja", "tipo_dia", "transito_rel"]].sum().sum() == 0, \
    "las variables que salen de la hora o del tránsito no deberían tener faltantes"

# Qué vemos:
#   franja y tipo_dia salen de la hora, que está completa: 0 faltantes.
#   transito_rel sale del tránsito, también completo: 0 faltantes.
#   log_pm25 falta exactamente donde falta pm25 (los mismos números que esa
#   columna, 470 en total), porque el logaritmo de un faltante es un faltante.
#   Como el piso del instrumento es 3, no hay ceros y no aparecen infinitos.


# =============================================================================
# EJERCICIO 2. ¿ESTÁ BIEN DEFINIDA LA HORA PICO?
# =============================================================================
# En la consigna se mira el gráfico y se anotan a ojo las horas mal
# clasificadas. Acá lo hace la tabla: se ordenan las 24 horas por tránsito
# promedio, se toman las 6 más altas (las mismas 6 que tenía hora_pico, para
# que la comparación sea justa) y se comparan con las de la definición vieja.
# %%
lv_tc = datos[(datos["estacion"] == "Tres Cruces")
              & (datos["tipo_dia"] == "lunes a viernes")]

por_hora = lv_tc.groupby("h")["transito"].mean()

horas_pico_viejas = {7, 8, 9, 17, 18, 19}
horas_pico_nuevas = set(por_hora.nlargest(6).index)

print("Tránsito promedio por hora, de mayor a menor:")
print(por_hora.sort_values(ascending=False).round(0).head(10))

print("\nHoras pico según el gráfico:", sorted(horas_pico_nuevas))
print("Estaban como pico y no lo son:", sorted(horas_pico_viejas - horas_pico_nuevas))
print("Son pico y estaban como resto:", sorted(horas_pico_nuevas - horas_pico_viejas))

# ---- 2.2 La variable nueva ---------------------------------------------------
# Se calcula en Tres Cruces de lunes a viernes, pero se aplica a toda la tabla
# por la hora del día (igual que hora_pico, que tampoco distingue estación).
datos["pico_observado"] = np.where(datos["h"].isin(horas_pico_nuevas),
                                   "hora pico", "resto")
print(datos["pico_observado"].value_counts())

# ---- 2.3 El gráfico con la variable nueva ------------------------------------
# En vez de colorear por una columna, cada barra recibe su color según la
# variable nueva, y las horas que cambiaron de grupo llevan borde punteado.
# %%
colores = [COL_OSCURO if h in horas_pico_nuevas else COL_GRIS for h in por_hora.index]
cambiaron = horas_pico_nuevas ^ horas_pico_viejas      # diferencia simétrica

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.bar(por_hora.index, por_hora.values, color=colores)
for h, barra in zip(por_hora.index, barras):
    if h in cambiaron:
        barra.set_edgecolor("black")
        barra.set_linestyle("--")
        barra.set_linewidth(1.5)

ax.set_xticks(range(24))
ax.set_title("Tránsito promedio por hora del día, Tres Cruces, lunes a viernes\n"
             "Oscuro: hora pico observada. Borde punteado: cambió de grupo.")
ax.set_xlabel("Hora del día")
ax.set_ylabel("Vehículos por hora")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.show()

# Qué vemos: las horas pico observadas son 8, 9, 12, 15, 16 y 17. Estaban mal
#   clasificadas 7, 18 y 19 (marcadas como pico y no lo son) y 12, 15 y 16
#   (pico y marcadas como resto). La de más tránsito es las 17.
# Ojo: de 9 a 17 el tránsito es bastante parejo (las 12 y las 13 difieren en
#   500 vehículos), así que el corte en "las 6 más altas" es algo arbitrario.
