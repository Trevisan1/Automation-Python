from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

email = input("Email: ")
senha = input("Senha: ")


navegador = webdriver.Chrome()
navegador.get("http://mail.google.com/")
navegador.delete_all_cookies()
navegador.find_element ('xpath', '//[@id="identifierId"]').send_keys(email)
navegador.find_element ('xpath', '//[@id="identifierNext"]/div/button/span').click