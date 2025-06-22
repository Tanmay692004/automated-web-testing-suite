from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def test_login_success():
    options = Options()
    options.add_argument("--headless")  # thank you copilot
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--remote-debugging-port=9222")

  
    driver = webdriver.Chrome(options=options)

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")  #acc to the website
    driver.find_element(By.TAG_NAME, "button").click()
    assert "dashboard" in driver.current_url.lower()

    driver.quit()
