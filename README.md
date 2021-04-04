# Datos abiertos del ente nacional regulador de Comunicaciones (Enacom)

El objetivo de este proyecto es armar un proceso automático de descarga de datasets utilizando la API de Enacom y la generación de reportes utilizando los datos disponibles.

El código fue desarrollado en python y consta de dos etapas 

1) La primera etapa consiste en la descarga de una serie de archivos Json disponibles a traves de la API. 
La ubicación de los archivos es http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/ y la lista de archivos disponibles está en 
http://api.datosabiertos.enacom.gob.ar/api/v2/resources.json/?auth_key= (Auth_Key)

La Auth_Key se genera en https://datosabiertos.enacom.gob.ar/developers/

El codigo para la descarga se encuentra en el archivo Request_Enacom_Json.py 

2) La segunda etapa consiste en armar reportes para control de la frecuencia con la que se actualizan los datasets y la fecha en la que fueron actualizados por última vez.

Esta parte se encuentra en el archivo xxxxxx.py
