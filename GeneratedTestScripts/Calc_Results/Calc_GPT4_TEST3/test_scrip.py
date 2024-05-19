from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scenario_0():
    """
    Basic Addition
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '3', "Addition result is incorrect"
    driver.quit()


def test_scenario_1():
    """
    Basic Subtraction
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '2', "Subtraction result is incorrect"
    driver.quit()


def test_scenario_2():
    """
    Basic Multiplication
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='4']").click()
    driver.find_element(By.XPATH, "//button[text()='*']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '8', "Multiplication result is incorrect"
    driver.quit()


def test_scenario_3():
    """
    Basic Division
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '4', "Division result is incorrect"
    driver.quit()


def test_scenario_4():
    """
    Division by Zero
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert 'Error' in result or result == 'Infinity', "Division by zero should result in an error or Infinity"
    driver.quit()


def test_scenario_5():
    """
    Clear Display
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='C']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '', "Clear display should result in an empty display"
    driver.quit()


def test_scenario_6():
    """
    Square Root of Positive Number
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '3', "Square root of 9 should be 3"
    driver.quit()


def test_scenario_7():
    """
    Square Root of Negative Number
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert 'Error' in result, "Square root of negative number should result in an error"
    driver.quit()


def test_scenario_8():
    """
    Exponentiation
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='^']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '8', "Exponentiation result is incorrect"
    driver.quit()


def test_scenario_9():
    """
    Invalid Operator Sequence
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result == '', "Invalid operator sequence should not be allowed or should show an error"
    driver.quit()


def test_scenario_10():
    """
    Multiple Operations
    """
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='*']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    result = driver.find_element(By.ID, "display").get_attribute('value')
    assert result in ['8', '12'], "Multiple operations result is incorrect"
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

    try:
        test_scenario_8()
    except AssertionError as e:
        print("Assertion error in test_scenario_8:", e)

    try:
        test_scenario_9()
    except AssertionError as e:
        print("Assertion error in test_scenario_9:", e)

    try:
        test_scenario_10()
    except AssertionError as e:
        print("Assertion error in test_scenario_10:", e)