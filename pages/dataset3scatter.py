import dash
from dash import dcc, html, callback, Input, Output, State
import pandas as pd
from dash import ctx
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc

df = pd.read_csv('data/df_genre.csv')

list_columns_numerical = df.columns.tolist()

#function that has a column name as input, and a graph name (for the label name) as output. 
def map_col_name_to_graph_name_genre(column_name):
    columns = df.columns.tolist()
    graph_names = ['Genre',
     'Number of songs',
     'Duration',
     'Explicit ratio',
     'Danceability',
     'Energy',
     'Loudness',
     'Speechiness',
     'Acousticness',
     'Instrumentalness',
     'Liveness',
     'Valence',
     'Tempo']
    try: 
        index = columns.index(column_name)
    except:
        print('This is not a column name!')
    return graph_names[index]

dash.register_page(__name__)

layout = html.Div([html.Div([
    html.Div([html.P('Select fields below to be used in the scatter plot')]),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name_genre(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-1-3',value='Average_energy', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name_genre(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-2-3',value='genre', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name_genre(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-3-3',value='Average_danceability', 
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container')
                                            
], className='select-fields-container'), 


html.Div([
    dcc.Graph(id='scatter-3',style={'width': '100vh', 'height': '85vh'})
], className='scatter-plot-container')], 
style={'height':'100%', 'width':'100%'})

@callback(
    Output(component_id='scatter-3', component_property='figure'),
    [Input(component_id='input-scatter-1-3', component_property='value'),
     Input(component_id='input-scatter-2-3', component_property='value'),
     Input(component_id='input-scatter-3-3', component_property='value')
    ],
    prevent_initial_call=False)
def make_scatter_3(field1, field2, field3 = None):
    df_copy = df.copy()
    if field3 != None:
        figure_scatter = px.scatter(df_copy, x=field1, y=field2, color=field3, template='plotly_dark', 
                                    labels = {field1: map_col_name_to_graph_name_genre(field1),
                                                field2 : map_col_name_to_graph_name_genre(field2),
                                                field3 : map_col_name_to_graph_name_genre(field3)},
                                    title = "Scatter plot of " + map_col_name_to_graph_name_genre(field1) + " VS " + map_col_name_to_graph_name_genre(field2) + " VS " + map_col_name_to_graph_name_genre(field3))
    else:
        figure_scatter = px.scatter(df_copy, x=field1, y=field2, template='plotly_dark', 
                                    labels = {field1: map_col_name_to_graph_name_genre(field1),
                                                field2 : map_col_name_to_graph_name_genre(field2)},
                                    title = "Scatter plot of " + map_col_name_to_graph_name_genre(field1) + " VS " + map_col_name_to_graph_name_genre(field2))

    figure_scatter.update_layout(
    font=dict(
        #family="Courier New, monospace",
        size=10
    ))
    
    return figure_scatter