# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import pandas as pd 
import pathlib
import plotly.express as px  

# df = pd.read_csv("data_build_scatter_geo.csv")  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_scatter_geo.csv"))

# app = dash.Dash(__name__)
layout = html.Div([

    html.H1('Information about your network with Scatter Geo', style={'textAlign': 'center', 'font-weight': 'bold'}),

    html.Div(
        dcc.Graph(id = 'scatter_geo')
    ),

    html.Div([
        html.Label(['Choose your OG you want to show all NW locations:'], style={'font-weight': 'bold'}),
        dcc.RadioItems(id = 'my_radioitems',
            options = [
                {'label': x, 'value': x} for x in df['organizationId'].unique()
            ],
            value = df['organizationId'][0]
        )
    ])
])

@app.callback(
    Output(component_id='scatter_geo', component_property='figure'),
    Input(component_id='my_radioitems', component_property='value')
)

def update_scatter_geo(OG_id):
    filt = (df['organizationId'] == OG_id)
    dff = df[filt] 
    fig = px.scatter_geo(dff,
                        locations = 'location',
                        projection= 'orthographic',
                        color = 'name',
                        opacity= .8,
                        hover_name = 'id',
                        hover_data = ['name','timeZone','productTypes']
                        )
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)






   
