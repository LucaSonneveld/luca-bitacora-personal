# 04 · Ozono 2024 — carga y transformación (clase del 17/09)

- `carga_y_transformacion.py` — lee las mediciones de ozono (enero a abril 2024), corrige los
  nombres de estación mal codificados (Colón, Curva de Maroñas), saca faltantes y duplicados,
  agrega año/mes/día/hora y guarda `o3_limpio.csv`. Después grafica:
  - el O3 medio por mes → `figuras/Concentracion_Ozono_por_Mes.png`
  - el O3 promedio por hora y estación → `figuras/Concentracion_Ozono_PpHora.png`

Necesita `o3_01_2024_04_2024.csv` en esta carpeta.
