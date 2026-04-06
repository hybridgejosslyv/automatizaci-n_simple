from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def obtener_precio_accion(empresa):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(f"https://www.google.com/search?q=precio+accion+{empresa}")
        sleep(4)

        # Nombre de la empresa
        nombre = driver.find_element(By.CSS_SELECTOR, "span.d6Ejqe.aSRlid").text

        # Precio (el div grande con el número)
        precio_elemento = driver.find_element(By.CSS_SELECTOR, "div.nB7Pqb.aSRlid")
        precio = precio_elemento.text.split("\n")[0]  # Solo el número, sin el cambio

        # Ticker y bolsa
        ticker = driver.find_element(By.CSS_SELECTOR, "span.UK5aid.MDvRSc").text

        print(f"Empresa : {nombre}")
        print(f"Ticker  : {ticker}")
        print(f"Precio  : {precio}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

obtener_precio_accion("microsoft")