import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import seaborn as sns
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Titanic Dashboard: Understanding Analytics!"
df = sns.load_dataset('titanic')
fig = px.scatter(
df,
x="fare",
y="age",
size="pclass",
color="alive",
hover_name="embark_town",
log_x=True,
size_max=60
)
app.layout = html.Div(children = [
html.H1(children='Titanic Dashboard', className="header-h1"),
html.P(children="A simple dashboard representing the number of people and their age.", className="header-description"),
dcc.Graph(id="fare_vs_age", figure=fig),
#Add interactive callback here
html.H4("Change the value in the text box to see callbacks in action", className="header-description"),
html.Div([
"Input: ",
dcc.Input(id='my-input', value='initial value', type='text', className="header-description")
], className="header-description"),
html.Br(),
html.Div(id='my-output', className="header-description"),
],)
@app.callback(
Output(component_id='my-output', component_property='children'),
Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'
if __name__ == "__main__":
   app.run_server(debug=True)