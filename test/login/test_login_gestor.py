# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 11/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #1 sobre el Inicio de sesión gestor con datos correctos


import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_gestor_datos_correctos(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "gestorQA"
    contrasena = "clave_gestor"

    login.iniciar_sesion(usuario, contrasena)

    # Validaciones
    assert "Dashboard Gestor" in driver.title or "gestor" in driver.current_url.lower(), \
    #        
     assert not login.mensaje_error_visible(), "Se mostró una alerta inesperada."

    pass

    