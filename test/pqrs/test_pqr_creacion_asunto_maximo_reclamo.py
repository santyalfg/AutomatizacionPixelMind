# Fecha creacion: 14/11/2025
# Ultima fecha de modificación: 14/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #34 sobre la creacion PQRS, opcion reclamo , carecteres maximos campo asunto

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


def test_creacion_pqrs_reclamo_campo_asunto_maximo_caracteres(driver, request):
    """Caso #34: Creacion PQRS, opcion reclamo , carecteres maximos campo asunto"""

    pqrs = PQRSPage(driver)
    pqrs.abrir_pagina("http://localhost:5173")

    

    driver.save_screenshot("reportes/01_pagina_cargada.png")

    pqrs.llenar_formulario(
        tipo="RECLAMO",
        asunto="Solicitud de información de servicios fdsfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        descripcion="Deseo conocer los servicios disponibles para clientes nuevos.",
        nombre="David Santiago Alfonso",
        email="david@test.com",
        archivo_path= None
    )
    driver.save_screenshot("reportes/02_formulario_lleno.png")

    pqrs.enviar_formulario()
    time.sleep(3)
    driver.save_screenshot("reportes/03_envio_realizado.png")

    # Aquí verificamos el mensaje de error
    mensaje_error = pqrs.obtener_mensaje_error()  # <-- método implementado en PQRSPage
    driver.save_screenshot("reportes/04_resultado.png")

    # Aserción: debe mostrar un mensaje indicando que el archivo no es válido
    assert any(
        texto in mensaje_error.lower()
        for texto in ["archivo no válido", "formato inválido", "error al radicar la solicitud", "error en archivo"]
    ), f"Error: No se mostró mensaje de archivo inválido. Texto recibido: {mensaje_error}"
