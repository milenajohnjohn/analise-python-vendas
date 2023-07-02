# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configurando o matplotlib
plt.style.use('ggplot')

# Criando um conjunto de dados fictício de vendas de produtos
np.random.seed(0)
num_entradas = 1000
df = pd.DataFrame({
    'Data': pd.date_range(start='1/1/2022', periods=num_entradas),
    'Produto': np.random.choice(['Produto A', 'Produto B', 'Produto C'], num_entradas),
    'Vendas': np.random.randint(1, 100, num_entradas),
    'Custo': np.random.randint(50, 70, num_entradas),
})
df['Lucro'] = df['Vendas'] - df['Custo']

# Salvando o DataFrame como um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)

# Carregando os dados do arquivo CSV
df = pd.read_csv('dados_vendas.csv')

# Verificando as primeiras linhas do DataFrame
print(df.head())

# Verificando a existência de valores faltantes
print(df.isnull().sum())

# Descrevendo o conjunto de dados
print(df.describe())

# Verificando a distribuição das vendas
sns.histplot(df['Vendas'], bins=30, kde=False)
plt.show()

# Verificando a distribuição do lucro
sns.histplot(df['Lucro'], bins=30, kde=False)
plt.show()

# Verificando a relação entre vendas e lucro
sns.scatterplot(x='Vendas', y='Lucro', data=df)
plt.show()

# Verificando as vendas médias por produto
media_vendas_produto = df.groupby('Produto')['Vendas'].mean()
print(media_vendas_produto)

# Visualizando as vendas médias por produto
sns.barplot(x=media_vendas_produto.index, y=media_vendas_produto.values)
plt.show()
