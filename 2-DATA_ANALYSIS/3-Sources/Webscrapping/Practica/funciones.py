from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3 # urllib3 es un cliente HTTP potente y fácil de usar para Python.
import re # Expresiones regulares 
import time
import pandas as pd

def acceso_pag():
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.imdb.com/chart/top/")
    return driver

def pulsar_aceptar(objeto_nav):
    boton_aceptar = WebDriverWait(objeto_nav, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/div/button[2]')))
    boton_aceptar.click()

def extraer_peliculas_top(objeto_nav):

    lista_top = []

    listado_peliculas = WebDriverWait(objeto_nav, 60).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li')))

    for pelicula in listado_peliculas:
        
        try:   
            posicion = pelicula.find_element(By.XPATH, ".//div[contains(@class, 'ipc-signpost__text')]").text
            posicion = int(posicion.replace("#", ""))

            titulo = pelicula.find_element(By.XPATH, ".//h3[contains(@class, 'ipc-title__text')]").text
            anio = int(pelicula.find_element(By.XPATH, ".//span[contains(@class, 'cli-title-metadata-item')][1]").text)
            duracion = pelicula.find_element(By.XPATH, ".//span[contains(@class, 'cli-title-metadata-item')][2]").text
            rating = float(pelicula.find_element(By.XPATH, ".//span[contains(@class, 'ipc-rating-star--rating')]").text.replace(",", "."))

            lista_top.append({"Ranking": posicion,
                            "Título": titulo,
                            "Año": anio,
                            "Duración": duracion,
                            "Rating": rating
                            })
        except Exception as e:
            print(f"Fallo al obtener pelicula: {e}")
            continue

    return lista_top

def convertir_csv(lista_top_peliculas):
    df_peliculas = pd.DataFrame(lista_top_peliculas)

    df_peliculas.to_csv("top_peliculas.csv", sep=";", index=True)
    return df_peliculas

def cerrar_nav(objeto_nav):
    objeto_nav.quit()