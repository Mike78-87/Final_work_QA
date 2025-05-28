import pytest
import testit_adapter_pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login_admin(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "login").send_keys(LOGIN)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "add-btn").click()
    time.sleep(1)


#Test.it
def pytest_addoption(parser):
    parser.addoption("--testit", action="store_true", help="Enable TestIT integration")
