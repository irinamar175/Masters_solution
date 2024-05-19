from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that user can perform addition operation using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_2 = driver.find_element(By.XPATH, "//button[text()='2']")
    number_2.click()
    operator_plus = driver.find_element(By.XPATH, "//button[text()='+']")
    operator_plus.click()
    number_3 = driver.find_element(By.XPATH, "//button[text()='3']")
    number_3.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '5', f"Result is not 5, actual result: {result}"
    driver.quit()


def test_scenario_1():
    """
    Verify that user can perform subtraction operation using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_6 = driver.find_element(By.XPATH, "//button[text()='6']")
    number_6.click()
    operator_minus = driver.find_element(By.XPATH, "//button[text()='-']")
    operator_minus.click()
    number_4 = driver.find_element(By.XPATH, "//button[text()='4']")
    number_4.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '2', f"Result is not 2, actual result: {result}"
    driver.quit()


def test_scenario_2():
    """
    Verify that user can perform multiplication operation using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_7 = driver.find_element(By.XPATH, "//button[text()='7']")
    number_7.click()
    operator_multiply = driver.find_element(By.XPATH, "//button[text()='*']")
    operator_multiply.click()
    number_8 = driver.find_element(By.XPATH, "//button[text()='8']")
    number_8.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '56', f"Result is not 56, actual result: {result}"
    driver.quit()


def test_scenario_3():
    """
    Verify that user can perform division operation using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_9 = driver.find_element(By.XPATH, "//button[text()='9']")
    number_9.click()
    operator_divide = driver.find_element(By.XPATH, "//button[text()='/']")
    operator_divide.click()
    number_3 = driver.find_element(By.XPATH, "//button[text()='3']")
    number_3.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '3', f"Result is not 3, actual result: {result}"
    driver.quit()


def test_scenario_4():
    """
    Verify that user can calculate power using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_2 = driver.find_element(By.XPATH, "//button[text()='2']")
    number_2.click()
    operator_power = driver.find_element(By.XPATH, "//button[text()'^']")
    operator_power.click()
    number_3 = driver.find_element(By.XPATH, "//button[text()='3']")
    number_3.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '8', f"Result is not 8, actual result: {result}"
    driver.quit()


def test_scenario_5():
    """
    Verify that user can calculate square root using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_9 = driver.find_element(By.XPATH, "//button[text()='9']")
    number_9.click()
    operator_sqrt = driver.find_element(By.XPATH, "//button[text()='sqrt']")
    operator_sqrt.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '3', f"Result is not 3, actual result: {result}"
    driver.quit()


def test_scenario_6():
    """
    Verify that user can clear the display using the calculator
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_5 = driver.find_element(By.XPATH, "//button[text()='5']")
    number_5.click()
    clear_button = driver.find_element(By.XPATH, "//button[text()='C']")
    clear_button.click()
    display = driver.find_element(By.ID, "display").get_attribute("value")
    assert display == '', f"Display is not empty, actual display: {display}"
    driver.quit()


def test_scenario_7():
    """
    Verify that user cannot divide by zero
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_8 = driver.find_element(By.XPATH, "//button[text()='8']")
    number_8.click()
    operator_divide = driver.find_element(By.XPATH, "//button[text()='/']")
    operator_divide.click()
    number_0 = driver.find_element(By.XPATH, "//button[text()='0']")
    number_0.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    alert = Alert(driver)
    assert 'Error' in alert.text, f"Error message not displayed: {alert.text}"
    alert.accept()
    driver.quit()


if __name__ == "__main__":

    try:
        test_scenario_0()
    except AssertionError as e:
        print("Assertion error in test_scenario_0:", e)

    try:
        test_scenario_1()
    except AssertionError as e:
        print("Assertion error in test_scenario_1:", e)

    try:
        test_scenario_2()
    except AssertionError as e:
        print("Assertion error in test_scenario_2:", e)

    try:
        test_scenario_3()
    except AssertionError as e:
        print("Assertion error in test_scenario_3:", e)

    try:
        test_scenario_4()
    except AssertionError as e:
        print("Assertion error in test_scenario_4:", e)

    try:
        test_scenario_5()
    except AssertionError as e:
        print("Assertion error in test_scenario_5:", e)

    try:
        test_scenario_6()
    except AssertionError as e:
        print("Assertion error in test_scenario_6:", e)

    try:
        test_scenario_7()
    except AssertionError as e:
        print("Assertion error in test_scenario_7:", e)