from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_success():
    options = Options()
    options.add_argument("--headless")  #thank you copilot 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/")

    wait = WebDriverWait(driver, 10)


    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys("Admin")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123") #acc tot the site

    login_btn = driver.find_element(By.TAG_NAME, "button")
    login_btn.click()

    wait.until(EC.url_contains("dashboard"))

    assert "dashboard" in driver.current_url.lower()
    driver.quit()
