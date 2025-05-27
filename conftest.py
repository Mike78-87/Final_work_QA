import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://158.160.87.146:5000"
LOGIN = "admin_ui_test"
PASSWORD = "password123"

@pytest.fixture(scope="session", autouse=True)
def register_admin():
    requests.post(f"{BASE_URL}/api/register", json={"login": LOGIN, "password": PASSWORD})
    time.sleep(1)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_admin(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "login").send_keys(LOGIN)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "add-btn").click()
    time.sleep(1)
