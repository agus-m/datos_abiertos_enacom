import pandas  as pd
import datetime

# Busca la lista de recursos disponibles dentro de cada uno de los tipos de recursos citados en la documentación de la API,
# los carga en un dataframe, agrupa por última fecha de modificación y escribe el resultado en un csv

# Parámetros y urls para acceder a las listas de recursos disponibles

auth_key = "xxxxxxxxxxxxxxxxxxxxx"

url_resources = 'http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key={clave}'.format(clave=auth_key)
url_datastream = 'https://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/?auth_key={clave}'.format(clave=auth_key)
url_datasets = 'http://api.datosabiertos.enacom.gob.ar/api/v2/datasets.json/?auth_key={clave}'.format(clave=auth_key)
url_visualizations = 'http://api.datosabiertos.enacom.gob.ar/api/v2/visualizations.json/?auth_key={clave}'.format(clave=auth_key)
url_dashboards = 'http://api.datosabiertos.enacom.gob.ar/api/v2/dashboards.json/?auth_key={clave}'.format(clave=auth_key)

# Estos parecen ser otros tipos de recursos que no están citados en la documentación de la API

# http://api.datosabiertos.enacom.gob.ar/api/v2/sources/
# http://api.datosabiertos.enacom.gob.ar/api/v2/tags/
# http://api.datosabiertos.enacom.gob.ar/api/v2/categories/
# http://api.datosabiertos.enacom.gob.ar/api/v2/stats/
# http://api.datosabiertos.enacom.gob.ar/api/v2/account/resources/
# http://api.datosabiertos.enacom.gob.ar/api/v2/account/children/
# http://api.datosabiertos.enacom.gob.ar/api/v2/iot/


# Creo los dataframes con los recursos disponibles en cada categoría

df_resources = pd.read_json(url_resources)
df_dstream = pd.read_json(url_datastream)
df_dsets = pd.read_json(url_datasets)
df_visualizations = pd.read_json(url_visualizations)
df_dashboards = pd.read_json(url_dashboards)


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

df_visualizations['year'] = pd.DatetimeIndex(df_visualizations['modified_at']).year
df_visualizations['yearmonth'] = pd.DatetimeIndex(df_visualizations['modified_at']).year * 100 + pd.DatetimeIndex(df_visualizations['modified_at']).month
df_visualizations['yearmonthday'] = pd.DatetimeIndex(df_visualizations['modified_at']).year * 10000 + pd.DatetimeIndex(df_visualizations['modified_at']).month * 100 + pd.DatetimeIndex(df_visualizations['modified_at']).day

df_dashboards['year'] = pd.DatetimeIndex(df_dashboards['modified_at']).year
df_dashboards['yearmonth'] = pd.DatetimeIndex(df_dashboards['modified_at']).year * 100 + pd.DatetimeIndex(df_dashboards['modified_at']).month
df_dashboards['yearmonthday'] = pd.DatetimeIndex(df_dashboards['modified_at']).year * 10000 + pd.DatetimeIndex(df_dashboards['modified_at']).month * 100 + pd.DatetimeIndex(df_dashboards['modified_at']).day


# path para descargar archivos csv a una carpeta local

Current_Date_Formatted = datetime.datetime.today().strftime ('%Y%m%d')

csv_path_resouces = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/resources' + '_' + Current_Date_Formatted + '.csv'
csv_path_dstream = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/datastreams' + '_' + Current_Date_Formatted + '.csv'
csv_path_dsets = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/datasets' + '_' + Current_Date_Formatted + '.csv'
csv_path_visualizations = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/visualizations' + '_' + Current_Date_Formatted + '.csv'
csv_path_dashboards = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/dashboards' + '_' + Current_Date_Formatted + '.csv'

csv_path_resouces_cant = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/resources_cant' + '_' + Current_Date_Formatted + '.csv'
csv_path_dstream_cant = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/datastreams_cant' + '_' + Current_Date_Formatted + '.csv'
csv_path_dsets_cant = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/datasets_cant' + '_' + Current_Date_Formatted + '.csv'
csv_path_visualizations_cant = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/visualizations_cant' + '_' + Current_Date_Formatted + '.csv'
csv_path_dashboards_cant = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/dashboards_cant' + '_' + Current_Date_Formatted + '.csv'

csv_path_dsets_cant_category = r'C:/Users/xxxxx/Desktop/Python/Enacom/Json/datasets_cant_category' + '_' + Current_Date_Formatted + '.csv'

# Creo los reportes para contar la cantidad de actualizados por mes

df_dsets_cant = df_dsets.groupby(['yearmonth'],sort=True)['yearmonth'].count()
df_dstream_cant = df_dstream.groupby(['yearmonth'],sort=True)['yearmonth'].count()
df_resources_cant = df_resources.groupby(['yearmonth'],sort=True)['yearmonth'].count()
df_visualizations_cant = df_visualizations.groupby(['yearmonth'],sort=True)['yearmonth'].count()
df_dashboards_cant = df_dashboards.groupby(['yearmonth'],sort=True)['yearmonth'].count()


df_dsets_cant_category = df_dsets.groupby([['yearmonth','category_name']])[['yearmonth','category_name']].count()


# Ejecuto el export de los csv

df_resources.to_csv(csv_path_resouces)
df_dstream.to_csv(csv_path_dstream)
df_dsets.to_csv(csv_path_dsets)
df_visualizations.to_csv(csv_path_visualizations)
df_dashboards.to_csv(csv_path_dashboards)

df_resources_cant.to_csv(csv_path_resouces_cant)
df_dstream_cant.to_csv(csv_path_dstream_cant)
df_dsets_cant.to_csv(csv_path_dsets_cant)
df_visualizations_cant.to_csv(csv_path_visualizations_cant)
df_dashboards_cant.to_csv(csv_path_dashboards_cant)

df_dsets_cant_category.to_csv(csv_path_dsets_cant_category)
