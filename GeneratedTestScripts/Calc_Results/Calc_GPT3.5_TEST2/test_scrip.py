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

# Add the implementation for the remaining test scenarios

if __name__ == "__main__":

    try:
        test_scenario_0()
    except AssertionError as e:
        print("Assertion error in test_scenario_0:", e)

    try:
        test_scenario_1()
    except AssertionError as e:
        print("Assertion error in test_scenario_1:", e)