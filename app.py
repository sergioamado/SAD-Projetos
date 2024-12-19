# Comentei tudo pois é meu primeiro contato com python
# Importa bibliotecas necessárias
import streamlit as st  # Biblioteca para criar interfaces web em Python
import pandas as pd  # Manipulação de dados tabulares
import matplotlib.pyplot as plt  # Criação de gráficos com Matplotlib

# Configuração da tela inicial do Streamlit (layout e título)
st.set_page_config(page_title="Inovação Tecnológica", layout="wide")

# Define o estilo para a tela preta e textos brancos usando HTML/CSS
st.markdown(
    """
    <style>
    body {
        color: white; /* Define a cor do texto como branco */
        background-color: black; /* Define a cor de fundo como preta */
    }
    .stTextInput, .stDataFrame, .stButton > button {
        background-color: #333333; /* Cinza escuro para inputs e botões */
        color: white; /* Texto branco */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff; /* Mantém os títulos em branco */
    }
    </style>
    """,
    unsafe_allow_html=True  # Permite a utilização de HTML direto no Streamlit
)

# Adiciona o cabeçalho principal da página
st.markdown("# 🚀 Inovação Tecnológica no Brasil")

# Carrega o arquivo CSV contendo os dados para análise
df = pd.read_csv('pro-csv-produtos-de-inovacao.csv')  # O arquivo deve conter as colunas especificadas

st.markdown("DADOS TOTAIS")
st.write(df)


# ---------------- Gráfico 1: Tipos de Propriedade Intelectual ----------------
# Adiciona um título para a seção
st.markdown("## 📊 Tipos de Propriedade Intelectual")

# Conta quantos registros existem para cada tipo de propriedade intelectual
tipo_pi = df['tipo_pi'].value_counts()

# Cria o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))  # Define o tamanho do gráfico
ax.bar(tipo_pi.index, tipo_pi.values, color='skyblue')  # Adiciona as barras
ax.set_title("Distribuição dos Tipos de Propriedade Intelectual")  # Título do gráfico
ax.set_xlabel("Tipo de Propriedade Intelectual")  # Rótulo do eixo X
ax.set_ylabel("Quantidade")  # Rótulo do eixo Y
plt.xticks(rotation=45, ha="right")  # Inclina os nomes no eixo X para evitar sobreposição

# Mostra o gráfico no Streamlit
st.pyplot(fig)

# ---------------- Gráfico 2: Distribuição por Grande Área de Conhecimento ----------------
# Adiciona um título para a seção
st.markdown("## 📚 Distribuição por Grande Área do Conhecimento")

# Conta a quantidade de registros em cada grande área de conhecimento
grande_area = df['grande_area_conhecimento'].value_counts()

# Cria o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))  # Define o tamanho do gráfico
ax.bar(grande_area.index, grande_area.values, color='lightgreen')  # Adiciona as barras
ax.set_title("Distribuição por Grande Área de Conhecimento")  # Título do gráfico
ax.set_xlabel("Grande Área de Conhecimento")  # Rótulo do eixo X
ax.set_ylabel("Quantidade")  # Rótulo do eixo Y
plt.xticks(rotation=45, ha="right")  # Inclina os nomes no eixo X para evitar sobreposição

# Mostra o gráfico no Streamlit
st.pyplot(fig)

# ---------------- Gráfico 3: Inovações por Unidade e Tipo de PI ----------------
# Adiciona um título para a seção
st.markdown("## 🏢 Inovações por Unidade e Tipo de PI")

# Agrupa os dados por "centro/unidade" e "tipo_pi" e conta quantos registros existem
unidades = df.groupby(['centro/unidade', 'tipo_pi']).size().reset_index(name='quantidade')

# Loop para criar um gráfico separado para cada "centro/unidade"
for unidade in unidades['centro/unidade'].unique():  # Para cada unidade única
    st.markdown(f"### Unidade: {unidade}")  # Adiciona um subtítulo com o nome da unidade

    # Filtra os dados apenas para a unidade atual
    unidade_data = unidades[unidades['centro/unidade'] == unidade]

    # Cria o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))  # Define o tamanho do gráfico
    ax.bar(unidade_data['tipo_pi'], unidade_data['quantidade'], color='orange')  # Adiciona as barras
    ax.set_title(f"Inovações por Tipo de PI na Unidade: {unidade}")  # Título do gráfico
    ax.set_xlabel("Tipo de PI")  # Rótulo do eixo X
    ax.set_ylabel("Quantidade")  # Rótulo do eixo Y
    plt.xticks(rotation=45, ha="right")  # Inclina os nomes no eixo X para evitar sobreposição

    # Mostra o gráfico no Streamlit
    st.pyplot(fig)
