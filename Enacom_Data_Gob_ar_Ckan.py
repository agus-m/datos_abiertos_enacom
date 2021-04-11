import csv
import requests     # 2.18.4
import json         # 2.0.9
import pandas as pd # 0.23.0


# Package list of the Data Gob ar open data portal

packages = 'https://datos.gob.ar/api/3/action/package_list'
response = requests.get(packages)

# Use the json module to load CKAN's response into a dictionary
response_dict = json.loads(response.content)

# Check the contents of the response
assert response_dict['success'] is True  # make sure if response is OK

datasets = response_dict['result']         # extract all the packages from the response

# Creo una lista seleccionando solamente los datasets de enacom

enacom_datasets = []

for resources in datasets:
    if resources[0:7] == 'enacom-':
        enacom_datasets.append(resources)


# Base url for package information.

base_url = 'http://datos.gob.ar/api/3/action/package_show?id='

Lst_archivos_enacom_Data_Gob_ar = []

# Recorro todos los nombres de dataset descargando el archivo que tiene los metadatos de Datos.Gob.ar

for archivo in enacom_datasets:
    package_information_url = base_url + archivo

    # creo un dataframe con la informacion del json que devuelve DataGobAr para el recurso seleccionado y lo exporto a csv

    df_package = pd.read_json(package_information_url)
    path_DataGobAr = r'C:/Users/xxxxx/Desktop/Python/Enacom/DataGobAr/Metadatos_por_archivo/{file}_DataGobAr{formato}'.format(file=archivo,formato='.csv')
    df_package.to_csv(path_DataGobAr)

    # Make the HTTP request
    package_information = requests.get(package_information_url)

    # Use the json module to load CKAN's response into a dictionary
    package_dict = json.loads(package_information.content)

    # Check the contents of the response.
    assert package_dict['success'] is True  # again make sure if response is OK
    package_dict = package_dict['result']   # we only need the 'result' part from the dictionary

    # Exportamos los datos de result para ver los metadatos de cada dataset

    path_DataGobAr_result = r'C:/Users/xxxxx/Desktop/Python/Enacom/DataGobAr/Metadatos_por_archivo/{file}_DataGobAr_Res{formato}'.format(file=archivo,formato='.csv')

    with open(path_DataGobAr_result, 'w') as f: 
        w = csv.DictWriter(f, package_dict.keys())
        w.writeheader()
        w.writerow(package_dict)

    # pprint.pprint(package_dict)           # pretty print the package information to screen

    # Guardo el nombre, la descripcion, la url y los formatos en una lista  para poder exportarla despues del loop

    # Get data from the dictionary, first metadata from the file, and next nested data from resources

    archivo_Datos_Gob_ar_id = package_dict['id']
    archivo_name = package_dict['name']
    archivo_notes = package_dict['notes']
    archivo_title = package_dict['title']

    data_name = package_dict['resources'][0]['name']
    data_last_mod = package_dict['resources'][0]['last_modified']
    data_url = package_dict['resources'][0]['url']
    data_access = package_dict['resources'][0]['accessURL']
    data_description = package_dict['resources'][0]['description']
    data_format = package_dict['resources'][0]['format']


    Lst_archivos_enacom_Data_Gob_ar.append([archivo_Datos_Gob_ar_id, archivo_name,archivo_notes,archivo_title,data_name,data_last_mod,data_url, data_access,data_description,data_format])

# Exporto la lista con todos los parametros

df_archivos_enacom_Data_Gob_ar = pd.DataFrame(Lst_archivos_enacom_Data_Gob_ar,columns=['Dataset_id','file_name','notes','title','res_name','last_mod','url','access','description','format'])

path_res_lista_datasets = r'C:/Users/xxxxx/Desktop/Python/Enacom/DataGobAr/Metadatos_por_archivo/Lista_Datasets_Enacom_DataGobAr_Res{formato}'.format(formato='.csv')

df_archivos_enacom_Data_Gob_ar.to_csv(path_res_lista_datasets)
