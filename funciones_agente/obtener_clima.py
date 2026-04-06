from time import sleep
from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):
    try:
        driver.get(f"https://www.google.com/search?q=clima+{consulta}")
        sleep(4)

        try:
            boton_aceptar = driver.find_element(By.XPATH, "//button[contains(., 'Aceptar')]")
            boton_aceptar.click()
            sleep(2)
        except:
            pass

        # Ciudad
        ciudad = driver.find_element(By.CSS_SELECTOR, "span.d6Ejqe.aSRlid").text

        # Temperatura
        temperatura = driver.find_element(By.CSS_SELECTOR, "div.nB7Pqb.aSRlid").text

        # Descripción (hora y condición)
        descripcion = driver.find_element(By.CSS_SELECTOR, "div.d6Ejqe.aSRlid").text

        return f"{ciudad} | {temperatura} | {descripcion}"

    except Exception as e:
        return f"No se pudo obtener el clima: {e}"