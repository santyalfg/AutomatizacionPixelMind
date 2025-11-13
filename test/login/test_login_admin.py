# Fecha creacion: 10/11/2025
# Ultima fecha de modificación: 11/11/2025
# Autor: David Santiago Alfonso Guzman
# Descripcion: Este archivo prueba el test case #7 sobre el Inicio de sesion administrador datos correctos


import pytest
import time
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginAdmin:

    def test_inicio_sesion_admin_datos_correctos(self):
        driver = self.driver
        login = LoginPage(driver)

        driver.get("URL")
        driver.save_screenshot("screenshots/paso_1_pantalla_login.png")

        login.ingresar_datos("usuario_demo", "clave123")
        driver.save_screenshot("screenshots/paso_1_pantalla_login.png")

        login.click_ingresar()
        time.sleep(2)
        driver.save_screenshot("screenshots/paso_3_pantalla_dashboard.png")

        assert"Dashboard cliente" in driver.title


