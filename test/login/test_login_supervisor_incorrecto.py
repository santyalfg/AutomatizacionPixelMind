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


    """
    CASO DE PRUEBA #8
    Nombre: Inicio de sesion supervisor datos equivocados

    Descripción:
        El sistema debe validar y  NO dar acceso a un usuario tipo supervisor con sus datos equivocados, 
        y debera mostrara la notificacion de inicio en sesión

    Precondiciones:
        - Usario supervisor y contraseña equivocados
    
    Entradas:
        - Username (supervisor)
        - Contraseña (Invalida)
    
    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. Llenar con los datos del usuario (errados)
        3. Dar click en "ingresar"
    Resultados esperados:
        1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
        2. No mostrara ninguna alerta por falta de datos
        3. No dejara ingresar a la siguiente pantalla y mostrara una notificacion de datos errados
    
    Poscondición:
        El sistema NO dejará ingresar al sistema al usuario tipo supervisor
    """