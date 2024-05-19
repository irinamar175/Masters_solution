from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    """
    Basic Addition
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['1', '+', '2', '='], ['3'])
    driver.quit()


def test_scenario_1():
    """
    Basic Subtraction
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['5', '-', '3', '='], ['2'])
    driver.quit()


def test_scenario_2():
    """
    Basic Multiplication
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['4', '*', '2', '='], ['8'])
    driver.quit()


def test_scenario_3():
    """
    Basic Division
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['8', '/', '2', '='], ['4'])
    driver.quit()


def test_scenario_4():
    """
    Division by Zero
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['5', '/', '0', '='], ['Cannot divide by zero!'])
    driver.quit()


def test_scenario_5():
    """
    Clear Display
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['9', '+', '1', 'C'], ['', '0'])
    driver.quit()


def test_scenario_6():
    """
    Square Root of Positive Number
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['9', 'sqrt'], ['3'])
    driver.quit()


def test_scenario_7():
    """
    Square Root of Negative Number
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['-', '9', 'sqrt'], ['Error'])
    driver.quit()


def test_scenario_8():
    """
    Exponentiation
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['2', '^', '3', '='], ['8'])
    driver.quit()


def test_scenario_9():
    """
    Invalid Operator Sequence
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[contains(text(), '+')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(), '+')]").click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '', 'Display should not accept consecutive operators without numbers in between'
    driver.quit()


def test_scenario_10():
    """
    Multiple Operations
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    test_calculator_operation(driver, ['2', '+', '2', '*', '3', '='], ['8'])
    driver.quit()


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
