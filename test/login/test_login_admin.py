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

        """
    CASO DE PRUEBA #10
    Nombre: Inicio de sesion administrador datos correctos

    Descripción:
        El sistema debe validar y dar acceso a un usuario tipo administrador 
        con sus datos funcionales y correctos

    Precondiciones:
        - Usario y contraseña funcional
        - Usuario ya registrado tipo administrador

    Entradas:
        - Username (administrador válido)
        - Contraseña (correcta)

    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. Llenar con los datos del usuario (funcional)
        3. Dar click en "ingresar"
    Resultados esperados:
        1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
        2. No mostrara ninguna alerta por los datos
        3. Dejar ingresar al dashboard administrador del sistema
    
    Poscondición:
        El sistema dejará ingresar al dashboard administrador al usuario sin ninguna alerta o problema
    """
