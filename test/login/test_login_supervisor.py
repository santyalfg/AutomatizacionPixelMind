import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_supervisor_datos_correctos(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "supervisorQA"
    contrasena = "clave_supervisor"

    login.iniciar_sesion(usuario, contrasena)

    # Validaciones
    assert "Dashboard Supervisor" in driver.title or "supervisor" in driver.current_url.lower(), \
    #        
     assert not login.mensaje_error_visible(), "Se mostró una alerta inesperada."

    pass

    """
    CASO DE PRUEBA #7
    Nombre: Inicio de sesion supervisor datos correctos

    Descripción:
        El sistema debe validar y dar acceso a un usuario tipo supervisor con sus datos
        funcionales y correctos

    Precondiciones:
        - Usario y contraseña funcional
        - Usuario ya registrado tipo supervisor

    Entradas:
        - Username (gestor válido)
        - Contraseña (correcta)

    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. Llenar con los datos del usuario (funcional)
        3. Dar click en "ingresar"

    Resultados esperados:
        1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
        2. No mostrara ninguna alerta por los datos
        3. Dejar ingresar al dashboard supervisor del sistema
    
    Poscondición:
        El sistema dejará ingresar al dashboard supervisor al usuario sin ninguna alrta o problema
    """
