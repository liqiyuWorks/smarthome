import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "location.csv")))
# print(df)

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Student Coordinates'),
                    # html.H5('Enegry Consumption'),
                ],
            ),
        ],
    )
def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Batch'][:7],
                    'y': df['Total'][:7],
                    # 'name': 'Techniques',
                    # 'marker': {'size': 12}
                },
                # {
                #     'x': [10],
                #     'y': [100],
                # },
                # {
                #     'x': [20],
                #     'y': [20],
                # },
                # {
                #     'x': [15],
                #     'y': [150],
                # },
                # {
                #     'x': [40],
                #     'y': [160],
                # },
                # {
                #     'x': [30],
                #     'y': [180],
                # },
                # {
                #     'x': [50],
                #     'y': [179],
                # },
                # {
                #     'x': [0],
                #     'y': [200],
                # },
                # {
                #     'x': [30],
                #     'y': [100],
                # },
                # {
                #     'x': [20],
                #     'y': [100],
                # },
                # {
                #     'x': [20],
                #     'y': [100],
                # },
                # {
                #     'x': [10],
                #     'y': [100],
                # },
                # {
                #     'x': [10],
                #     'y': [100],
                # },


            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                },
                "xaxis":{
                    'title':'longitude',
                },
                "yaxis":{
                    'title':'latitude',
                }
        }
        }
    )

# def build_graph():
#     return dcc.Graph(
#         id='basic-interactions',
#         figure={
#             'data': [
#                 {
#                     'x': df['Batch'][:50],
#                     'y': df['Techniques'][:50],
#                     'name': 'Techniques',
#                     'marker': {'size': 12}
#                 },
#                 {
#                     'x': df['Batch'][:50],
#                     'y': df['Workplace'][:50],
#                     'name': 'Workplace',
#                     'marker': {'size': 12}
#                 },
#                 {
#                     'x': df['Batch'][:50],
#                     'y': df['Garage'][:50],
#                     'name': 'Garage',
#                     'marker': {'size': 12}
#                 },
#                 {
#                     'x': df['Batch'][:50],
#                     'y': df['Kitchen'][:50],
#                     'name': 'Kitchen',
#                     'marker': {'size': 12}
#                 },
#                 {
#                     'x': df['Batch'][:50],
#                     'y': df['Hall'][:50],
#                     'name': 'Hall',
#                     'marker': {'size': 12}
#                 },
#             ],
#             'layout': {
#                 'plot_bgcolor': theme['background'],
#                 'paper_bgcolor': theme['background'],
#                 'font': {
#                     'color': theme['text']
#                 }
#             }
#         }
#     )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
