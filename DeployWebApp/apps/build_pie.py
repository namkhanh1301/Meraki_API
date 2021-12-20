# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import pandas as pd 
import pathlib
import plotly.express as px           

# df = pd.read_csv("data_build_dropdown.csv") 
# app = dash.Dash(__name__) 

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_pie.csv"))

layout = html.Div([

    html.H1('Information about your network with Pie Graph', style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(id='pie_graph')
    ]),

    html.Div([

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options=[
                {'label': 'id', 'value': 'id'},
                {'label': 'organizationId', 'value': 'organizationId'},
                {'label': 'name', 'value': 'name'},
                {'label': 'productTypes', 'value': 'productTypes'},
                {'label': 'timeZone', 'value': 'timeZone'}
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='name',                       #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            # className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            )                                                                           
    ])
])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='pie_graph', component_property='figure'),
    Input(component_id='my_dropdown', component_property='value')
)

def update_pie(column_chosen):
    fig = px.pie(df,names=column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)