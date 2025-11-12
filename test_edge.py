
#Automatizacion para poder ver si el navegador o drivers de este funcionan
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pytest
import time


def test_busqueda_google():
    service = Service(executable_path=r"C:\SeleniumDrivers\edgedriver_win64\msedgedriver.exe")

    driver = webdriver.Edge(service=service)
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium con Edge")
    search_box.submit()

    time.sleep(2) 
    
    assert "Selenium" in driver.title

    
    driver.quit()
