# ================================================================
# Fecha creación: 12/11/2025
# Última modificación: 13/11/2025
# Autor: David Santiago Alfonso Guzmán
# Descripción: Archivo base de la automatización y sus procesos
# ================================================================
# Ejecutar pruebas con capturas:
# pytest tests/ --html=report.html --self-contained-html -v
# ================================================================

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pytest_html import extras
import os
import datetime

# Ruta del driver de Edge
EDGE_DRIVER_PATH = r"C:\SeleniumDrivers\edgedriver_win64\msedgedriver.exe"

# Lista global para registrar resultados
test_results = []

# ================================================================
# CONFIGURACIÓN DEL DRIVER
# ================================================================
@pytest.fixture
def setup(request):
    """Inicializa el navegador Edge antes de cada test."""
    service = Service(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    # Crear carpeta para capturas si no existe
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    request.cls.driver = driver
    yield driver
    driver.quit()


# ================================================================
# REGISTRO DE RESULTADOS EN LISTA GLOBAL
# ================================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Registra el resultado final de cada test."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        test_results.append({
            "name": item.name,
            "outcome": rep.outcome,
            "duration": round(rep.duration, 2),
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
        })


# ================================================================
# CAPTURA AUTOMÁTICA DE PANTALLAZOS
# ================================================================
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, setup):
    """Toma capturas automáticas y las adjunta al reporte HTML."""
    yield
    driver = setup
    test_name = request.node.name

    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{datetime.datetime.now().strftime('%H%M%S')}.png")
    driver.save_screenshot(screenshot_path)

    # Adjuntar imagen al reporte HTML
    if hasattr(request.node, "rep_call") and request.node.rep_call:
        if hasattr(request.node.rep_call, "extra"):
            extras_list = request.node.rep_call.extra
        else:
            extras_list = []
        extras_list.append(extras.png(screenshot_path))
        request.node.rep_call.extra = extras_list


# ================================================================
# CONFIGURACIÓN DEL REPORTE HTML
# ================================================================
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
