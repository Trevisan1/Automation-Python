import pyautogui
import pyperclip
import time
import pandas as pd


pyautogui.PAUSE = 1                             #Adiciona delay 

#Passo 1: Entrar no sistema (no nosso caso vai ser entrar no link)


pyautogui.press ("win")
pyautogui.write ("brave")
pyautogui.press ("enter")


pyautogui.hotkey("ctrl", "t")                   #comando, + que 1 tecla
pyperclip.copy("https://docs.google.com/spreadsheets/d/1XgOmqx8A5Hohvo6LSDe04Ki7iUx5X0kG/edit#gid=1634402548") 
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


# site ta carregando
time.sleep(7)                                   #Adiciona delay somente na linha
                                             

#Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta exportar)
pyautogui.click(x=92, y=111)
pyautogui.click(x=254, y=396)
pyautogui.click(x=469, y=398)
pyautogui.sleep(5)
pyautogui.click(x=522, y=446)


#Passo 3: Download da base de dados

pyautogui.click(x=522, y=446)


#Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)



tabela = pd.read_excel(r"C:\Users\felip\OneDrive\Área de Trabalho\Cópia de Vendas - Dez.xlsx")

quantidade = tabela["Quantidade"].sum()

faturamento = tabela["Valor Final"].sum()

print(quantidade)
print(faturamento)



#Passo 5: Entrar no email
#Passo 6: Mandar um email para a diretoria com os indicadores