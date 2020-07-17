# Contains the dash app's html and core components
# Define the app layout and callbacks

from app import app
from app import server
import pandas as pd
import math
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc  # See app.py for how to install boostrap
from dash.dependencies import Input, Output
import dash_daq as daq


dat = pd.read_csv("./assets/example_practice_data.txt", sep='\t')

df = dat[["Routine Vets", "Routine Nurses"]]
routine_vets = df['Routine Vets'].sum()

df_vets = dat[["Routine Vets"]]
df_nurses = dat[["Routine Nurses"]]
routine_vets = df['Routine Vets'].sum()
routine_nurses = df['Routine Nurses'].sum()

# df = df.rename(columns={"Excess Vets":"Vets", "Excess Nurses": "Nurses"})


# The layout of the dashboard
# Comprised of a tree of components that describe what the application looks like
# Layout coded using boostrap for responsive design

body = html.Div([
    dbc.Row([
        dbc.Col(html.Div(html.H1("COVID19 Dashboard")), lg=10, md=10, xs=10),
        dbc.Col(html.Div(html.Img(src="/assets/logo.png")), lg=2, md=2, xs=2)
    ], className="banner"),
    dbc.Row([
        dbc.Col(html.Div(html.Iframe(id="map_html", srcDoc=open("./assets/manchester_singleFile.html", 'r').read())),
                lg=8, md=12, xs=12, className="map"),
        dbc.Col([
            html.Div([
                dbc.Row(
                    dbc.Col([
                        html.Div(html.H1("PetHack Veterinary Group"), className="practice_name"),
                        dbc.Row(dbc.Container([
                            dbc.Row([
                                dbc.Col(html.Div(html.H2("Hospital"))),
                                dbc.Col(html.Div(dcc.Slider(
                                    min=0,
                                    max=1,
                                    value=1,
                                    marks={
                                        0: {'label': 'Closed', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                        1: {'label': 'Open', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                    },
                                    className="slider-opening",
                                    id="hospital-open-slider"
                                ),
                                    style={
                                    "width": "100 %",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "right",
                                    "fontFamily": "sans-serif",
                                    "fontWeight": "500",
                                    "padding": "10px"
                                }
                                ))
                            ]),
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
                                    id="hospital-consult-slider"
                                ),
                                html.P("Procedure Vets"),
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
                                    id="hospital-procedure-slider"
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
                                    className="slider",
                                    id="hospital-nurse-slider"
                                ),
                                html.Div(id="hospital-nurse-warning", className="nurse-warning")
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row([
                                dbc.Col(html.Div(html.H2("Branch 1"))),
                                dbc.Col(html.Div(dcc.Slider(
                                    min=0,
                                    max=1,
                                    value=1,
                                    marks={
                                        0: {'label': 'Closed', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                        1: {'label': 'Open', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                    },
                                    className="slider-opening",
                                    id="branch1-open-slider"
                                ),
                                    style={
                                    "width": "100 %",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "right",
                                    "fontFamily": "sans-serif",
                                    "fontWeight": "500",
                                    "padding": "10px"
                                }
                                ))
                            ]),
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
                                    className="slider",
                                    id="branch1-consult-slider"
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
                                    className="slider",
                                    id="branch1-procedure-slider"
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
                                    className="slider",
                                    id="branch1-nurse-slider"
                                ),
                                html.Div(id="branch1-nurse-warning", className="nurse-warning")
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row([
                                dbc.Col(html.Div(html.H2("Branch 2"))),
                                dbc.Col(html.Div(dcc.Slider(
                                    min=0,
                                    max=1,
                                    value=1,
                                    marks={
                                        0: {'label': 'Closed', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                        1: {'label': 'Open', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                    },
                                    className="slider-opening",
                                    id="branch2-open-slider"
                                ),
                                    style={
                                    "width": "100 %",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "right",
                                    "fontFamily": "sans-serif",
                                    "fontWeight": "500",
                                    "padding": "10px"
                                }
                                ))
                            ]),
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
                                        className="slider",
                                        id="branch2-consult-slider"
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
                                        className="slider",
                                        id="branch2-procedure-slider"
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
                                    className="slider",
                                    id="branch2-nurse-slider"
                                ),
                                html.Div(id="branch2-nurse-warning", className="nurse-warning")
                            ]),
                                className="pbody",
                                style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row([
                                dbc.Col(html.Div(html.H2("Branch 3"))),
                                dbc.Col(html.Div(dcc.Slider(
                                    min=0,
                                    max=1,
                                    value=1,
                                    marks={
                                        0: {'label': 'Closed', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                        1: {'label': 'Open', 'style': {'color': 'rgba(22, 63, 85, 0.7)'}},
                                    },
                                    className="slider-opening",
                                    id="branch3-open-slider"
                                ),
                                    style={
                                    "width": "100 %",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "right",
                                    "fontFamily": "sans-serif",
                                    "fontWeight": "500",
                                    "padding": "10px"
                                }
                                ))
                            ]),
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
                                    className="slider",
                                    id="branch3-consult-slider"
                                )
                            ]), className="pbody", style={"width": "100 %", "display": "flex", "align-items": "center", "justify-content": "center"})],
                            className="practice"), no_gutters=True),
                        dbc.Row(dbc.Container([
                            dbc.Row(html.Div(html.H2("Impact Report"))),
                            dbc.Row([
                                dbc.Col(dbc.Container([
                                    dbc.Row(html.P("% of Routine Caseload"),
                                            style={"justify-content": "center",
                                                   "padding-top": "10px"},
                                            no_gutters=True),
                                    dbc.Row(daq.Gauge(
                                        color={"gradient": True, "ranges": {
                                            "#f40": [0, 20],
                                            # "yellow":[20, 50],
                                            "skyblue":[20, 100]
                                        }},
                                        value=100,
                                        max=100,
                                        min=0,
                                        className="gauge", id="gauge_indicator"), style={"justify-content": "center"}, no_gutters=True,
                                    )], className="gauge-box"), lg=7, md=7, xs=12),
                                dbc.Col([
                                    dbc.Container([
                                        dbc.Row(html.Div(id="excess-vets", className="excess-number"),
                                                style={"justify-content": "center", "padding-top": "10px"}, no_gutters=True),
                                        dbc.Row(html.P("Excess Vets"),
                                                style={"justify-content": "center"}, no_gutters=True),
                                    ], className="excess-box"),
                                    dbc.Container([
                                        dbc.Row(html.Div(id="excess-nurses", className="excess-number"),
                                                style={"justify-content": "center", "padding-top": "10px"}, no_gutters=True),
                                        dbc.Row(html.P("Excess Nurses"),
                                                style={"justify-content": "center"}, no_gutters=True),
                                    ], className="excess-box", style={"margin-top": "20px"}),
                                ], lg=5, md=5, xs=12),
                            ], className="pbody")], className="practice"), no_gutters=True)
                    ]), className="practice_col"),
                #     dbc.Row(dbc.Col([
                #         dbc.Row(html.Div(html.H2("Impact Report"))),
                #         dbc.Row(html.Div(html.P("Impact report")), className="pbody")], className="practice"), no_gutters=True, className="bottom")
            ])
        ], lg=4, md=12, xs=12)
    ], className="main"),
])

app.layout = html.Div([body])

# Enables more CSS flexibility
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

# The interactive component of the dashboard
# Automatically called when an input property changes

# Hospital consulting vets


@app.callback(
    Output("hospital-consult-slider", "value"),
    [Input("hospital-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 4
    return value

# Hospital procedure vets


@app.callback(
    Output("hospital-procedure-slider", "value"),
    [Input("hospital-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 4
    return value

# Hospital nurses


@app.callback(
    Output("hospital-nurse-slider", "value"),
    [Input("hospital-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 12
    return value

# Hospital nurse warning


@app.callback(
    Output("hospital-nurse-warning", "children"),
    [Input("hospital-nurse-slider", "value"),
     Input("hospital-procedure-slider", "value"),
     Input("hospital-consult-slider", "value")])
def update_output_div(selection1, selection2, selection3):
    vets = selection2 + selection3
    nurses = selection1
    if nurses < (math.ceil(1*vets)):
        return 'You may not have enough nurses at this practice'
    if nurses > (math.ceil(2*vets)):
        return 'You may have too many nurses at this practice'

# Branch 1


@app.callback(
    Output("branch1-consult-slider", "value"),
    [Input("branch1-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 1
    return value


@app.callback(
    Output("branch1-procedure-slider", "value"),
    [Input("branch1-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 1
    return value


@app.callback(
    Output("branch1-nurse-slider", "value"),
    [Input("branch1-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 3
    return value

# Branch1 nurse warning


@app.callback(
    Output("branch1-nurse-warning", "children"),
    [Input("branch1-nurse-slider", "value"),
     Input("branch1-procedure-slider", "value"),
     Input("branch1-consult-slider", "value")])
def update_output_div(selection1, selection2, selection3):
    vets = selection2 + selection3
    nurses = selection1
    if nurses < (math.ceil(1*vets)):
        return 'You may not have enough nurses at this practice'
    if nurses > (math.ceil(2*vets)):
        return 'You may have too many nurses at this practice'

# Branch 2


@app.callback(
    Output("branch2-consult-slider", "value"),
    [Input("branch2-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 1
    return value


@app.callback(
    Output("branch2-procedure-slider", "value"),
    [Input("branch2-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 1
    return value


@app.callback(
    Output("branch2-nurse-slider", "value"),
    [Input("branch2-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 3
    return value

# Branch2 nurse warning


@app.callback(
    Output("branch2-nurse-warning", "children"),
    [Input("branch2-nurse-slider", "value"),
     Input("branch2-procedure-slider", "value"),
     Input("branch2-consult-slider", "value")])
def update_output_div(selection1, selection2, selection3):
    vets = selection2 + selection3
    nurses = selection1
    if nurses < (math.ceil(1*vets)):
        return 'You may not have enough nurses at this practice'
    if nurses > (math.ceil(2*vets)):
        return 'You may have too many nurses at this practice'

# Branch 3


@app.callback(
    Output("branch3-consult-slider", "value"),
    [Input("branch3-open-slider", "value")])
def update_slider(selection):
    if selection == 0:
        value = 0
    else:
        value = 1
    return value

# Table


@app.callback(
    Output("excess-vets", "children"),
    [
        Input("hospital-procedure-slider", "value"),
        Input("hospital-consult-slider", "value"),
        Input("branch1-procedure-slider", "value"),
        Input("branch1-consult-slider", "value"),
        Input("branch2-procedure-slider", "value"),
        Input("branch2-consult-slider", "value"),
        Input("branch3-consult-slider", "value")
    ])
def update_output_div(
    sel1,
    sel2,
    sel3,
    sel4,
    sel5,
    sel6,
    sel7
):
    vets = sel1+sel2+sel3+sel4+sel5+sel6+sel7
    cases = (routine_vets-vets)
    if cases > 0:
        children = cases
    if cases <= 0:
        children = 0
    return children


@app.callback(
    Output("excess-nurses", "children"),
    [
        Input("hospital-nurse-slider", "value"),
        Input("branch1-nurse-slider", "value"),
        Input("branch2-nurse-slider", "value")
    ])
def update_output_div(
    sel1,
    sel2,
    sel3,
):
    nurses = sel1+sel2+sel3
    cases = (routine_nurses-nurses)
    if cases > 0:
        children = cases
    if cases <= 0:
        children = 0
    return children

# Gauge


@app.callback(
    Output("gauge_indicator", "value"),
    [
        Input("hospital-procedure-slider", "value"),
        Input("hospital-consult-slider", "value"),
        Input("branch1-procedure-slider", "value"),
        Input("branch1-consult-slider", "value"),
        Input("branch2-procedure-slider", "value"),
        Input("branch2-consult-slider", "value"),
        Input("branch3-consult-slider", "value")
    ])
def update_output_div(
    sel1,
    sel2,
    sel3,
    sel4,
    sel5,
    sel6,
    sel7
):
    vets = sel1+sel2+sel3+sel4+sel5+sel6+sel7
    cases = ((vets/routine_vets)*100)
    if cases <= 100:
        value = cases
    if cases > 100:
        value = 100
    return value


# The app refreshes when you make changes to your code
if __name__ == '__main__':
    app.run_server(debug=True)
