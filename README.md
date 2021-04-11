# Datos abiertos del ente nacional de Comunicaciones de la República Argentina (Enacom)

El objetivo de este proyecto es armar un proceso automático que realice un análisis de la información disponible en la sección de datos abiertos del ente nacional de Comunicaciones de la República Argentina (Enacom). 

El código fue desarrollado en python y consta de tres etapas: 

1) En la primera genera unos reportes indicando la cantidad y el grado de actualización de los datasets utilizando la API de Enacom, que fue publicada en base a los desarrollos
de la empresa JUNAR en Django Rest Framework. La documentación está disponible en el siguiente link https://junar.github.io/docs/es/_sections/01-index.html.

Consultando la API de Enacom podemos consumir la metadata de los recursos de tipo dataset, visualizations, datastreams y dashboards a través de una llamada GET. 
Las llamadas GET nos pueden traer una lista completa de todos los conjuntos de datos o solo de un GUID específico. 

Podemos acceder a la metadata de todos los tipos de recursos disponibles en la siguiente dirección https://api.datosabiertos.enacom.gob.ar/api/v2/?auth_key=(Auth_Key), y para consultar y descargar los recursos de cada tipo se puede recorrer la lista de GUID correspondiente, introduciendo el valor del GUID en una variable.

La Auth_Key se genera en https://datosabiertos.enacom.gob.ar/developers/

Por ejemplo la lista de recursos se puede obtener de http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key=(Auth_Key) y la ubicación de las visualizaciones datastreams en http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/?auth_key=(Auth_Key).

El código que realiza esta sección se encuentra en el archivo Enacom_API_Analysis.py

2) En la segunda etapa busca la información disponible a través del portal de datos abiertos de jefatura de gabinete de ministros de la nación Argentina Datos.gob.ar creado sobre la plataforma CKAN, exporta los metadatos de cada archivo publicado y al final genera un reporte con una fila por archivo indicando la información mas relevante (nombre del archivo, url, última fecha de actualización, etc.)

Esta parte se encuentra en el archivo Enacom_Data_Gob_ar_Ckan.py

3) En la tercer etapa descarga los datasets en formato json y csv.

Para descargar automáticamente todos los archivos json se puede automatizar un proceso llamando a cada GUID de la siguiente manera   http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/{guid}/data.{format}/?auth_key=(Auth_Key)  

El codigo para la descarga automática de todos los recursos disponibles a una carpeta local se encuentra en el archivo Request_Enacom_Json.py.

Los requerimientos para para el proyecto son python 3.x, pandas, requests, csv y json
