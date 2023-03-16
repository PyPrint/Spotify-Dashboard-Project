import dash
from dash import dcc, html, callback, Input, Output, State
import pandas as pd
from dash import ctx
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc

df = pd.read_csv('data/df.csv')
df_genre = pd.read_csv('data/df_genre.csv')
df_year = pd.read_csv('data/df_year.csv')

list_columns_numerical = df.columns.tolist()
list_columns_numerical.remove('genre')
list_columns_numerical.remove('artist')
list_columns_numerical.remove('song')
list_columns_numerical

#function that has a column name as input, and a graph name (for the label name) as output. 
def map_col_name_to_graph_name(column_name):
    columns = df.columns.tolist()
    graph_names = ['Artist',
     'Song Name',
     'Duration (Milliseconds)',
     'Explicit',
     'Release Year',
     'Popularity',
     'Danceability',
     'Energy',
     'Key',
     'Loudness (Db)',
     'Mode',
     'Speechiness',
     'Acousticness',
     'Instrumentalness',
     'Liveness',
     'Valence',
     'Tempo (BPM)',
     'Genre']
    try: 
        index = columns.index(column_name)
    except:
        print('This is not a column name!')
    return graph_names[index]


dash.register_page(__name__)

layout = html.Div([html.Div([
    html.Div([html.P('Select the fields below to be used in the correlation heatmap')]),
    
    html.Div([dcc.Checklist(options=[{'label': map_col_name_to_graph_name(column), 'value': column} for i, column in enumerate(list_columns_numerical)],
                                    value=list_columns_numerical,
                                    id='input-corr', inline=True, style={"width": '80%', 'display': "block"})]),
    ], className='select-boxes-container'),
    html.Div([dcc.Graph(id='corr',style={'width': '100vh', 'height': '85vh'})], 
             className='corr-plot-container')], style={"width": '100%', 'height':'100%'})




@callback(
    Output(component_id='corr', component_property='figure'),
    [Input(component_id='input-corr', component_property='value')
    ],
    prevent_initial_call=False)
def make_corr(list_corr):
    df_copy = df.copy()
    figure_corr = px.imshow(df_copy[list_corr].corr(), text_auto=True, template='plotly_dark',
                            title= "Correlation plot of the selected fields",
                            x=[map_col_name_to_graph_name(column) for column in list_corr],
                            y=[map_col_name_to_graph_name(column) for column in list_corr])
    figure_corr.update_layout(
    font=dict(
        size=10
    ))
        
    return figure_corr