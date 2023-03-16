import dash
from dash import dcc, html, callback, Input, Output, State
import pandas as pd
from dash import ctx
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import plotly.tools as tls
import plotly.graph_objects as go
import numpy as np
    
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
    html.Div([html.P('Select fields below to be used in the scatter plot')]),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-hist-1',value='loudness', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-hist-2',value='energy', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-hist-3',value='danceability', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-hist-4',value='liveness', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container')
                                            
], className='select-fields-container'), 


html.Div([
    dcc.Graph(id='hist1',style={'width': '40vh', 'height': '37vh'})
], className='hist-plot-container'), 
html.Div([
    dcc.Graph(id='hist2',style={'width': '40vh', 'height': '37vh'})
], className='hist-plot-container'), 
html.Div([
    dcc.Graph(id='hist3',style={'width': '40vh', 'height': '37vh'})
], className='hist-plot-container'), 
html.Div([
    dcc.Graph(id='hist4',style={'width': '40vh', 'height': '37vh'})
], className='hist-plot-container')], 
style={'height':'100%', 'width':'100%'})



@callback(
    [Output(component_id='hist1', component_property='figure'),
     Output(component_id='hist2', component_property='figure'),
     Output(component_id='hist3', component_property='figure'),
     Output(component_id='hist4', component_property='figure')],
    [Input(component_id='input-hist-1', component_property='value'),
     Input(component_id='input-hist-2', component_property='value'),
     Input(component_id='input-hist-3', component_property='value'),
     Input(component_id='input-hist-4', component_property='value')],
    prevent_initial_call=False)
def make_histograms(field1, field2, field3, field4):
    df_copy = df.copy()
    print('field1', field1)
    hist1 = px.histogram(df_copy, x=field1,template='plotly_dark',color_discrete_sequence=['indianred'], title="Histogram of " + map_col_name_to_graph_name(field1))
    hist1.add_vline(x=np.median(df[field1]), line_dash = 'dash', line_color = 'white')
    hist2 = px.histogram(df_copy, x=field2,template='plotly_dark',color_discrete_sequence=['lightblue'], title="Histogram of " + map_col_name_to_graph_name(field2))
    hist2.add_vline(x=np.median(df[field2]), line_dash = 'dash', line_color = 'white')
    hist3 = px.histogram(df_copy, x=field3,template='plotly_dark',color_discrete_sequence=['lightgreen'], title="Histogram of " + map_col_name_to_graph_name(field3))
    hist3.add_vline(x=np.median(df[field3]), line_dash = 'dash', line_color = 'white')
    hist4 = px.histogram(df_copy, x=field4,template='plotly_dark',color_discrete_sequence=['violet'], title="Histogram of " + map_col_name_to_graph_name(field4))
    hist4.add_vline(x=np.median(df[field4]), line_dash = 'dash', line_color = 'white')
    return hist1, hist2, hist3, hist4