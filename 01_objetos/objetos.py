import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

# Definición del diccionario
datos_objetos = {
    "objeto": [
        "hexagono",
        "tubito repositorio",
        "juguete peluche",
        "cono",
        "libro",
        "enchufe adaptador",
        "lapicera",
        "cubo rubik",
        "antiparras"
    ],

    "color": [
        "amarillo",
        "transparente",
        "marron",
        "naranja",
        "azul",
        "blanco",
        "azul",
        "multicolor",
        "negro"
    ],

    "material": [
        "plastico",
        "plastico",
        "tela",
        "plastico",
        "papel",
        "plastico",
        "plastico",
        "plastico",
        "plastico"
    ],

    "textura": [
        "liso",
        "liso",
        "suave",
        "liso",
        "liso",
        "liso",
        "liso",
        "liso",
        "liso"
    ],

    "rigidez": [
        "rigido",
        "rigido",
        "blando",
        "rigido",
        "medio",
        "rigido",
        "rigido",
        "rigido",
        "medio"
    ],

    "forma": [
        "hexagonal",
        "cilindrica",
        "irregular",
        "conica",
        "rectangular",
        "rectangular",
        "cilindrica",
        "cubica",
        "irregular"
    ],

    "peso_estimado_g": [
        100,
        30,
        150,
        120,
        300,
        80,
        10,
        90,
        60
    ]
}

df_objetos = pd.DataFrame(datos_objetos)

df_objetos
print(df_objetos
      )
