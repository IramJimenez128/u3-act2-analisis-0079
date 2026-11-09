#Importar librerias
import pandas as pd
import numpy as np
#Iram Jimenez NC = 0079
print(" ---- Analisis de datos ---- Iram Jimenez NC = 0079")
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Diesel", "Diesel", "Hibrido", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}
df = pd.DataFrame(vehiculos)
print(df)
print(" -+-+-+-+-+-+ Agrupar por una sola columnna Tipo_Motor +-+-+-+-+-+-+-")
agrupado = df.groupby('Tipo_Motor')
print(agrupado)
print(" -+-+-+-+-+-+ Promedio de km por automovil +-+-+-+-+-+-+-")
# Promedio de km por automovil
print(agrupado['Autonomia_Km'].mean())
print(" -+-+-+-+-+-+ Precio en dolares maximo de cada automovil +-+-+-+-+-+-+-")
# Precio en dolares maximo de cada automovil
print(agrupado['Precio_USD'].max())

print("-+-+-+Iram-+-+-+-+-+ Segunda parte -+-+-+-+-0079+-+-+-+-+")
print("Agregaciones multiples")
print("Mean --> Promedio, sum --> suma, max --> Maximo, min --> Minimo")
# Multiples funciones de agregado
resultado_agregado = agrupado['Autonomia_Km'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al Data Frame")
print("Columna Teams --> Equipo")
# Crear nueva columna
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Tipo_Motor', 'Equipo'])['Autonomia_Km'].mean()
print(agrupado_multiple)