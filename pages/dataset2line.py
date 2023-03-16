from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import dcc, html, callback, Input, Output, State
import pandas as pd
from dash import ctx
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc


dash.register_page(__name__)

df = pd.read_csv('data/df_year.csv')

list_columns_numerical = df.columns.tolist()

#function that has a column name as input, and a graph name (for the label name) as output. 
def map_col_name_to_graph_name_year(column_name):
    columns = df.columns.tolist()
    graph_names = ['Year',
     'Number of Releases',
     'Duration (Milliseconds)',
     'Explicit ratio',
     'Danceability',
     'Energy',
     'Loudness (Db)',
     'Speechiness',
     'Acousticness',
     'Instrumentalness',
     'Liveness',
     'Valence',
     'Tempo (BPM)']
    try: 
        index = columns.index(column_name)
    except:
        print('This is not a column name!')
    return graph_names[index]


layout = html.Div([html.Div([
    html.Div([html.P('Select fields below to be used in the line chart')]),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name_year(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-line-1',value='Average_liveness', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
    html.Div([dcc.Dropdown(
                                                options=[{'label': map_col_name_to_graph_name_year(column), 'value': column} for i, column in enumerate(df.columns.tolist())],
                                            id='input-line-2',value='Average_energy', clearable=False,
                                            style={'width':'100%', 'padding':'0px', 'font-size':'15px', 'text-align-last':'center'}
                                            )], className='select-field-container'),
                                            
], className='select-fields-container'), 


html.Div([
    dcc.Graph(id='line-2',style={'width': '100vh', 'height': '85vh'})
], className='scatter-plot-container')], 
style={'height':'100%', 'width':'100%'})




@callback(
    Output("line-2", "figure"), 
    [Input("input-line-1", "value"),Input('input-line-2', 'value')],)
def make_line(field1, field2):
    df_copy = df.copy()

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df_copy['year'], y=df_copy[field1], # replace with your own data source
        name=map_col_name_to_graph_name_year(field1)), secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df_copy['year'], y=df_copy[field2], # replace with your own data source
        name=map_col_name_to_graph_name_year(field2)), secondary_y=True,
    )

    # Add figure title
    fig.update_layout(template= 'plotly_dark',title_text="A double line chart of " + map_col_name_to_graph_name_year(field1) + " and " +map_col_name_to_graph_name_year(field2))

    # Set x-axis title
    fig.update_xaxes(title_text="Year")

    # Set y-axes titles
    fig.update_yaxes(
        title_text=map_col_name_to_graph_name_year(field1), 
        secondary_y=False)
    fig.update_yaxes(
        title_text=map_col_name_to_graph_name_year(field2), 
        secondary_y=True)

    return fig