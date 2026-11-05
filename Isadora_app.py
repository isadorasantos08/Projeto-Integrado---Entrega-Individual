import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.header("Formalidade vs. Informalidade no Trabalho")
    st.write("Análise estrutural da distribuição dos trabalhadores entre empregos formais e informais filtrados por Setor Econômico.")
    
    # dados simulados para o estudo
    data = {
        'Setor': ['Agropecuária', 'Indústria', 'Serviços', 'Comércio', 'Construção Civil'],
        'Trabalhadores_Formais': [1200000, 4500000, 12000000, 6000000, 2100000],
        'Trabalhadores_Informais': [2800000, 1100000, 5200000, 3800000, 3400000]
    }
    df = pd.DataFrame(data)
    
    setor_sel = st.selectbox("Selecione o Setor Econômico Principal:", options=df['Setor'].unique())
    df_sel = df[df['Setor'] == setor_sel].iloc[0]
    
    c1, c2 = st.columns(2)
    total = df_sel['Trabalhadores_Formais'] + df_sel['Trabalhadores_Informais']
    c1.metric("Trabalho Regularizado (Formal)", f"{df_sel['Trabalhadores_Formais']:,}", f"{(df_sel['Trabalhadores_Formais']/total)*100:.1f}% do setor")
    c2.metric("Trabalho Sub-regularizado (Informal)", f"{df_sel['Trabalhadores_Informais']:,}", f"-{(df_sel['Trabalhadores_Informais']/total)*100:.1f}% do setor", delta_color="inverse")
    
    # Gráfico de barras relativo solicitado pela rubrica
    df_melted = df.melt(id_vars=['Setor'], value_vars=['Trabalhadores_Formais', 'Trabalhadores_Informais'], var_name='Tipo', value_name='Total')
    df_melted['Tipo'] = df_melted['Tipo'].map({'Trabalhadores_Formais': 'Formal', 'Trabalhadores_Informais': 'Informal'})
    
    fig = px.bar(df_melted, x='Setor', y='Total', color='Tipo', title="Proporção de Ocupação Formal vs Informal por Setor", barmode='relative')
    st.plotly_chart(fig, use_container_width=True)
