import pandas as pd

df = pd.read_csv('Conteo_Agosto_2026.csv', sep=',', encoding='latin-1')

print(df.head())
print(df.columns)
print(df.dtypes)

df_filtrado = df[df['dsc_avenida'] == 'Bv Artigas']
print(df_filtrado)

df_fecha = df[df['fecha'] == '2026-08-01']
print(df_fecha)

df_hora = df[df['volumen_hora'] > 100]
print(df_hora)

promedio_artigas = df_filtrado['volumen_hora'].mean()
print("Promedio de vehículos por hora en Bv Artigas:", promedio_artigas)

cantidad_horas_pico = df_hora.shape[0]
print("Cantidad de registros con más de 100 vehículos:", cantidad_horas_pico)

total_dia = df_fecha['volumen_hora'].sum()
print("Total de vehículos contados el 2026-08-01:", total_dia)