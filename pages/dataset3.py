import dash
from dash import dcc, html, dash_table, callback, Input, Output, State
import pandas as pd

df = pd.read_csv('data/df_genre.csv')
PAGE_SIZE = 15

dash.register_page(__name__)

layout = html.Div([dash_table.DataTable(
    id='table-multicol-sorting-3',
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom',

    #filter_action='custom',
    #filter_query='',

    sort_action='custom',
    sort_mode='multi',
    sort_by=[],
    
    style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'color': 'white',
        'border': '1px solid black' 
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'},
    style_cell={ 'border': '1px solid black' },
    
)],style={'overflowY': 'scroll'}, className='dash-table-container')

@callback(
    Output('table-multicol-sorting-3', "data"),
    Input('table-multicol-sorting-3', "page_current"),
    Input('table-multicol-sorting-3', "page_size"),
    Input('table-multicol-sorting-3', "sort_by"))
def update_table_3(page_current, page_size, sort_by):
    print(sort_by)
    if len(sort_by):
        dff = df.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')