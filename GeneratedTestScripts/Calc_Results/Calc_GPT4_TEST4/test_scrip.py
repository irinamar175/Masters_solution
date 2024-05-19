from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_operation(driver, button_sequence, expected_result):
    for button in button_sequence:
        if button.isdigit() or button in ['+', '-', '*', '/', '^', 'sqrt', 'C', '=']:
            driver.find_element(By.XPATH, f"//button[contains(text(), '{button}')]").click()
        elif button == 'clear-btn':
            driver.find_element(By.CLASS_NAME, 'clear-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def setup_driver():
    driver = webdriver.Chrome()
    driver.get('https://sea-lion-app-q6nwz.ondigitalocean.app/sample1')
    return driver


def test_scenario_0():
    driver = setup_driver()
    test_calculator_operation(driver, ['1', '+', '2', '='], '3')
    driver.quit()


def test_scenario_1():
    driver = setup_driver()
    test_calculator_operation(driver, ['5', '-', '3', '='], '2')
    driver.quit()


def test_scenario_2():
    driver = setup_driver()
    test_calculator_operation(driver, ['4', '*', '2', '='], '8')
    driver.quit()


def test_scenario_3():
    driver = setup_driver()
    test_calculator_operation(driver, ['8', '/', '2', '='], '4')
    driver.quit()


def test_scenario_4():
    driver = setup_driver()
    test_calculator_operation(driver, ['5', '/', '0', '='], 'Error')
    driver.quit()


def test_scenario_5():
    driver = setup_driver()
    test_calculator_operation(driver, ['9', 'sqrt'], '3')
    driver.quit()


def test_scenario_6():
    driver = setup_driver()
    test_calculator_operation(driver, ['-', '9', 'sqrt'], 'Error')
    driver.quit()


def test_scenario_7():
    driver = setup_driver()
    test_calculator_operation(driver, ['2', '^', '3', '='], '8')
    driver.quit()


def test_scenario_8():
    driver = setup_driver()
    test_calculator_operation(driver, ['9', '5', '+', '4', 'clear-btn'], '')
    driver.quit()


def test_scenario_9():
    driver = setup_driver()
    test_calculator_operation(driver, ['2', '+', '3', '*', '4', '='], '20')
    driver.quit()


def test_scenario_10():
    driver = setup_driver()
    test_calculator_operation(driver, ['0', '0', '3', '+', '2', '='], '5')
    driver.quit()


if __name__ == '__main__':
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
