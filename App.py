import dash
from dash import html, ctx
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('df.csv')
df_genre = pd.read_csv('df_genre.csv')
df_year = pd.read_csv('df_year.csv')

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



# Create a dash application
app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Application layout
app.layout = html.Div(children=[
                                html.H1('Spotify Music Knowledge Dashboard'),
                                html.Div([
                                        html.Div([
                                            html.H1('Scatterplot of 2D or 3D data')
                                        ],), 
                                        html.Div([
                                            html.H1('Select field 1:', style={'margin-right': '2em'}), 
                                            dcc.Dropdown(
                                                options=[{'label': column, 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-1',value='loudness', clearable=False
                                            )
                                        ],),
                                        html.Div([
                                            html.H1('Select field 2:', style={'margin-right': '2em'}), 
                                            dcc.Dropdown(
                                                options=[{'label': column, 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-2',value='energy', clearable=False,
                                            style={'width':'30px', 'padding':'3px', 'font-size':'10px', 'text-align-last':'center'}
                                            )
                                        ],),
                                        html.Div([
                                            html.H1('Select field 3:', style={'margin-right': '2em'}), 
                                            dcc.Dropdown(
                                                options=[{'label': column, 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-scatter-3',value='danceability', 
                                            style={'width':'30px', 'padding':'3px', 'font-size':'10px', 'text-align-last':'center'}
                                            )
                                        ],),                                     
                                        ],),
                                html.Div([dcc.Graph(id='scatter',style={'width': '400px', 'height': '400px', 'font-size':'10px'})]),
                                html.Div([dcc.Checklist(options=
                                    [{'label': column, 'value': column} for i, column in enumerate(list_columns_numerical)],
                                    value=list_columns_numerical,
                                    id='input-corr')
                                ]),
                                html.Div([dcc.Graph(id='corr',style={'width': '800px', 'height': '800px', 'font-size':'20px'})]),
    #style={'width':'100px', 'padding':'3px', 'font-size':'15px', 'line-height':'1', 'text-align-last':'center', 'color': '#white !important', 'border':'0','background':'#000000'}
                                            
    #html.Div([
    #daq.StopButton(
    #    id='my-stop-button-1',
    #    label='Default',
    #    n_clicks=0
    #),
    #html.Div(id='stop-button-output-1')])
                               ],
    )
                                
@app.callback(
    [Output(component_id='scatter', component_property='figure'),
     Output(component_id='corr', component_property='figure')],
    [Input(component_id='input-scatter-1', component_property='value'),
     Input(component_id='input-scatter-2', component_property='value'),
     Input(component_id='input-scatter-3', component_property='value'),
     Input(component_id='input-corr', component_property='value'),
    ],
    prevent_initial_call=False)
def multiple_callbacks(field1, field2, field3, list_corr):
    df_copy = df.copy()
    figure_scatter = px.scatter(df_copy, x=field1, y=field2, color=field3, template='plotly_dark')
    figure_scatter.update_layout(
    font=dict(
        #family="Courier New, monospace",
        size=10
    ))
    
    figure_corr = px.imshow(df[list_corr].corr(), text_auto=True, aspect="auto", template='plotly_dark')
    figure_scatter.update_layout(
    font=dict(
        #family="Courier New, monospace",
        size=10
    ))
    
    return figure_scatter, figure_corr

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)