import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_add_student_missing_name(driver, login_admin):
    driver.get("http://158.160.87.146:5000/add-user")

    driver.find_element(By.NAME, "age").send_keys("22")
    driver.find_element(By.NAME, "gender").send_keys("М")
    driver.find_element(By.NAME, "date_birthday").send_keys("2021-09-01")
 
    driver.find_element(By.NAME, "is_active").click()

    driver.find_element(By.ID, "add-btn").click()
    time.sleep(2)

    assert "обязательное" in driver.page_source.lower() or "ошибка" in driver.page_source.lower()

@pytest.mark.ui
def test_add_student_invalid_age(driver, login_admin):
    driver.get("http://158.160.87.146:5000/add-user")

    driver.find_element(By.NAME, "name").send_keys("Неверный возраст")
    driver.find_element(By.NAME, "age").send_keys("21.5")
    driver.find_element(By.NAME, "gender").send_keys("М")
    driver.find_element(By.NAME, "date_birthday").send_keys("2021-09-01")
   
    driver.find_element(By.NAME, "is_active").click()

    driver.find_element(By.ID, "add-btn").click()
    time.sleep(2)

    assert "некорректный" in driver.page_source.lower() or "ошибка" in driver.page_source.lower()
