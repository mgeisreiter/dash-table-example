import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd







########### Define your variables ######
myheading = "Best Craft Beers in DC"
mysubheading = "August 2019"
tabtitle = 'python rocks'
filename = 'dc-breweries.csv'
sourceurl = 'https://www.beeradvocate.com/beer/top-rated/us/dc/'
githublink = 'https://github.com/austinlasseter/dash-table-example'

########### Set up the data
df = pd.read_csv(filename)


########### Set up the chart
x_list= df['Beer Name']
y_list=df['Alcohol By Volume (ABV)']
myfavoritecolor = '#33AFFF'
label1 = 'ABV'
mydata = [go.Bar(x=x_list,
                y=y_list,
                name = label1,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = 'Beer',
    xaxis = dict(title = 'Beer Name'),
    yaxis = dict(title = 'ABV'))
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle




########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.Br(),
    dcc.Graph(id = 'figure-1', figure = myfigure),

    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Plotly Dash", href='https://plot.ly/python/pie-charts/')
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
