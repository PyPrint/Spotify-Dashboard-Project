import dash
from dash import html, ctx
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_daq as daq
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('data/df.csv')



# Create a dash application
app = dash.Dash(__name__, assets_url_path='\assets', use_pages=True)
#print('dash.page_registry.values():',dash.page_registry.values())
# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Application layout
app.layout = html.Div(children=[
                                html.Div([html.Div([html.H1(['Spotify Music Knowledge Dashboard']),html.A(html.I(className='bx bxl-spotify'), href="https://open.spotify.com/playlist/37i9dQZF1F0sijgNaJdgit?si=e9f68e329f52464b")], className='title-container'), 
                                          html.Div([dcc.Link(html.Div([html.Div(html.P('Introduction of the dashboard'), className='option-text-chart'), html.Div([html.I(className='bx bx-cog')], className='option-icon-chart')], className='option-chart'), href='/'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Information about the Spotify dataset'), className='option-text-chart'), html.Div([html.I(className='bx bx-info-circle')], className='option-icon-chart')], className='option-chart'), href='/informationdataset'),
                                                    html.Div([html.Div(html.A('Github Repository', href='https://github.com/PyPrint/Spotify-Dashboard-Project'), className='option-text-chart'), html.Div([html.I(className='bx bxl-github')], className='option-icon-chart')], className='option-chart')],className='more-info-container'),    
                                          html.Div([html.H1('Original dataset'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Dataset'), className='option-text-chart'), html.Div([html.I(className='bx bx-data')], className='option-icon-chart')], className='option-chart'), href='/dataset1'),
                                                    dcc.Link(html.Div([html.Div(html.P('Scatter Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-scatter-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset1scatter'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Correlation Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-network-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset1correlation'),
                                                    dcc.Link(html.Div([html.Div(html.P('Histogram Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-bar-chart')], className='option-icon-chart')], className='option-chart'),href='/dataset1hist')], className='chart-selection-container'),
                                          html.Div([html.H1('Dataset grouped by Release Year'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Dataset'), className='option-text-chart'), html.Div([html.I(className='bx bx-data')], className='option-icon-chart')], className='option-chart'), href='/dataset2'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Correlation Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-network-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset2correlation'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Line Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-line-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset2line')], className='chart-selection-container'),
                                          html.Div([html.H1('Dataset grouped by Genre'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Dataset'), className='option-text-chart'), html.Div([html.I(className='bx bx-data')], className='option-icon-chart')], className='option-chart'), href='/dataset3'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Scatter Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-scatter-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset3scatter'), 
                                                    dcc.Link(html.Div([html.Div(html.P('Correlation Plot'), className='option-text-chart'), html.Div([html.I(className='bx bx-network-chart')], className='option-icon-chart')], className='option-chart'), href='/dataset3correlation')], className='chart-selection-container')], className ='main-menu-container'),
                                        html.Div([dash.page_container],className='big-container')
                               ], style = {'width':'100%', 'height':'100%'}
    )
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)