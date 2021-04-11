import requests
import pandas  as pd
import json
import datetime

# Busca la lista de datasets disponibles en resources.json, los carga en un dataframe, corre un loop con la petición get para cada guid
# y guarda cada archivo .json en una carpeta local.

# Parámetros de la url para acceder a las listas de recursos disponibles

auth_key = "A6xbR3TrMZW6ivfxJmAzo5QMGbxLLUYjLPatSzr4"
url_resources = 'http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key={clave}'.format(clave=auth_key)
url_datastream = 'https://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/?auth_key={clave}'.format(clave=auth_key)
url_datasets = 'http://api.datosabiertos.enacom.gob.ar/api/v2/datasets.json/?auth_key={clave}'.format(clave=auth_key)

# http://api.datosabiertos.enacom.gob.ar/api/v2/visualizations/
# http://api.datosabiertos.enacom.gob.ar/api/v2/sources/
# http://api.datosabiertos.enacom.gob.ar/api/v2/dashboards/
# http://api.datosabiertos.enacom.gob.ar/api/v2/tags/
# http://api.datosabiertos.enacom.gob.ar/api/v2/categories/
# http://api.datosabiertos.enacom.gob.ar/api/v2/stats/
# http://api.datosabiertos.enacom.gob.ar/api/v2/account/resources/
# http://api.datosabiertos.enacom.gob.ar/api/v2/account/children/
# http://api.datosabiertos.enacom.gob.ar/api/v2/iot/


#headers = {"User-Agent": "Mozilla/5.0"}
#respuesta_res = requests.get(url_resources, headers=headers).text  # sin .text te da la respuesta pero no ves el texto

# Creo los dataframes con los recursos disponibles en cada categoría

df_resources = pd.read_json(url_resources)
df_dstream = pd.read_json(url_datastream)
df_dsets = pd.read_json(url_datasets)


# Le agrego año, mes y día a los dataframes para podes manipular los reportes

df_resources['year'] = pd.DatetimeIndex(df_resources['modified_at']).year
df_resources['yearmonth'] = pd.DatetimeIndex(df_resources['modified_at']).year * 100 + pd.DatetimeIndex(df_resources['modified_at']).month
df_resources['yearmonthday'] = pd.DatetimeIndex(df_resources['modified_at']).year * 10000 + pd.DatetimeIndex(df_resources['modified_at']).month * 100 + pd.DatetimeIndex(df_resources['modified_at']).day

df_dstream['year'] = pd.DatetimeIndex(df_dstream['modified_at']).year
df_dstream['yearmonth'] = pd.DatetimeIndex(df_dstream['modified_at']).year * 100 + pd.DatetimeIndex(df_dstream['modified_at']).month
df_dstream['yearmonthday'] = pd.DatetimeIndex(df_dstream['modified_at']).year * 10000 + pd.DatetimeIndex(df_dstream['modified_at']).month * 100 + pd.DatetimeIndex(df_dstream['modified_at']).day

df_dsets['year'] = pd.DatetimeIndex(df_dsets['modified_at']).year
df_dsets['yearmonth'] = pd.DatetimeIndex(df_dsets['modified_at']).year * 100 + pd.DatetimeIndex(df_dsets['modified_at']).month
df_dsets['yearmonthday'] = pd.DatetimeIndex(df_dsets['modified_at']).year * 10000 + pd.DatetimeIndex(df_dsets['modified_at']).month * 100 + pd.DatetimeIndex(df_dsets['modified_at']).day


# path para descargar archivos csv a una carpeta local

Current_Date_Formatted = datetime.datetime.today().strftime ('%Y%m%d')

csv_path_resouces = r'C:/Users/agus3/Desktop/Python/Enacom/Json/resources' + '_' + Current_Date_Formatted + '.csv'
csv_path_dstream = r'C:/Users/agus3/Desktop/Python/Enacom/Json/datastreams' + '_' + Current_Date_Formatted + '.csv'
csv_path_dsets = r'C:/Users/agus3/Desktop/Python/Enacom/Json/datasets' + '_' + Current_Date_Formatted + '.csv'
csv_path_dsets_cant = r'C:/Users/agus3/Desktop/Python/Enacom/Json/datasets_cant' + '_' + Current_Date_Formatted + '.csv'

# Creo los reportes para contar la cantidad de actualizados por mes

df_dsets_cant = df_dsets.groupby(['yearmonth'],sort=True)['yearmonth'].count()
#df_dsets_cant2 = df_dsets.value_counts(subset=['yearmonth'])

# Ejecuto el export de los csv

df_resources.to_csv(csv_path_resouces)
df_dstream.to_csv(csv_path_dstream)
df_dsets.to_csv(csv_path_dsets)
df_dsets_cant.to_csv(csv_path_dsets_cant)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Recorro el dataframe resources para tomar los guid y descargar los archivos json en una carpeta local

guid_list = df_resources['guid'].tolist()

i = 0

for i in range(len(guid_list)):
    url_bucle = 'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/{guid}/data.json/?auth_key={clave}'.format(
        guid=guid_list[i], clave=auth_key)

    headers = {"User-Agent": "Mozilla/5.0"}
    respuesta_ds = requests.get(url_bucle, headers=headers).json()
    archivo = guid_list[i] + '.json'
    path = r'C:/Users/agus3/Desktop/Python/Enacom/Json/' + archivo
    with open(path, 'w') as f:
        json.dump(respuesta_ds, f)
