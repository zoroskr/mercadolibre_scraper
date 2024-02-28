import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

url = 'https://www.mercadolibre.com.ar'

keyword = input('Enter content to search: ')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=option)
driver.get(url)



WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#cb1-edit')))\
    .send_keys(keyword)


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'body > header > div > div.nav-area.nav-top-area.nav-center-area > form > button > div')))\
    .click()
    
try:
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.onboarding-cp > div > div > div.andes-tooltip-inner > div > div > div.andes-tooltip__buttons > button.onboarding-cp-button.andes-button.andes-button--transparent.andes-button--small')))\
        .click()
except Exception as e:
    print('No hay captcha')
    

time.sleep(5)


titles = driver.find_elements(By.XPATH, '/html/body/main/div/div[3]/section/ol/li/div/div/div[2]/div[1]/a/h2')

precios = driver.find_elements(By.XPATH, '/html/body/main/div/div[3]/section/ol/li/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]')

links_elements = driver.find_elements(By.XPATH, '/html/body/main/div/div[3]/section/ol/li/div/div/div[2]/div[1]/a')

links = []

for le in links_elements:
    links.append(le.get_attribute('href'))

url_company = []

with open('data_mercadolibre.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'link'])
    for i in range(len(titles)):
        row = [titles[i].text, precios[i].text, links[i]]
        writer.writerow(row)

time.sleep(60)


driver.quit()

