import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import bs4
import time
from tabulate import tabulate
from bs4 import BeautifulSoup




service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.maxima.lv"
driver.get(url)
time.sleep(2)

find=driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
find.click()
find=driver.find_element(By.LINK_TEXT, "Piedāvājumi")
time.sleep(2)
find=driver.find_element(By.LINK_TEXT, "Visi piedāvājumi")
find.click()
time.sleep(3)

url = "https://www.maxima.lv/cenulideri"
saturs = requests.get(url)
soup = BeautifulSoup(saturs.text, 'html.parser')



span_elements = soup.find_all('span', class_='unit-price')
nosaukums_elements = soup.find_all('div', class_='title')  

data = []


if span_elements:
    
    for span_element, nosaukums_element in zip(span_elements, nosaukums_elements):
        price = span_element.text.strip()
        nosaukums = nosaukums_element.text.strip()
        data.append([price, nosaukums])

    
    print(tabulate(data, headers=["Cena/kg", "Nosaukums"], tablefmt="grid"))
else:
    print("No span elements found on the page.")