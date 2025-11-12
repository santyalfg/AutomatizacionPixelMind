import pytest
from pages.login_page import LoginPage

@pytest.mark.regresion
def test_inicio_sesion_sin_username(setup):


driver = setup
login = LoginPage(driver)

    login.abrir_pagina("URL_DEL_SISTEMA")

    usuario = ""
    contrasena = "clave_sin_usuario"

    login.iniciar_sesion(usuario, contrasena)

    #Validaciones        
     assert not login.mensaje_error_visible(), "Se mostró una alerta."

    pass

"""
 CASO DE PRUEBA #13
    Nombre: Inicio de sesion sin nombre de usuario

    Descripción:
        El sistema debe validar y  No dar acceso a un usuario que ha llenado el formulario sin el 
        username 

    Precondiciones:
        - Usuario sin un username
        - Usuario no registrado

    Entradas:
        - Contraseña (cualqueria)

    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. No llenar el campo de usuario
        3. Dar click en "ingresar"
    Resultados esperados:
        1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
        2. Debe mostrar la alerta en el campo de username 
        3. No dejara ingresar a la siguiente pantalla y mostrara una notificacion de rellear el formulario con
        todos los datos requeridos
    
    Poscondición:
        El sistema NO dejará ingresar al sistema al usuario y debe mostarar una alerta por falta del username 
        en el formulario de inicio de sesión
"""
