import requests
import pandas  as pd
import urllib.request
import json


# Busca la lista de datasets disponibles en resources.json, los carga en un dataframe y busca la columna guid,
# para poder construir los get con esos id, después corre un loop con la petición de cada id
# y guarda cada archivo en una carpeta local.

auth_key = "A6xbR3TrMZW6ivfxJmAzo5QMGbxLLUYjLPatSzr4"
url = 'http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key={clave}'.format(clave=auth_key)

headers = {"User-Agent":"Mozilla/5.0"}
respuesta_res = requests.get(url, headers=headers).text # sin .text te da la respuesta pero no ves el texto
print(respuesta_res)
df = pd.read_json(url)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)
guid_list = df['guid'].tolist()
print(guid_list)

i=0

for i in range(len(guid_list)):
    url_bucle = 'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/{guid}/data.json/?auth_key={clave}'.format(guid=guid_list[i],clave=auth_key)
    print()
    print(url_bucle)
    headers = {"User-Agent": "Mozilla/5.0"}
    respuesta_ds = requests.get(url_bucle, headers=headers).json()
    archivo = guid_list[i] + '.json'
    path = r'C:/Users/agus3/Desktop/Python/Enacom/Json/' + archivo
    with open(path, 'w') as f:
        json.dump(respuesta_ds, f)
