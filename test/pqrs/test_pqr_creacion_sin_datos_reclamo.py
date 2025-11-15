# Fecha creacion: 15/11/2025
# Ultima fecha de modificación: 15/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #36 sobre la creacion PQRS, opcion reclamo , sin datos 

import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.pqrs_page import PQRSPage


@pytest.fixture
def driver():
    
    options = Options()
    options.add_argument("--start-maximized")

    service = Service("C:\\SeleniumDrivers\\edgedriver_win64\\msedgedriver.exe")

    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_creacion_pqrs_reclamo_campo_descripcion_maximo_caracteres(driver, request):
    """Caso #36: Creacion PQRS, opcion reclamo , sin datos  """

    pqrs = PQRSPage(driver)
    pqrs.abrir_pagina("http://localhost:5173")

    

    driver.save_screenshot("reportes/01_pagina_cargada.png")

    
    pqrs.enviar_formulario()
    time.sleep(3)
    driver.save_screenshot("reportes/03_envio_realizado.png")

    # Aquí verificamos el mensaje de error
    mensaje_error = pqrs.obtener_errores_campos_obligatorios()
    driver.save_screenshot("reportes/04_resultado.png")

    # Aserción: debe mostrar un mensaje indicando que faltan campos
    assert any(
    palabra in mensaje_error.lower()
    for palabra in ["oblig", "requer", "campo"]
), f"No se mostraron mensajes de campos obligatorios: {mensaje_error}"
