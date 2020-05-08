from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

driver.get('https://docker.events.cube365.net/docker/dockercon/agenda')
wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.agendaInfo')))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
agendaTime = soup.find_all('span',{'class':'agendaTime'})
#print(len(agendaTime))
agendaTitle = soup.find_all('p',{'style':'font-family: TTCommons-Medium; font-size: 18px; color:#32353A; line-height: 21px;'})
#print(len(agendaTitle))

for i in range(len(agendaTitle)):
    print(agendaTime[i].text,' | ',agendaTitle[i].text)
driver.quit()