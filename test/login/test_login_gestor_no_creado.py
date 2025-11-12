
# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 12/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #3 sobre el Inicio de sesion gestor datos equivocados


import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_gestor_no_creado(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "gestor_nuevo"
    contrasena = "123456"

    login.iniciar_sesion(usuario, contrasena)

    
    # Validaciones 
    texto_error = login.obtener_texto_error()
    assert "no registrado" in texto_error.lower() or "usuario inexistente" in texto_error.lower(), \
           
    assert "Dashboard" not in driver.title, "El sistema no debe permitir acceso al dashboard."

    pass

