import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Carregando os datasets
df = pd.read_csv('indicadoressegurancapublicauf - Ocorrências.csv', encoding='utf-8')

print(df.head(10))

# Dicionário de mapeamento de nomes completos para siglas
mapa_estados = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM", "Bahia": "BA",
    "Ceará": "CE", "Distrito Federal": "DF", "Espírito Santo": "ES", "Goiás": "GO",
    "Maranhão": "MA", "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG",
    "Pará": "PA", "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI",
    "Rio de Janeiro": "RJ", "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS",
    "Rondônia": "RO", "Roraima": "RR", "Santa Catarina": "SC", "São Paulo": "SP",
    "Sergipe": "SE", "Tocantins": "TO"
}

# Padronizar os estados para maiúsculas e remover espaços extras antes da substituição
df['UF'] = df['UF'].str.strip().map(mapa_estados)


# Verificar se há estados que não foram convertios corretamente
estados_nao_mapeados = df[df['UF'].isnull()]
print(f"Estados que não foram convertidos {estados_nao_mapeados['UF'].unique()}")

# Verificar duplicatas antes da fusão na planilha de indicadores de segurança
print("Duplicatas na planilha de indicadores:", df.duplicated(
    subset=["UF", "Ano", "Tipo Crime", "Mês", "Ocorrências"]).sum())


# Verificar se há valores Nan
print(df.isnull().sum())

# Análise Exploratória de Dados (EDA)

print(df.head(10))

# Distribuição temporal dos homicídios
df_ano_ocorrencias = df.groupby('Ano')['Ocorrências'].sum().plot(kind='line', marker='o', figsize=(10, 6))

plt.title("Evolução das Ocorrências (2015-2022)")
plt.xlabel("Ano")
plt.ylabel("Ocorrências")
plt.grid()
plt.show()

# Quais estados têm os maiores índices de ocorrências

plt.figure(figsize=(10, 6))
sns.barplot(data=df,
            x='UF',
            y='Ocorrências',
            ci=None,
            palette='Blues_r')
plt.title("Total de Ocorrências por Estado (2015-2022)")
plt.xlabel("Estado")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.show()

# Analisar a distribuição dos homicídios por estado

plt.figure(figsize=(10, 6))
sns.boxplot(data=df,
            x='UF',
            y='Ocorrências',
            palette='Set2')
plt.title("Distribuição das Ocorrências por Estado")
plt.xlabel("Estado")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.show()

# Visualizar os crimes mais frequentes
df_crime_counts = df['Tipo Crime'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=df_crime_counts.index,
            y=df_crime_counts.values,
            palette='viridis')
plt.title("Frequência dos Crimes Registrados")
plt.xlabel("Tipo de Crime")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.show()

# Analisar a evolução temporal para cada estado

plt.figure(figsize=(10, 6))
sns.lineplot(data=df,
             x='Ano',
             y='Ocorrências',
             hue='UF',
             ci=None,
             marker='o')
plt.title("Evolução das Ocorrências por Estado (2015-2022)")
plt.xlabel("Ano")
plt.ylabel("Número de Ocorrências")
plt.legend(title="Estado", bbox_to_anchor=(1, 1))
plt.grid()
plt.show()

# Comparação entre os crimes mais comuns por estado

plt.figure(figsize=(10, 6))
sns.countplot(df,
              x='Tipo Crime',
              hue='UF',
              palette='Set1')
plt.title("Crimes mais frequentes por Estado")
plt.xlabel("Tipo de Crime")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.legend(title="Estado", bbox_to_anchor=(1, 1))
plt.show()

# Identificar sazonalidade por mês
plt.figure(figsize=(10, 6))
sns.boxplot(df,
            x='Mês',
            y='Ocorrências',
            palette='coolwarm')
plt.title("Distribuição de Ocorrências por Mês")
plt.xlabel("Mês")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.show()
