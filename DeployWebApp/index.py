import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import build_pie, build_bar, build_scatter_geo, build_map_density


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Pie | ', href='/apps/build_pie'),
        dcc.Link('Bar | ', href='/apps/build_bar'),
        dcc.Link('ScatterGeo | ', href='/apps/build_scatter_geo'), 
        dcc.Link('MapDensity', href='/apps/build_map_density')
    ], className="row"),
    html.Div(id='page-content', children=[]) #, pathname = '/apps/build_dropdown' but default it's empty)
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
              
def display_page(pathname):
    if pathname == '/apps/build_pie':
        return build_pie.layout
    if pathname == '/apps/build_bar':
        return build_bar.layout
    if pathname == '/apps/build_scatter_geo':
        return build_scatter_geo.layout
    if pathname == '/apps/build_map_density':
        return build_map_density.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True) 
