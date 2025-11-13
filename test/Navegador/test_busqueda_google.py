import pytest
import time

@pytest.mark.usefixtures("setup")
class TestBusquedaGoogle:

    def test_busqueda_google(self):
        driver = self.driver

        # Paso 1: Abrir Google
        driver.get("https://www.google.com")
        driver.save_screenshot("screenshots/test_busqueda_google_paso1_pagina_google.png")
        time.sleep(1)

        # Paso 2: Escribir “Selenium” en la barra de búsqueda
        caja_busqueda = driver.find_element("name", "q")
        caja_busqueda.send_keys("Selenium")
        driver.save_screenshot("screenshots/test_busqueda_google_paso2_ingreso_palabra.png")
        time.sleep(1)

        # Paso 3: Enviar la búsqueda
        caja_busqueda.submit()
        time.sleep(2)
        driver.save_screenshot("screenshots/test_busqueda_google_paso3_resultados.png")

        # Verificar que aparece Selenium en los resultados
        assert "Selenium" in driver.title
