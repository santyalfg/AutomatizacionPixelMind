# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 11/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #7 sobre el Inicio de sesion administrador datos correctos


import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_admin_datos_correctos(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "adminQA"
    contrasena = "clave_admin"

    login.iniciar_sesion(usuario, contrasena)

    # Validaciones
    assert "Dashboard Administrador" in driver.title or "administrador" in driver.current_url.lower(), \
    #        
     assert not login.mensaje_error_visible(), "Se mostró una alerta inesperada."

    pass

