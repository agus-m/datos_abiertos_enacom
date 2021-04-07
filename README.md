# Datos abiertos del ente nacional de Comunicaciones de la República Argentina (Enacom)

El objetivo de este proyecto es armar un proceso automático de descarga de datasets utilizando la API de Enacom y la generación de reportes utilizando los datos disponibles.

El código fue desarrollado en python y consta de dos etapas 

1) La primera etapa consiste en la descarga de una serie de archivos Json disponibles a traves de la API. 

La API fue desarrollada por la empresa JUNAR y pueden encontrar la documentación en el siguiente link https://junar.github.io/docs/es/_sections/01-index.html.

Podemos consumir la metadata de los recursos de tipo dataset, visualizations, datastreams y dashboards través de una llamada GET. 
Las llamadas GET nos pueden traer una lista completa de todos los conjuntos de datos o solo de un GUID específico. 

Podemos acceder a la metadata de todos los tipos de recursos disponibles en la siguiente dirección https://api.datosabiertos.enacom.gob.ar/api/v2/?auth_key=(Auth_Key), y para consultar y descargar los recursos de cada tipo se puede recorrer la lista de GUID correspondiente, introduciendo el valor del GUID en una variable.

La Auth_Key se genera en https://datosabiertos.enacom.gob.ar/developers/


Por ejemplo la lista de recursos se puede obtener de http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key=(Auth_Key) y la ubicación de las visualizaciones datastreams en http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/?auth_key=(Auth_Key). Para descargar automáticamente todos los archivos json se puede automatizar un proceso llamando a cada GUID de la siguiente manera  http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/{guid}/data.{format}/?auth_key=(Auth_Key)  

El codigo para la descarga automática de todos los recursos disponibles a una carpeta local se encuentra en el archivo Request_Enacom_Json.py.
Los requerimientos para esta etapa consisten exclusivamente en el uso de python 3.x y la librería pandas para crear dataframes.

2) La segunda etapa consiste en armar reportes para control de la frecuencia con la que se actualizan los datasets y la fecha en la que fueron actualizados por última vez.

Esta parte se encuentra en el archivo xxxxxx.py


