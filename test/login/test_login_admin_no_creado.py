# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 12/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #8 sobre el incio de sesion administrador datos equivocados  

import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_admin_no_creado(setup):

    driver = setup
    login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = "usuario_nuevo"
    contrasena = "123456"

    login.iniciar_sesion(usuario, contrasena)

    # Validaciones 
    texto_error = login.obtener_texto_error()
    assert "no registrado" in texto_error.lower() or "usuario inexistente" in texto_error.lower(), \
           
    assert "Dashboard" not in driver.title, "El sistema no debe permitir acceso al dashboard."

    pass

"""
    CASO DE PRUEBA #12
    Nombre: Inicio de sesion administrador datos no creado

    Descripción:
        El sistema debe validar y  NO dar acceso a un usuario tipo administrador con sus datos 
        equivocados, y debera mostrara la notificacion de inicio en sesión

    Precondiciones:
        - El usuario no está registrado en el sistema.

    Entradas:
        - Username (usuario no creado)
        - Contraseña (cualquiera)

    Pasos:
        1. Dar click en el botón "Inicio de sesión".
        2. Llenar con los datos del usuario no registrado.
        3. Dar click en "Ingresar".

    Resultados esperados:
        1. El sistema no permite ingresar al dashboard.
        2. Muestra una notificación indicando "usuario no registrado" o similar.
        3. No se muestran alertas por falta de datos.
    
    Poscondición:
        El sistema permanece en la pantalla de inicio de sesión.
    """