from selenium.webdriver.common.by import By

def obtener_precio_accion(driver, consulta):
    try:
        driver.get(f"https://www.google.com/search?q=precio+accion+{consulta}")

        nombre = driver.find_element(By.CSS_SELECTOR, "span.d6Ejqe.aSRlid").text
        precio_elemento = driver.find_element(By.CSS_SELECTOR, "div.nB7Pqb.aSRlid")
        precio = precio_elemento.text.split("\n")[0]
        ticker = driver.find_element(By.CSS_SELECTOR, "span.UK5aid.MDvRSc").text

        return f"{nombre} ({ticker}) | Precio: {precio}"

    except Exception as e:
        return f"No se pudo obtener el precio: {e}"