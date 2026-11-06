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