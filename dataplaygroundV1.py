import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

import datetime

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

date = ['MON','TUE','WED','THU','FRI','SAT','SUN']

app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Rama 4 Data Playground",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

    dbc.Row([

       

        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['MON','TUE'],
                         options=[{'label':x, 'value':x}
                                  for x in date],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
        

        dbc.Col(html.H1("Hello world :)",
                        className='text-center text-primary mb-4'),
                width=6)

    ], justify='start'),
    dbc.Row([

        

        dbc.Col([
            dcc.Dropdown(id='my-dpdn4', multi=True, value=['MON','TUE'],
                         options=[{'label':x, 'value':x}
                                  for x in date],
                         ),
            dcc.Graph(id='line-fig4', figure={})
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col(html.H1("Hello world :)",
                        className='text-center text-primary mb-4'),
                width=6)

        

    ], justify='start'), 
 ]) # Horizontal:start,center,end,between,around

    


if __name__=='__main__':
    app.run_server(debug=True, port=8000)