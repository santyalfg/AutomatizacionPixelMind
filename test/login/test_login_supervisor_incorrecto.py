
# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 11/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #5 sobre el Inicio de sesion supervisor datos equivocados


import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_supervisor_datos_equivocados(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "supervisorQA"
    contrasena = "claveIncorrecta"

    login.iniciar_sesion(usuario, contrasena)

    #Validaciones hasta que se tengan el dashboard
    assert login.mensaje_error_visible(), "No se mostró el mensaje de error esperado."
    assert "Dashboard supervisor" not in driver.title, "El usuario no debería acceder al dashboard."

    pass

