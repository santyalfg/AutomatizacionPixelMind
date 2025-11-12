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

    """
    CASO DE PRUEBA #6
    Nombre: Inicio de sesion gestor datos equivocados

    Descripción:
        El sistema debe validar y  NO dar acceso a un usuario tipo gestor con sus datos equivocados, y debera mostrara 
        la notificacion de inicio en sesión
    Precondiciones:
        - El Usario es tipo gestor y la contraseñaequivocados

    Entradas:
        - Username (usuario no creado)
        - Contraseña (cualquiera)

    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. Llenar con los datos del usuario (errados)
        3. Dar click en "ingresar"

    Resultados esperados:   
    1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
    2. No mostrara ninguna alerta por falta de datos
    3. No dejara ingresar a la siguiente pantalla y mostrara una notificacion de usuario no creado
    
    Poscondición:
        El sistema NO dejará ingresar al sistema al usuario tipo gestor
    """