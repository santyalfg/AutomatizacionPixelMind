from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores (Faltantes de FRONT)
        self.btn_inicio_sesion = ("", "")  
        self.input_username = ("", "")      
        self.input_password = ("", "")     
        self.btn_ingresar = ("", "")        
        self.alerta_error = ("", "")        

    def abrir_pagina(self, url):
        """Abre la página del sistema."""
        self.driver.get(url)

    def iniciar_sesion(self, usuario, contrasena):
        """Simula el inicio de sesión con las credenciales dadas."""
        self.driver.find_element(*self.btn_inicio_sesion).click()
        self.driver.find_element(*self.input_username).send_keys(usuario)
        self.driver.find_element(*self.input_password).send_keys(contrasena)
        self.driver.find_element(*self.btn_ingresar).click()
        pass

    def mensaje_error_visible(self):
        """Verifica si aparece una notificación o mensaje de error."""
        try:
            elemento = self.driver.find_element(*self.alerta_error)
            return elemento.is_displayed()
        except NoSuchElementException:
            return False
    
    def obtener_texto_error(self):
    """Devuelve el texto del mensaje de error si existe."""
    try:
        return self.driver.find_element(*self.alerta_error).text
    except:
        return ""

