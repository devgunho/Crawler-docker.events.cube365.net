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
datalist = soup.find_all('div',{'class':'agendaInfo'})
print(len(datalist))
driver.quit()