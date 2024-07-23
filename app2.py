from dash import Dash, dash_table, dcc, callback, Output, Input, html
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import json
import plotly.graph_objects as go
import numpy as np

# Carregar o dataset
df_gapminder = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Layout da aplicação
app.layout = html.Div([
    dmc.Container([
        dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
        dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ['pop', 'lifeExp', 'gdpPercap']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
        dmc.Grid([
            dmc.Col([
                dash_table.DataTable(data=df_gapminder.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
            ], span=6),
            dmc.Col([
                dcc.Graph(figure={}, id='graph-placeholder')
            ], span=6),
        ]),
    ], fluid=True),

    html.Div([
        dcc.Dropdown(
            ["Coderre", "Joly", "Bergeron"], id="candidate-select", value="Joly"
        ),
        dcc.Graph(id="new-data-graph"),
    ]),

    html.Div([
        dcc.Graph(id='basic-interactions', figure={}),
    ]),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Pre(id='hover-data', style={'border': 'thin lightgrey solid', 'overflowX': 'scroll'})
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style={'border': 'thin lightgrey solid', 'overflowX': 'scroll'}),
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Selection Data**

                Choose the lasso or rectangle tool in the graph's menu
                bar and then select points in the graph.

                Note that if `layout.clickmode = 'event+select'`, selection data also
                accumulates (or un-accumulates) selected data if you hold down the shift
                button while clicking.
            """),
            html.Pre(id='selected-data', style={'border': 'thin lightgrey solid', 'overflowX': 'scroll'}),
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """),
            html.Pre(id='relayout-data', style={'border': 'thin lightgrey solid', 'overflowX': 'scroll'}),
        ], className='three columns')
    ]),

    html.Div([
        dcc.Graph(id='marimekko-chart', figure={}),
        html.Div([
            dcc.Markdown("### South Values"),
            dcc.Slider(id='south-slider-0', min=0, max=100, step=1, value=50, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='south-slider-1', min=0, max=100, step=1, value=80, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='south-slider-2', min=0, max=100, step=1, value=60, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='south-slider-3', min=0, max=100, step=1, value=70, marks={i: str(i) for i in range(0, 101, 10)}),
        ]),
        html.Div([
            dcc.Markdown("### North Values"),
            dcc.Slider(id='north-slider-0', min=0, max=100, step=1, value=50, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='north-slider-1', min=0, max=100, step=1, value=20, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='north-slider-2', min=0, max=100, step=1, value=40, marks={i: str(i) for i in range(0, 101, 10)}),
            dcc.Slider(id='north-slider-3', min=0, max=100, step=1, value=30, marks={i: str(i) for i in range(0, 101, 10)}),
        ]),
        html.Button('Update Marimekko Chart', id='update-marimekko-btn', n_clicks=0)
    ])
])

# Callback para atualizar o gráfico
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df_gapminder, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Dados para o segundo gráfico
df_election = px.data.election()[:20]

# Callback para atualizar o segundo gráfico
@callback(Output("new-data-graph", "figure"), Input("candidate-select", "value"))
def update_figure(value):
    fig = px.bar(df_election, x="district", y=value)
    return fig

# Dados para o terceiro gráfico de barras interativo
df_bars = pd.DataFrame({
    "x": [1, 2, 1, 2],
    "y": [1, 2, 3, 4],
    "customdata": [1, 2, 3, 4],
    "fruit": ["apple", "apple", "orange", "orange"]
})

# Callback para atualizar o terceiro gráfico de barras interativo
@callback(
    Output('basic-interactions', 'figure'),
    Input('basic-interactions', 'hoverData'),
    Input('basic-interactions', 'clickData'),
    Input('basic-interactions', 'selectedData'),
    Input('basic-interactions', 'relayoutData'))
def display_basic_interactions(hoverData, clickData, selectedData, relayoutData):
    fig = px.bar(df_bars, x="x", y="y", color="fruit", custom_data=["customdata"])
    fig.update_layout(clickmode='event+select')
    return fig

# Callback para o gráfico Marimekko
@callback(
    Output('marimekko-chart', 'figure'),
    Input('update-marimekko-btn', 'n_clicks'),
    Input('south-slider-0', 'value'),
    Input('south-slider-1', 'value'),
    Input('south-slider-2', 'value'),
    Input('south-slider-3', 'value'),
    Input('north-slider-0', 'value'),
    Input('north-slider-1', 'value'),
    Input('north-slider-2', 'value'),
    Input('north-slider-3', 'value'))
def update_marimekko(n_clicks, south0, south1, south2, south3, north0, north1, north2, north3):
    labels = ["apples", "oranges", "pears", "bananas"]
    widths = np.array([10, 20, 20, 50])
    data = {
        "South": [south0, south1, south2, south3],
        "North": [north0, north1, north2, north3]
    }

    fig_marimekko = go.Figure()
    for key in data:
        fig_marimekko.add_trace(go.Bar(
            name=key,
            y=data[key],
            x=np.cumsum(widths) - widths,
            width=widths,
            offset=0,
            customdata=np.transpose([labels, widths * np.array(data[key])]),
            texttemplate="%{y} x %{width} =<br>%{customdata[1]}",
            textposition="inside",
            textangle=0,
            textfont_color="white",
            hovertemplate="<br>".join([
                "label: %{customdata[0]}",
                "width: %{width}",
                "height: %{y}",
                "area: %{customdata[1]}",
            ])
        ))

    fig_marimekko.update_xaxes(
        tickvals=np.cumsum(widths) - widths / 2,
        ticktext=["%s<br>%d" % (l, w) for l, w in zip(labels, widths)]
    )

    fig_marimekko.update_xaxes(range=[0, 100])
    fig_marimekko.update_yaxes(range=[0, 100])

    fig_marimekko.update_layout(
        title_text="Marimekko Chart",
        barmode="stack",
        uniformtext=dict(mode="hide", minsize=10),
    )

    return fig_marimekko

@callback(
    Output('hover-data', 'children'),
    Input('basic-interactions', 'hoverData'))
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

@callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

@callback(
    Output('selected-data', 'children'),
    Input('basic-interactions', 'selectedData'))
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)

@callback(
    Output('relayout-data', 'children'),
    Input('basic-interactions', 'relayoutData'))
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
