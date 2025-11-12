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

    """
    CASO DE PRUEBA #4
    Nombre: Inicio de sesión gestor con datos correctos

    Descripción:
        El sistema debe validar y dar acceso a un usuario tipo gestor con sus datos correctos y funcionales.
        El usuario debe ser previamente creado por el administrador.

    Precondiciones:
        - El usuario gestor existe en el sistema y sus credenciales son válidas.

    Entradas:
        - Username (gestor válido)
        - Contraseña (correcta)

    Pasos:
        1. Dar click en el botón "Inicio de sesión".
        2. Llenar con los datos del usuario (funcional).
        3. Dar click en "Ingresar".

    Resultados esperados:
        1. El sistema no muestra alertas ni errores.
        2. Deja ingresar al dashboard del gestor sin problemas.
    
    Poscondición:
        El sistema muestra el dashboard del gestor autenticado.
    """
