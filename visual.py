import pandas
from dash import Dash, html, dcc

import plotly.express as px

dataFile = "./finalData.csv"
data = pandas.read_csv(dataFile)
data = data.sort_values(by="date")

app = Dash(__name__)

fig = px.line(data, x="date", y="sales", title="Pink Morsel Sales")


app.layout = html.Div(
    children=[
        html.H1(
            children='Pink Morsel Visual', 
            id="head"
        ),
        
        dcc.Graph(
            id='pinkMorsel',
            figure=fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server()