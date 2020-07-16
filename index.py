# Contains the dash app's html and core components
# Define the app layout and callbacks

from app import app
from app import server
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc  # See app.py for how to install boostrap
from dash.dependencies import Input, Output
import dash_daq as daq

# The layout of the dashboard
# Comprised of a tree of components that describe what the application looks like
# Layout coded using boostrap for responsive design

body = html.Div([
    dbc.Row([
        dbc.Col(html.Div(html.H1("COVID19 Dashboard")), lg=10, md=10, xs=10),
        dbc.Col(html.Div(html.Img(src="/assets/logo.png")), lg=2, md=2, xs=2)
    ], className="banner"),
    dbc.Row([
        dbc.Col(html.Div(html.Iframe(id="map_html", srcDoc=open("./assets/tester_manchester.html", 'r').read())),
                lg=8, md=12, xs=12, className="map"),
        dbc.Col([
            html.Div([
                dbc.Row(
                    dbc.Col([
                        html.Div(html.H1("Example Veterinary Group"), className="practice_name"),
                        dbc.Row(dbc.Container([
                            dbc.Row(html.Div(html.H2("Hospital"))),
                            # Add slider as dash core component
                            dbc.Row(html.Div([
                                html.P("Consulting Vets"),
                                dcc.Slider(
                                    min=0,
                                    max=5,
                                    value=4,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2'},
                                        3: {'label': '3'},
                                        4: {'label': '4'},
                                        5: {'label': '5', 'style': {'color': '#f50'}}
                                    },
                                    className="slider",
                                ),
                                html.P("Procedure Vets"),
                                dcc.Slider(
                                    min=0,
                                    max=4,
                                    value=3,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2'},
                                        3: {'label': '3'},
                                        4: {'label': '4', 'style': {'color': '#f50'}}
                                    },
                                    className="slider"
                                ),
                                html.P("Nurses"),
                                dcc.Slider(
                                    min=0,
                                    max=15,
                                    value=12,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {},
                                        2: {'label': '2'},
                                        3: {},
                                        4: {'label': '4'},
                                        5: {},
                                        6: {'label': '6'},
                                        7: {},
                                        8: {'label': '8'},
                                        9: {},
                                        10: {'label': '10'},
                                        11: {},
                                        12: {'label': '12'},
                                        13: {'label': '13', 'style': {'color': '#f50'}},
                                        14: {'label': '14', 'style': {'color': '#f50'}},
                                        15: {'label': '15', 'style': {'color': '#f50'}},
                                    },
                                    className="slider"
                                ),
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row(html.Div(html.H2("Branch 1"))),
                            dbc.Row(html.Div([
                                html.P("Consulting Vets"),
                                dcc.Slider(
                                    min=0,
                                    max=2,
                                    value=1,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2', 'style': {'color': '#f50'}}
                                    },
                                    className="slider"
                                ),
                                html.P("Procedure Vets"),
                                dcc.Slider(
                                    min=0,
                                    max=2,
                                    value=1,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2', 'style': {'color': '#f50'}}
                                    },
                                    className="slider"
                                ),
                                html.P("Nurses"),
                                dcc.Slider(
                                    min=0,
                                    max=5,
                                    value=3,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2'},
                                        3: {'label': '3'},
                                        4: {'label': '4', 'style': {'color': '#f50'}},
                                        5: {'label': '5', 'style': {'color': '#f50'}}
                                    },
                                    className="slider"
                                ),
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row(html.Div(html.H2("Branch 2"))),
                            dbc.Row(html.Div([
                                html.P("Consulting Vets"),
                                    dcc.Slider(
                                        min=0,
                                        max=2,
                                        value=1,
                                        marks={
                                            0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                            1: {'label': '1'},
                                            2: {'label': '2', 'style': {'color': '#f50'}}
                                        },
                                        className="slider"
                                ),
                                html.P("Procedure Vets"),
                                dcc.Slider(
                                        min=0,
                                        max=2,
                                        value=1,
                                        marks={
                                            0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                            1: {'label': '1'},
                                            2: {'label': '2', 'style': {'color': '#f50'}}
                                        },
                                        className="slider"
                                ),
                                html.P("Nurses"),
                                dcc.Slider(
                                    min=0,
                                    max=5,
                                    value=3,
                                    marks={
                                        0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                        1: {'label': '1'},
                                        2: {'label': '2'},
                                        3: {'label': '3'},
                                        4: {'label': '4', 'style': {'color': '#f50'}},
                                        5: {'label': '5', 'style': {'color': '#f50'}}
                                    },
                                    className="slider"
                                ),
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                                dbc.Row(html.Div(html.H2("Branch 3"))),
                                dbc.Row(html.Div([
                                    html.P("Consulting Vets"),
                                    dcc.Slider(
                                        min=0,
                                        max=2,
                                        value=1,
                                        marks={
                                            0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                            1: {'label': '1'},
                                            2: {'label': '2', 'style': {'color': '#f50'}}
                                        },
                                        className="slider")
                                ]), className="pbody", style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row(html.Div(html.H2("Impact Report"))),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Row(html.P("% of Routine Caseload"),
                                            style={"justify-content": "center", "padding-top": "10px"}),
                                    dbc.Row(daq.Gauge(
                                        color={"gradient": True, "ranges": {
                                            "red": [0, 20],
                                            "yellow":[20, 50],
                                            "green":[50, 100]
                                        }},
                                        value=100,
                                        max=100,
                                        min=0,
                                        className="gauge"), style={"justify-content": "center"}
                                    )]),
                                dbc.Col(dbc.Row(dash_table.DataTable(
                                        id='table',
                                        columns=[
                                            {'name': 'Excess Vets', 'id': 'column1'},
                                            {'name': 'N', 'id': 'column2'}],
                                        style_cell={
                                            'textAlign': 'left',
                                            'padding': '5px',
                                            "fontWeight": "500",
                                            "fontSize": "16px",
                                            "font-family": "sans-serif",
                                            'backgroundColor': 'rgba(250, 250, 250, 0.8)',
                                            'color': "rgba(22, 63, 85, 0.7)",
                                            "borderStyle": "none",
                                        },
                                        ), className="data_table")),
                            ], className="pbody")], className="practice"), no_gutters=True)
                    ]), className="practice_col"),
                #     dbc.Row(dbc.Col([
                #         dbc.Row(html.Div(html.H2("Impact Report"))),
                #         dbc.Row(html.Div(html.P("Impact report")), className="pbody")], className="practice"), no_gutters=True, className="bottom")
            ])
        ], lg=4, md=12, xs=12)
    ], className="main"),

    # Old versions: Tall format
    # dbc.Row([
    #         dbc.Col(html.Div(dbc.Alert("This will be the map", color="primary")), lg=12, md=12, xs=12)
    #     ], className="map"),
    #     html.Div([
    #         # Tall format
    #         dbc.Row([
    #             dbc.Col([
    #                 dbc.Row([
    #                     dbc.Col(dbc.Container([
    #                         dbc.Row(html.Div(html.H2("Hospital"))),
    #                         dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=6, md=6, xs=12),
    #                     dbc.Col(dbc.Container([
    #                         dbc.Row(html.Div(html.H2("Branch 1"))),
    #                         dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=6, md=6, xs=12)
    #                 ], no_gutters=True),
    #                 dbc.Row([
    #                     dbc.Col(dbc.Container([
    #                         dbc.Row(html.Div(html.H2("Hospital"))),
    #                         dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=6, md=6, xs=12),
    #                     dbc.Col(dbc.Container([
    #                         dbc.Row(html.Div(html.H2("Branch 1"))),
    #                         dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=6, md=6, xs=12)
    #                 ], no_gutters=True)], lg=6, md=6, xs=12),
    #             dbc.Col([
    #                 dbc.Col([
    #                     dbc.Row(html.Div(html.H2("Impact Report"))),
    #                     dbc.Row(html.Div(html.P("Impact report")), className="ibody")], className="impact", lg=12, md=12, xs=12)
    #             ], lg=6, md=6, xs=12)
    #         ])
    #     ], className="bottom")
    #     # Wide format
    #     #         dbc.Col(dbc.Container([
    #     #             dbc.Row(html.Div(html.H2("Hospital"))),
    #     #             dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=3, md=6, xs=12),
    #     #         dbc.Col(dbc.Container([
    #     #             dbc.Row(html.Div(html.H2("Branch 1"))),
    #     #             dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=3, md=6, xs=12),
    #     #         dbc.Col(dbc.Container([
    #     #             dbc.Row(html.Div(html.H2("Branch 2"))),
    #     #             dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=3, md=6, xs=12),
    #     #         dbc.Col(dbc.Container([
    #     #             dbc.Row(html.Div(html.H2("Branch 3"))),
    #     #             dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), lg=3, md=6, xs=12)
    #     #     ], no_gutters=True),
    #     #     dbc.Row([
    #     #         dbc.Col([
    #     #             dbc.Row(html.Div(html.H2("Impact Report"))),
    #     #             dbc.Row(html.Div(html.P("Impact report")), className="ibody")], className="impact", lg=12, md=12, xs=12)
    #     #     ], no_gutters=True)
    #     # ], className="bottom")
])

app.layout = html.Div([body])

# Enables more CSS flexibility
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

# The interactive component of the dashboard
# Automatically called when an input property changes

# Read in dataframe

dat = pd.read_csv("./assets/example_practice_data.txt", sep='\t')


# @app.callback(Output(component_id='graph-output', component_property='children'),
#               [Input(component_id='graph-input', component_property='')])
# def render_graph(_):
#     return dcc.Graph(
#         id='graph-1',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [10, 20, 30, 40,
#                                                    50, 60, 70], 'type': 'line', 'name': 'value1'},
#                 {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [12, 22, 36, 44,
#                                                    49, 58, 73], 'type': 'line', 'name': 'value2'}
#             ],
#             'layout': {
#                 'title': 'Simple Line Graph',
#                 'plot_bgcolor': colors['background'],
#                 'paper_bgcolor': colors['background'],
#                 'font': {
#                     'color': colors['text'],
#                     'size': 18
#                 },
#                 'xaxis': {
#                     'title': 'Variable name -1',
#                     'showspikes': True,
#                     'spikedash': 'dot',
#                     'spikemode': 'across',
#                     'spikesnap': 'cursor',
#                 },
#                 'yaxis': {
#                     'title': 'Variable name -2',
#                     'showspikes': True,
#                     'spikedash': 'dot',
#                     'spikemode': 'across',
#                     'spikesnap': 'cursor'
#                 },
#
#             }
#         }
#     )
#

# The app refreshes when you make changes to your code
if __name__ == '__main__':
    app.run_server(debug=True)
