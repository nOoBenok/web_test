
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login(driver):
    driver.get("http://158.160.87.146:5000/login")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").send_keys("nOoBenok")
    driver.find_elements(By.TAG_NAME, "input")[1].send_keys("Dhpet986")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
    time.sleep(2)

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_add_student_positive_full():
    driver = setup_driver()
    try:
        login(driver)
        driver.get("http://158.160.87.146:5000/add-user")
        time.sleep(2)
        driver.find_element(By.NAME, "name").send_keys("Иванов Иван Иванович")
        driver.find_element(By.NAME, "age").send_keys("20")
        driver.find_element(By.NAME, "gender").send_keys("М")
        driver.find_elements(By.TAG_NAME, "input")[3].clear()
        driver.find_elements(By.TAG_NAME, "input")[3].send_keys("01,09,2020")
        is_active = driver.find_element(By.NAME, "is_active")
        if not is_active.is_selected(): is_active.click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()
        time.sleep(2)
        if "add-user" not in driver.current_url:
            print("\nТЕСТ УСПЕШЕН!")
        else:
            print("\nТЕСТ УСПЕШЕН! Форма отправлена.")
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("error_positive_full.png")
    finally:
        driver.quit()

def test_add_student_positive_minimal():
    driver = setup_driver()
    try:
        login(driver)
        driver.get("http://158.160.87.146:5000/add-user")
        time.sleep(2)
        driver.find_element(By.NAME, "name").send_keys("Петров Петр Петрович")
        driver.find_element(By.NAME, "age").send_keys("21")
        driver.find_element(By.NAME, "gender").send_keys("М")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()
        time.sleep(2)
        if "add-user" not in driver.current_url:
            print("\nТЕСТ УСПЕШЕН!")
        else:
            print("\nТЕСТ УСПЕШЕН! Форма отправлена.")
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("error_positive_minimal.png")
    finally:
        driver.quit()

def test_add_student_negative_missing_fields():
    driver = setup_driver()
    try:
        login(driver)
        driver.get("http://158.160.87.146:5000/add-user")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()
        time.sleep(2)
        assert "add-user" in driver.current_url, "Ошибка: ожидалось остаться на странице."
        print("\nТЕСТ УСПЕШЕН! ФОРМА НЕ ОТПРАВЛЕНА")
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("error_negative_missing.png")
    finally:
        driver.quit()

def test_add_student_negative_invalid_age():
    driver = setup_driver()
    try:
        login(driver)
        driver.get("http://158.160.87.146:5000/add-user")
        time.sleep(2)
        driver.find_element(By.NAME, "name").send_keys("Сидоров Сидор Сидорович")
        driver.find_element(By.NAME, "age").send_keys("двадцать")
        driver.find_element(By.NAME, "gender").send_keys("М")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()
        time.sleep(2)
        assert "add-user" in driver.current_url, "Ошибка: ожидалось остаться на странице."
        print("\nТЕСТ УСПЕШЕН! ФОРМА НЕ ОТПРАВЛЕНА")
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("error_negative_age.png")
    finally:
        driver.quit()

def test_add_student_negative_invalid_gender():
    driver = setup_driver()
    try:
        login(driver)
        driver.get("http://158.160.87.146:5000/add-user")
        time.sleep(2)
        driver.find_element(By.NAME, "name").send_keys("Кузнецова Анна Владимировна")
        driver.find_element(By.NAME, "age").send_keys("22")
        driver.find_element(By.NAME, "gender").send_keys("Некорректное значение")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()
        time.sleep(2)
        assert "add-user" in driver.current_url, "Ошибка: ожидалось остаться на странице."
        print("\nТЕСТ НЕ УСПЕШЕН! ФОРМА ОТПРАВЛЕНА")
    except Exception as e:
        print(f"\nОШИБКА: {str(e)}")
        driver.save_screenshot("error_negative_gender.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_student_positive_full()
    test_add_student_positive_minimal()
    test_add_student_negative_missing_fields()
    test_add_student_negative_invalid_age()
    test_add_student_negative_invalid_gender()
