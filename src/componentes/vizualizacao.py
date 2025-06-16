import plotly.graph_objects as go

def plotar_funil(df_leads):
    # Etapas do funil de vendas, altere aqui caso necessário
    etapas = ['Lead', 'Qualificação', 'Proposta', 'Negociação', 'Fechamento Ganho']
    
    valores = [df_leads[df_leads['etapa_funil'] == etapa].shape[0] for etapa in etapas]

    fig = go.Figure(go.Funnel(
        y = etapas,
        x = valores,
        textposition = "inside",
        textinfo = "value+percent initial",
        opacity = 0.65, marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
        "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
        connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )

    fig.update_layout(title_text="Funil de Vendas")
    fig.show()

def plotar_valor_por_etapa(df_leads):
    valor_por_etapa = df_leads.groupby('etapa_funil')['valor_estimado'].sum().reset_index()

    fig = go.Figure(go.Bar(
        x=valor_por_etapa['etapa_funil'],
        y=valor_por_etapa['valor_estimado'],
        text=valor_por_etapa['valor_estimado'],
        textposition='auto',
    ))

    fig.update_layout(title_text="Valor Estimado por Etapa do Funil",
                      xaxis_title="Etapa do Funil",
                      yaxis_title="Valor Estimado (R$)")
    fig.show()