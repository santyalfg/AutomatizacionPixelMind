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
    
"""
 CASO DE PRUEBA #14
    Nombre: Inicio de sesion sin contraseña del usuario

    Descripción:
       El sistema debe validar y  No dar acceso a un usuario que ha llenado el formulario sin la contraseña

    Precondiciones:
        Usuario sin contraseña en el formulario de inicio de sesión

    Entradas:
        - Username

    Pasos:
        1. Dar click en el boton "Inicio de sesión"
        2. No llenar el campo de contraseña
        3. Dar click en "ingresar"
    Resultados esperados:
        1. Dejar ingresar a la pantalla del fomulario de inicio de sesion
        2. Debe mostrar la alerta en el campo de contraseña
        3. No dejara ingresar a la siguiente pantalla y mostrara una notificacion de rellear el formulario con 
        todos los datos requeridos
    
    Poscondición:
    El sistema NO dejará ingresar al sistema al usuario y debe mostarar una alerta por falta del username en el 
    formulario de inicio de sesión
"""