from dash import dcc, callback, Output, Input, html
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import psycopg2
import numpy as np
from dash import Dash
import json

# Conectar ao banco de dados PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="godziny-db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    print("Conexão ao PostgreSQL bem-sucedida")
except psycopg2.Error as e:
    print("Erro ao conectar ao PostgreSQL:", e)
    conn = None

# Função para executar consultas e retornar resultados como DataFrame
def executar_consulta(query):
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                colnames = [desc[0] for desc in cursor.description]
                resultados = cursor.fetchall()
                return pd.DataFrame(resultados, columns=colnames)
        except psycopg2.Error as e:
            print("Erro ao executar a consulta:", e)
    return pd.DataFrame()

queries = {
    "Concluída": """
        SELECT u.nome, SUM(a.carga_horaria * ct.horas_multiplicador) AS horas_totais
        FROM tb_atividade AS a
        JOIN tb_usuario AS u ON u.matricula = a.usuario_id
        JOIN tb_categoria AS ct ON ct.id = a.categoria_id
        WHERE a.status = 'SIMULANDO'
        GROUP BY u.nome
        ORDER BY u.nome;
    """,
    "Em Andamento": """
        SELECT u.nome, SUM(a.carga_horaria * ct.horas_multiplicador) AS horas_totais
        FROM tb_atividade AS a
        JOIN tb_usuario AS u ON u.matricula = a.usuario_id
        JOIN tb_categoria AS ct ON ct.id = a.categoria_id
        WHERE a.status = 'Em Andamnto'
        GROUP BY u.nome
        ORDER BY u.nome;
    """,
    "Não Iniciado": """
        SELECT u.nome, SUM(a.carga_horaria * ct.horas_multiplicador) AS horas_totais
        FROM tb_atividade AS a
        JOIN tb_usuario AS u ON u.matricula = a.usuario_id
        JOIN tb_categoria AS ct ON ct.id = a.categoria_id
        WHERE a.status = 'Não Iniciado'
        GROUP BY u.nome
        ORDER BY u.nome;
    """
}

queries_atividades = {
    "Atividades":"""
    SELECT 
    u.nome, 
    a.titulo AS atividade_titulo,
    a.carga_horaria AS atividade_carga_horaria,
    c.nome AS categoria_nome,
    c.horas_multiplicador AS categoria_horar_multiplicador,
    c.porcentagem_horas_maximas AS categoria_horas_maximas,
    cu.carga_horaria_complementar AS curso_hora,
    a.status AS status,
    (a.carga_horaria * c.horas_multiplicador::FLOAT) AS horas_feitas,
    (c.porcentagem_horas_maximas * cu.carga_horaria_complementar) AS horas_max
    FROM 
        tb_usuario AS u
    JOIN 
        tb_atividade AS a ON u.matricula = a.usuario_id
    JOIN 
        tb_categoria AS c ON a.categoria_id = c.id
    JOIN 
        tb_curso AS cu ON c.curso_id = cu.id
    WHERE 
        u.matricula = 2;
    """
}

queries_categoria = {
    "Categoria": """
    SELECT 
    u.nome, 
    c.nome AS categoria_nome,
    a.status AS status,
    SUM((a.carga_horaria * c.horas_multiplicador::FLOAT)) AS horas_feitas,
    (c.porcentagem_horas_maximas * cu.carga_horaria_complementar) AS horas_max
    FROM 
        tb_usuario AS u
    JOIN 
        tb_atividade AS a ON u.matricula = a.usuario_id
    JOIN 
        tb_categoria AS c ON a.categoria_id = c.id
    JOIN 
        tb_curso AS cu ON c.curso_id = cu.id
    WHERE 
        u.matricula = 2
	GROUP BY 
		horas_max,u.nome,c.nome, a.status;
    """
}

# Executar consultas e armazenar resultados em DataFrames
dataframes = {}
for status, query in queries.items():
    df = executar_consulta(query)
    if not df.empty:
        df['Status'] = status
        dataframes[status] = df
        
dataframes_atividades = {}
for status, query in queries_atividades.items():
    df = executar_consulta(query)
    if not df.empty:
        df['Status'] = status
        dataframes_atividades[status] = df
        
df_cat = {}
for status, query in queries_categoria.items():
    df = executar_consulta(query)
    if not df.empty:
        df['Status'] = status
        df_cat[status] = df


# Combinar todos os DataFrames em um único DataFrame
df_total = pd.concat(dataframes.values(), ignore_index=True)

df_atividades = pd.concat(dataframes_atividades.values(), ignore_index=True)

df_categoria = pd.concat(df_cat.values(), ignore_index=True)

#print("DataFrame combinado:")
#print(df_total)

print("DataFrame atvidades:")
print(df_atividades)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)



styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

@callback(
    Output('hover-data', 'children'),
    Input('exemplo-graph', 'hoverData'))
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@callback(
    Output('click-data', 'children'),
    Input('exemplo-graph', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@callback(
    Output('selected-data', 'children'),
    Input('exemplo-graph', 'selectedData'))
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@callback(
    Output('relayout-data', 'children'),
    Input('exemplo-graph', 'relayoutData'))
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)




fig_pizza = px.pie(df_total, values='horas_totais', names='Status')

#grafico de barras
fig = px.bar(df_total, x="horas_totais", y="nome", color='Status')

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_line_width=20)

#grafico de duas cores se completando
fig_atv = go.Figure()
fig_atv.add_trace(go.Bar(
    y=df_atividades['categoria_nome'],
    x=df_atividades['horas_feitas'],
    name='Horas Feitas',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig_atv.add_trace(go.Bar(
    y=df_atividades['categoria_nome'],
    x=df_atividades['horas_max'],
    name='Horas Máximas',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))

fig_atv.update_layout(barmode='stack', title='Atividades do Usuário', xaxis_title='Horas', yaxis_title='Categorias')

#grafico das horas em porcentagem
df_atividades['porcentagem_feitas'] = (df_atividades['horas_feitas'] / df_atividades['horas_max'] * 100).fillna(0)
df_atividades['porcentagem_nao_feitas'] = df_atividades.apply(
    lambda row: 0 if row['porcentagem_feitas'] > 100 else 100 - row['porcentagem_feitas'],
    axis=1
)

categories = df_atividades['categoria_nome']
feitas = df_atividades['porcentagem_feitas']
nao_feitas = df_atividades['porcentagem_nao_feitas']
atividades = df_atividades['atividade_titulo']  

fig_porc = go.Figure()
fig_porc.add_trace(go.Bar(
    y=categories,
    x=feitas,
    name='Feitas',
    orientation='h',
    marker=dict(color='rgba(38, 24, 74, 0.8)'),
    text=atividades,  # Nome da atividade
    texttemplate='%{text}',  # Exibir texto personalizado
    textposition='inside',  # Posição do texto dentro da barra
    hoverinfo='x+text'  # Mostrar valor do eixo X e texto personalizado ao passar o mouse
))

fig_porc.add_trace(go.Bar(
    y=categories,
    x=nao_feitas,
    name='Não Feitas',
    orientation='h',
    marker=dict(color='rgba(190, 192, 213, 1)'),
    text=[''] * len(categories),  
    hoverinfo='x'
))

fig_porc.update_layout(
    barmode='stack',
    xaxis=dict(
        title='Porcentagem (%)',
        range=[0, 100]
    ),
    yaxis_title='Categoria',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=40, b=80),
    title='Tempo Feito e Não Feito por Categoria'
)

#grafico de linhas total
@app.callback(
    Output("graph_pontos", "figure"), 
    Input("checklist", "value"))
def update_line_chart(statuses):
    filtered_df = df_total[df_total['Status'].isin(statuses)]

    fig = px.scatter(filtered_df, x='horas_totais', y='horas_totais', color='nome', 
                 labels={'usuario': 'Usuário', 'horas_totais': 'Horas Totais'},
                 title='Horas Totais por Status e Usuário')

    fig.update_layout(
        xaxis_title='Usuário',
        yaxis_title='Horas Totais',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=100, r=20, t=70, b=70)
    )
    
    return fig

#feitas/naofeitas
@app.callback(
    Output("graph", "figure"), 
    Input("dropdown-cat", "value"))
def update_bar_chart(day):
    filtered_df=  df_atividades[df_atividades['categoria_nome'].isin(categories)]
    
    fig = px.bar(filtered_df, x='atividade_titulo', y='horas_feitas', 
                 color='horas_max', barmode="group")
    return fig

fig_atv_2 = px.bar(df_atividades, x="horas_feitas", y="categoria_nome",color='atividade_titulo', orientation='h')

#grafico de linha juntos
fig_linha = go.Figure()
fig_linha.add_trace(go.Scatter(x=df_atividades['atividade_titulo'], y=df_atividades['horas_feitas'],
                    marker=dict(color='#0099ff'),
                    name='Horas feitas',
                    xaxis='x2', yaxis='y2'))
fig_linha.add_trace(go.Scatter(x=df_atividades['atividade_titulo'], y=df_atividades['horas_max'],
                    marker=dict(color='#404040'),
                    name='Horas maximas',
                    xaxis='x2', yaxis='y2'))

fig_linha.update_layout(
    title_text = 'Horas Totais',
    margin = {'t':50, 'b':100},
    xaxis = {'domain': [0, .5]},
    xaxis2 = {'domain': [0.6, 1.]},
    yaxis2 = dict(anchor= 'x2', title= 'Horas', range=[0,100])
)

#doublebar
fig_duas = go.Figure()
fig_duas.add_trace(go.Bar(x=df_categoria['categoria_nome'], y=df_categoria['horas_feitas'], xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Horas Feitas'))

fig_duas.add_trace(go.Bar(x=df_categoria['categoria_nome'], y=df_categoria['horas_max'], xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Horas Maximas'))

horas_feitas = df_atividades['horas_max']

fig_duas.update_layout(
    title_text = 'Horas Totais',
    height = 800,
    margin = {'t':75, 'l':50},
    yaxis = {'domain': [0, 1]},
    xaxis2 = {'anchor': 'y2'},
    yaxis2 = dict(anchor= 'x2', title= 'Horas', range=[0,100])
)

#grafico com o dropdown das horas
app.layout = html.Div([
    
    dcc.Dropdown(
        options=[
            {'label': 'Concluídas', 'value': 'Concluída'},
            {'label': 'Em Andamento', 'value': 'Em Andamento'},
            {'label': 'Não Iniciado', 'value': 'Não Iniciado'}
        ],
        id='status-dropdown',
        value='Concluída'
    ),
    dcc.Graph(id='exemplo-graph', figure=fig),
    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style=styles['pre']),
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
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
    ]),
    
    
    
    
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='atividade', figure=fig_atv),
    dcc.Graph(id='graph_pontos'),
    dcc.Checklist(
        id="checklist",
        options=[
            {"label": "Concluída", "value": "Concluída"},
            {"label": "Em Andamento", "value": "Em Andamento"},
            {"label": "Não Iniciado", "value": "Não Iniciado"}
        ],
        value=["Concluída"],
        inline=True
    ),
    dcc.Graph(id='porcentagem', figure=fig_porc),
    dcc.Dropdown(
        id="dropdown-cat",
        options=["Seminário Técnico", "Sat", "Sun"],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
    dcc.Graph(id='histogram',figure=fig_atv_2),
    dcc.Graph(id='linhas_tabela',figure=fig_linha),
    dcc.Graph(id='pizza',figure=fig_pizza),
    dcc.Graph(id='duas',figure=fig_duas)
])

@app.callback(
    Output('bar-chart', 'figure'),
    Input('status-dropdown', 'value')
)
def update_graph(selected_status):
    filtered_df = df_total[df_total['Status'] == selected_status]
    
    if filtered_df.empty:
        fig = px.bar(x=[], y=[], title=f'Nenhum dado disponível para {selected_status}')
    else:
        fig = px.bar(filtered_df, x='nome', y='horas_totais', title=f'Horas Totais {selected_status}')
        fig.update_layout(xaxis_title='Nome', yaxis_title='Horas Totais')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


''' talvez da pra pegar a info da url
from dash import Dash, dcc, html, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    return html.Div([
        html.H3(f'You are on page {pathname}')
    ])


if __name__ == '__main__':
    app.run(debug=True)

'''