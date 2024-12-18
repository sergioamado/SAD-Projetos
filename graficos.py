import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Gráfico de Pizza
def grafico_pizza(dados, coluna_analisada):
    # Contar os valores únicos na coluna analisada
    dados_agrupados = dados[coluna_analisada].value_counts()

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(8, 8))  # Aumentar o tamanho do gráfico
    ax.pie(
        dados_agrupados,
        labels=dados_agrupados.index,
        autopct='%1.1f%%',
        startangle=90,
        labeldistance=1.1  # Ajustar a posição dos rótulos para evitar sobreposição
    )
    ax.set_title(f'Distribuição por {coluna_analisada}', fontsize=16)

    # Exibir no Streamlit
    st.pyplot(fig)

# Gráfico de Barras
def grafico_barras(dados, coluna_analisada):
    # Contar os valores únicos na coluna analisada
    dados_agrupados = dados[coluna_analisada].value_counts()

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 5))  # Tamanho ajustado para barras
    ax.bar(dados_agrupados.index, dados_agrupados.values, color='skyblue')
    ax.set_title(f'Distribuição de {coluna_analisada}', fontsize=14)
    ax.set_xlabel(coluna_analisada, fontsize=12)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.tick_params(axis='x', rotation=45)  # Rotacionar rótulos para melhor visualização

    # Exibir no Streamlit
    st.pyplot(fig)
