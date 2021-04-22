import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

auth_key = 'EehRvnYPa4JHRoBtjvrwP747MLvBC49nQ3TsE3a6'

url_datasets = 'http://api.datosabiertos.enacom.gob.ar/api/v2/datasets.json/?auth_key={clave}'.format(clave=auth_key)

df_dsets = pd.read_json(url_datasets)

df_dsets['year'] = pd.DatetimeIndex(df_dsets['modified_at']).year
df_dsets['yearmonth'] = pd.DatetimeIndex(df_dsets['modified_at']).year * 100 + pd.DatetimeIndex(df_dsets['modified_at']).month
df_dsets['yearmonthday'] = pd.DatetimeIndex(df_dsets['modified_at']).year * 10000 + pd.DatetimeIndex(df_dsets['modified_at']).month * 100 + pd.DatetimeIndex(df_dsets['modified_at']).day

df_dsets_cant_cat_month2 = df_dsets.groupby(['category_name','yearmonth']).count().reset_index()
df_dsets_cant_cat_month2['cantidad'] = df_dsets_cant_cat_month2['year']

df1 = df_dsets_cant_cat_month2[['yearmonth','category_name','cantidad']]


pd.to_numeric(df1['yearmonth'])
df1['mes']=df1['yearmonth'].apply(str)
df1 = df1.sort_values(by=['yearmonth'])
dict_meses = {'mes':df1['yearmonth'].unique()}

df2 = df1.sum(axis = 0, skipna = True)

array_endpoints = df_dsets['endpoint'].unique()
df_endpoints = pd.DataFrame(array_endpoints)
df_endpoints['cantidad'] = 1
cant_datasets = df_endpoints['cantidad'].sum()

#cant_dataset_files = set_endpoints['endpoint'].size()

fig = px.bar(df1,'category_name','cantidad' ,color='yearmonth', hover_name='yearmonth', range_color = [201601,202105]
              )

fig2 = px.bar(df1,'mes','cantidad', color='category_name', hover_name='category_name', category_orders=dict_meses
              )

App_Datos_Enacom = dash.Dash('Tablero de datos abiertos de Enacom')

App_Datos_Enacom.layout = html.Div([
    html.Div([html.H1('Análisis de datasets de Enacom en datos abiertos')]),
    html.Div([dcc.Input(id='texto',value='Cantidad de recursos publicados como datasets: {cant_rec_dset}. Cantidad de archivos diferentes publicados: {cant_archivos_dset}'.format(cant_rec_dset=df2['cantidad'],cant_archivos_dset=cant_datasets),size=200,readOnly=True)]),
    html.Div([dcc.Graph(id="graph2", figure=fig2)
              ]
             ),
    html.Div([dcc.Graph(id="graph", figure=fig)
            ]
        )
    ]
)

App_Datos_Enacom.run_server()
