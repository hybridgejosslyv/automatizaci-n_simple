from time import sleep
from selenium import webdriver

# Selenium buscará y descargará el driver adecuado automáticamente
driver = webdriver.Chrome()

driver.get("https://www.google.com")
sleep(2)
driver.get("https://hybridge.education")
sleep(2)
driver.get("https://openai.com")

sleep(5) # Para que no se cierre de inmediato
driver.quit()