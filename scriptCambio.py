import pandas as pd
import json

# Cargar el archivo Excel
df = pd.read_excel('D:\\Documentos\\Linea\\Html Bodegas\\bodegas.xlsx')

# Convertir el DataFrame a un diccionario
data_dict = df.to_dict(orient='records')

# Escribir el diccionario en un archivo JSON
with open('D:\\Documentos\\Linea\\Html Bodegas\\datos.json', 'w') as f:
    json.dump(data_dict, f, indent=4)
