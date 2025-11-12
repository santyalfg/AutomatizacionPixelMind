# Fecha creacion: 9/11/2025
# Ultima fecha de modificación: 11/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo es la plantilla de la pagina creacion PQRS de automatizacion para concectar con los test


from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PQRSPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores (Faltantes de FRONT)
        self.btn_registrar = ("", "")   
        self.input_username_register = ("", "")      
        self.input_password_register = ("", "")     
        self.input_paword_2_register = ("", "")
        self.input_email_register = ("", "")
        self.btn_confirm_register = ("", "")        
        self.alerta_error_register = ("", "")        

    #Faltante URL ó ruta de sistema
    def abrir_pagina_registro(self, url):
        """Abre la página del sistema."""
        self.driver.get(url)

    def registro(self, usuario, contrasena, contrasena2, email):
        """Simula el inicio de sesión con las credenciales dadas."""
        self.driver.find_element(*self.btn_registrar).click()
        self.driver.find_element(*self.input_username_register).send_keys(usuario)
        self.driver.find_element(*self.input_password_register).send_keys(contrasena)
        self.driver.find_element(*self.input_paword_2_register).send_keys(contrasena2)
        self.driver.find_element(*self.input_email_register).send_keys(email)
        self.driver.find_element(*self.btn_confirm_register).click()
        pass

    def mensaje_error_visible_register(self):
        """Verifica si aparece una notificación o mensaje de error."""
        try:
            elemento = self.driver.find_element(*self.alerta_error_register)
            return elemento.is_displayed()
        except NoSuchElementException:
            return False
    
    def obtener_texto_error_register(self):
    """Devuelve el texto del mensaje de error si existe."""
    try:
        return self.driver.find_element(*self.alerta_error_register).text
    except:
        return ""

