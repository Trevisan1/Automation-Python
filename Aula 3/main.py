import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# Passo 1: Pegar a cotação do dólar
# abrir o navegador
navegador = webdriver.Chrome()

# entrar no google
navegador.get("https://www.google.com.br/")

# pesquisar a cotação do dolar no google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dólar")

# enter
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


# pegar a cotação do dolar
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)



# Passo 2: Pegar a cotação do euro
# entrar no google
navegador.get("https://www.google.com.br/")

# pesquisar a cotação do euro no google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")

# enter
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


# pegar a cotação do euro
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)



# Passo 3: Pegar a cotação do ouro
# pesquisar cotação do ouro, entrar no site pq é diferente do google
navegador.get("https://www.melhorcambio.com/ouro-hoje")

# pegar cotação do ouro
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)



# Passo 4: Atualizar a base de dados
import pandas as pd

tabela = pd.read_excel(r"C:\Users\felip\OneDrive\Área de Trabalho\Prog\Intensivão de Python\Aula 3\Produtos.xlsx")
print(tabela)


# Passo 5: Recalcular os preços

tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)

# Formulas entre as colunas
tabela['Preço de Compra'] = tabela["Preço Original"] * tabela["Cotação"]

# Formulas entre as colunas
tabela['Preço de Venda'] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)



# Passo 6: Exportar a base de dados

tabela.to_excel("Produtos Novo.xlsx" , index=False)