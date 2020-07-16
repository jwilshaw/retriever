import dash
import dash_bootstrap_components as dbc

# Styling default
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Using bootstrap for responsive design
# Need to make sure that boostrap is installed: conda install -c conda-forge dash-bootstrap-components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True
