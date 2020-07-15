# Contains the dash app's html and core components
# Define the app layout and callbacks

from app import app
from app import server
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc  # See app.py for how to install boostrap
from dash.dependencies import Input, Output

# The layout of the dashboard
# Comprised of a tree of components that describe what the application looks like
# Layout coded using boostrap for responsive design

body = html.Div([
    dbc.Row([
        dbc.Col(html.Div(html.H1("COVID19 Dashboard")), lg=10, md=10, xs=10),
        dbc.Col(html.Div(html.Img(src="/assets/logo.png")), lg=2, md=2, xs=2)
    ], className="banner"),
    dbc.Row([
        dbc.Col(html.Div(html.P("Map goes here")), lg=8, md=8, xs=12, className="map"),
        dbc.Col([
            html.Div([
                dbc.Row(dbc.Col([
                    dbc.Row(dbc.Container([
                        dbc.Row(html.Div(html.H2("Hospital"))),
                        dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), no_gutters=True),
                    dbc.Row(dbc.Container([
                        dbc.Row(html.Div(html.H2("Hospital"))),
                        dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), no_gutters=True),
                    dbc.Row(dbc.Container([
                        dbc.Row(html.Div(html.H2("Hospital"))),
                        dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), no_gutters=True),
                    dbc.Row(dbc.Container([
                        dbc.Row(html.Div(html.H2("Hospital"))),
                        dbc.Row(html.Div(html.P("Practice text")), className="pbody")], className="practice"), no_gutters=True)
                ]), className="practice_col"),
                dbc.Row(dbc.Col([
                    dbc.Row(html.Div(html.H2("Impact Report"))),
                    dbc.Row(html.Div(html.P("Impact report")), className="ibody")], className="impact"), no_gutters=True, className="bottom")
            ])
        ], lg=4, md=4, xs=12)
    ], className="main"),





    # Tall format
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
