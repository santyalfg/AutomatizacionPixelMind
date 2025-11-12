# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 12/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #12 sobre el Inicio de sesion sin contraseña del usuario


import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_sin_pasword(setup):

driver = setup
login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "usernameCualquiera"
    contrasena = ""

    login.iniciar_sesion(usuario, contrasena)

    #Validaciones        
     assert not login.mensaje_error_visible(), "Se mostró una alerta."

    pass
    
