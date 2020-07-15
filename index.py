# Contains the dash app's html and core components
# Define the app layout and callbacks

from app import app
from app import server
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': 'black'
}

app.layout = html.Div([html.H1('Dash Demo Graph',
                               style={
                                   'textAlign': 'center',
                                   "background": "yellow"}),
                       html.Div(id='graph-input'),
                       html.H1(id='graph-output'),

                       ], style={
    "background": "#000080"}
)

@app.callback(Output(component_id='graph-output', component_property='children'),
              [Input(component_id='graph-input', component_property='')])
def render_graph(_):
    return dcc.Graph(
        id='graph-1',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [10, 20, 30, 40,
                                                   50, 60, 70], 'type': 'line', 'name': 'value1'},
                {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [12, 22, 36, 44,
                                                   49, 58, 73], 'type': 'line', 'name': 'value2'}
            ],
            'layout': {
                'title': 'Simple Line Graph',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text'],
                    'size': 18
                },
                'xaxis': {
                    'title': 'Variable name -1',
                    'showspikes': True,
                    'spikedash': 'dot',
                    'spikemode': 'across',
                    'spikesnap': 'cursor',
                },
                'yaxis': {
                    'title': 'Variable name -2',
                    'showspikes': True,
                    'spikedash': 'dot',
                    'spikemode': 'across',
                    'spikesnap': 'cursor'
                },

            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
