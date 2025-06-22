from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")  # Testable login page

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()

    assert "dashboard" in driver.current_url.lower()
    driver.quit()
