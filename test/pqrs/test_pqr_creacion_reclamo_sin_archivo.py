# Fecha creacion: 15/11/2025
# Ultima fecha de modificación: 15/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #31 sobre la creacion PQRS ,opción reclamo , datos validos y sin archivos  adjuntos

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


def test_creacion_pqrs_reclamo_sin_archivo(driver, request):
    """Caso #31: Creacion PQRS ,opción reclamo , datos validos y sin archivos  adjuntos"""

    pqrs = PQRSPage(driver)
    pqrs.abrir_pagina("http://localhost:5173")


    driver.save_screenshot("reportes/01_pagina_cargada.png")

    pqrs.llenar_formulario(
        tipo="RECLAMO",
        asunto="Solicitud de información de servicios",
        descripcion="Deseo conocer los servicios disponibles para clientes nuevos.",
        nombre="David Santiago Alfonso",
        email="david@test.com",
        archivo_path= None
    )
    driver.save_screenshot("reportes/02_formulario_lleno.png")

    pqrs.enviar_formulario()
    time.sleep(3)
    driver.save_screenshot("reportes/03_envio_realizado.png")

    mensaje = pqrs.obtener_mensaje_exito()
    driver.save_screenshot("reportes/04_resultado.png")

    assert "¡Éxito!" in mensaje or "radicado" in mensaje, f"Error: no se mostró mensaje de éxito. Texto: {mensaje}"
