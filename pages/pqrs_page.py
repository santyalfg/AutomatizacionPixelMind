from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PQRSPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores del formulario (usa los nombres reales de los elementos del front)
        self.select_tipo_solicitud = (By.NAME, "tipo_solicitud")
        self.input_asunto = (By.NAME, "asunto")
        self.input_descripcion = (By.NAME, "descripcion")
        self.input_nombre = (By.NAME, "nombre_usuario")
        self.input_email = (By.NAME, "email_usuario")
        self.input_archivo = (By.NAME, "adjunto")
        self.btn_enviar = (By.CSS_SELECTOR, "button[type='submit']")
        self.alert_exito = (By.CLASS_NAME, "alert-success")

    def abrir_pagina(self, url):
        """Abre la página del formulario PQRS y espera a que cargue."""
        self.driver.get(url)
        try:
            # Espera hasta que el campo 'asunto' sea visible (máximo 15s)
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.input_asunto)
            )
            print("Página PQRS cargada correctamente.")
        except TimeoutException:
            print("página PQRS no cargó correctamente dentro del tiempo esperado.")

    def llenar_formulario(self, tipo, asunto, descripcion, nombre, email, archivo_path):
        """Llena el formulario de PQRS con los datos dados."""
        from selenium.webdriver.support.ui import Select

        Select(self.driver.find_element(*self.select_tipo_solicitud)).select_by_value(tipo)
        self.driver.find_element(*self.input_asunto).send_keys(asunto)
        self.driver.find_element(*self.input_descripcion).send_keys(descripcion)
        self.driver.find_element(*self.input_nombre).send_keys(nombre)
        self.driver.find_element(*self.input_email).send_keys(email)

        if archivo_path:
            self.driver.find_element(*self.input_archivo).send_keys(archivo_path)

    def enviar_formulario(self):
        """Hace clic en el botón de envío."""
        self.driver.find_element(*self.btn_enviar).click()

    def obtener_mensaje_exito(self):
        """Devuelve el texto del mensaje de éxito."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.alert_exito)
            )
            return self.driver.find_element(*self.alert_exito).text
        except TimeoutException:
            return " No se encontró mensaje de éxito."

    def obtener_mensaje_error(self):
        """
        Devuelve el texto del mensaje de error mostrado cuando se adjunta
        un archivo inválido o de tamaño no permitido.
        """
        try:
            elemento = self.driver.find_element(
                By.XPATH,
                "//div[contains(@class,'alert') or contains(@class,'error') or contains(text(),'archivo') or contains(text(),'Error')]"
            )
            texto = elemento.text.strip()
            print(f"Mensaje de error detectado: {texto}")
            return texto
        except NoSuchElementException:
            print(" No se encontró mensaje de error en pantalla.")
            return ""
