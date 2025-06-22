from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def test_login_success():
    options = Options()
    options.add_argument("--headless")  #uhhh thank you copilot
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123") #acc to the website
    driver.find_element(By.TAG_NAME, "button").click()

    assert "dashboard" in driver.current_url.lower()
    driver.quit()
