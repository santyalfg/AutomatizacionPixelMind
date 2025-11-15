# Fecha creacion: 15/11/2025
# Ultima fecha de modificación: 15/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #39 sobre la creacion PQRS ,opcion sugerencias , datos validos , con archivos invalidos

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


def test_creacion_pqrs_sugerencia_con_archivo_invalido(driver, request):
    """Caso #39: Creacion PQRS ,opcion sugerencias , datos validos , con archivos invalidos"""

    pqrs = PQRSPage(driver)
    pqrs.abrir_pagina("http://localhost:5173")

    archivo_path = os.path.abspath("resources/package-lock.json")

    driver.save_screenshot("reportes/01_pagina_cargada.png")

    pqrs.llenar_formulario(
        tipo="SUGERENCIA",
        asunto="Solicitud de información de servicios",
        descripcion="Deseo conocer los servicios disponibles para clientes nuevos.",
        nombre="David Santiago Alfonso",
        email="david@test.com",
        archivo_path=archivo_path
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
