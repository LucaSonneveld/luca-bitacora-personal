import pandas as pd
from pathlib import Path

CARPETA = Path(__file__).resolve().parent

ARCHIVO_ENTRADA = CARPETA / "o3_01_2024_04_2024.csv"
ARCHIVO_SALIDA = CARPETA / "o3_limpio.csv"

df = pd.read_csv(ARCHIVO_ENTRADA, encoding="latin1", parse_dates=["fecha"])

pauta_limpieza = {
    "ColÃ³n": "Colón",
    "Curva de MaroÃ±as": "Curva de Maroñas",
}
df["estacion"] = df["estacion"].replace(pauta_limpieza)

df_limpio = df.dropna(subset=["o3"]).copy()
df_limpio = df_limpio.drop_duplicates()

df_limpio["anio"] = df_limpio["fecha"].dt.year
df_limpio["mes"] = df_limpio["fecha"].dt.month
df_limpio["dia"] = df_limpio["fecha"].dt.day
df_limpio["hora"] = df_limpio["fecha"].dt.hour

df_limpio.to_csv(ARCHIVO_SALIDA, index=False, encoding="utf-8")
print(f"Listo: {len(df_limpio):,} filas guardadas en {ARCHIVO_SALIDA}")
import matplotlib.pyplot as plt

ozono_mes = (
    df_limpio.groupby("mes")["o3"]
    .agg(o3_medio_mes="mean", n_registros_mes="size")
    .reset_index()
)
print(ozono_mes)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ozono_mes["mes"], ozono_mes["o3_medio_mes"], color="blue", linewidth=2)
ax.scatter(ozono_mes["mes"], ozono_mes["o3_medio_mes"], color="red", s=60, zorder=3)
ax.set(title="Concentración de Ozono en el ambiente, por mes, 2024",
       xlabel="Mes", ylabel="O3 (µg/m³)")
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
def p95(x):
    return x.quantile(0.95)

ozono_hora = (
    df_limpio
    .groupby(["estacion", pd.Grouper(key="fecha", freq="h")])["o3"]
    .agg(media="mean", maximo="max", p95=p95, n_min="size")
    .reset_index()
    .rename(columns={"fecha": "fecha_hora"})
)
print(ozono_hora.head())

fig, ax = plt.subplots(figsize=(10, 5))
for est, d in ozono_hora.groupby("estacion"):
    ax.plot(d["fecha_hora"], d["media"], linewidth=1, label=est)
ax.set(title="Concentración de Ozono, promedio por hora, 2024",
       xlabel="Fecha", ylabel="O3 (µg/m³)")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()