from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import urllib3 # urllib3 es un cliente HTTP potente y fácil de usar para Python.
import re # Expresiones regulares 
import time
import pandas as pd

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# indicamos la URL de la página web a la que queremos acceder:
url = 'https://www.filmaffinity.com/es/main.html'
# el objeto driver nos va a permitir alterar el estado del la página
driver.get(url)

elements_by_tag = driver.find_elements(By.TAG_NAME,'button')
elements_by_class_name = driver.find_elements(By.CLASS_NAME, 'css-2tkghh')
element_by_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')

boton_aceptar = elements_by_tag[1]
boton_aceptar.click()