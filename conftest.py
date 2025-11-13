# Fecha creacion: 12/11/2025
# Ultima fecha de modificación: 12/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo es el archivo base de la automatizacion y sus procesos
# ================================================================
# COrrer test con capturas "pytest tests/ --html=report.html --self-contained-html -v"
# ================================================================

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pytest_html import extras
import os
import datetime

# Ruta de tu driver Edge
EDGE_DRIVER_PATH = r"C:\SeleniumDrivers\edgedriver_win64\msedgedriver.exe"



# CONFIGURACIÓN DEL DRIVER

@pytest.fixture
def setup():
    service = Service(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# OBTENER ESTADO DEL TEST (PASSED/FAILED)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Permite obtener el resultado (passed/failed) de cada test."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep



# CAPTURA AUTOMÁTICA DE PANTALLAZOS

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, setup):
    """Toma capturas automáticas y las adjunta al reporte HTML."""
    yield
    driver = setup
    test_name = request.node.name

    # Crear carpeta para guardar capturas
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Si falla la prueba
    if request.node.rep_call.failed:
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_FAILED.png")
        driver.save_screenshot(screenshot_path)
        if hasattr(request.node, "report"):
            request.node.report.extra = getattr(request.node.report, "extra", [])
            request.node.report.extra.append(pytest_html.extras.png(screenshot_path))

    # Si pasa la prueba 
    elif request.node.rep_call.passed:
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_PASSED.png")
        driver.save_screenshot(screenshot_path)
        if hasattr(request.node, "report"):
            request.node.report.extra = getattr(request.node.report, "extra", [])
            request.node.report.extra.append(pytest_html.extras.png(screenshot_path))



# CONFIGURACIÓN DE METADATOS PARA EL REPORTE HTML

def pytest_html_report_title(report):
    """Cambia el título del reporte HTML."""
    report.title = "Reporte de Automatización - Inicio de Sesión"

def pytest_html_results_summary(prefix, summary, postfix):
    """Agrega información personalizada al resumen del reporte."""
    prefix.extend([
        "Proyecto: Automatización de Login | ",
        "Tester: David Santiago Alfonso Guzmán | ",
        f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | ",
        "Navegador: Microsoft Edge"
    ])
