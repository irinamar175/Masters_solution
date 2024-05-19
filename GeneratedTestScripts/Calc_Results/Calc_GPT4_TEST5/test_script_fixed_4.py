from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = 'https://sea-lion-app-q6nwz.ondigitalocean.app/sample1'

def setup_driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    return driver

def teardown_driver(driver):
    driver.quit()

def test_calculator_operation(driver, button_sequence, expected_results):
    for button in button_sequence:
        if button.isdigit() or button in ['+', '-', '*', '/', '^', 'sqrt', 'C', '=']:
            driver.find_element(By.XPATH, f"//button[contains(text(), '{button}')]").click()
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert alert_text in expected_results, f"Expected alert text not found. Got: {alert_text}"
    except TimeoutException:
        result = driver.find_element(By.ID, 'display').get_attribute('value')
        assert result in expected_results, f"Expected display to be one of {expected_results} but got {result}"


def test_scenario_0():
    driver = setup_driver()
    test_calculator_operation(driver, ['1', '+', '2', '='], ['3'])
    teardown_driver(driver)

def test_scenario_1():
    driver = setup_driver()
    test_calculator_operation(driver, ['5', '-', '3', '='], ['2'])
    teardown_driver(driver)

def test_scenario_2():
    driver = setup_driver()
    test_calculator_operation(driver, ['4', '*', '2', '='], ['8'])
    teardown_driver(driver)

def test_scenario_3():
    driver = setup_driver()
    test_calculator_operation(driver, ['8', '/', '2', '='], ['4'])
    teardown_driver(driver)

def test_scenario_4():
    driver = setup_driver()
    test_calculator_operation(driver, ['5', '/', '0', '='], ['Cannot divide by zero!'])
    teardown_driver(driver)

def test_scenario_5():
    driver = setup_driver()
    test_calculator_operation(driver, ['9', '+', '1', 'C'], ['', '0'])
    teardown_driver(driver)

def test_scenario_6():
    driver = setup_driver()
    test_calculator_operation(driver, ['9', 'sqrt'], ['3'])
    teardown_driver(driver)

def test_scenario_7():
    driver = setup_driver()
    test_calculator_operation(driver, ['-', '9', 'sqrt'], ['Error'])
    teardown_driver(driver)

def test_scenario_8():
    driver = setup_driver()
    test_calculator_operation(driver, ['2', '^', '3', '='], ['8'])
    teardown_driver(driver)

def test_scenario_9():
    driver = setup_driver()
    driver.find_element(By.XPATH, "//button[contains(text(), '+')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(), '+')]").click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '', 'Display should not accept consecutive operators without numbers in between'
    teardown_driver(driver)

def test_scenario_10():
    driver = setup_driver()
    test_calculator_operation(driver, ['2', '+', '2', '*', '3', '='], ['8'])
    teardown_driver(driver)

if __name__ == "__main__":
    test_scenario_0()
    test_scenario_1()
    test_scenario_2()
    test_scenario_3()
    test_scenario_4()
    test_scenario_5()
    test_scenario_6()
    test_scenario_7()
    test_scenario_8()
    test_scenario_9()
    test_scenario_10()
