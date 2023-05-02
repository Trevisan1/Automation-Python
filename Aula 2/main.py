# Passo 1: Importar a base de dados

import pandas as pd                     # Apelido
import plotly.express as px


tabela = pd.read_csv(r"C:\Users\felip\OneDrive\Área de Trabalho\Prog\Intensivão de Python\Aula 2\telecom_users.csv")

# informação que não te ajuda, atrapalha



# Passo 2: Visualizar a base de dados
# Entender as informações que você tem disponível
# Descobrir a cagada da base de dados


# excluir coluna inútil
# tabela = tabela.drog("nome", eixo)                
# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna
tabela = tabela.drop("Unnamed: 0", axis=1)  


# Passo 3: Tratamento de Dados (resolver as cagadas da base de dados)
# informações do tipo correto - ajustar o TotalGasto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# informações vazias

# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna
# colunas completamente vazias -> excluir
tabela = tabela.dropna(how="all", axis=1)

# linhas que tem alguma informação vazia -> excluir
tabela = tabela.dropna(how="any", axis=0)



# Passo 4: Análise inicial dos dados
# como estão os cancelamentos? 26%
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))



# Passo 5: Descobrir os motivos do cancelamento

for coluna in tabela.columns:

    # etapa 1: criar o grafico
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # etapa 2: exibir o grafico
    grafico.show()