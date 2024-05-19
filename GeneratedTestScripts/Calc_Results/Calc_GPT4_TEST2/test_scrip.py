from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_operations():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")

    # Basic Addition
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '3', 'Addition result is incorrect'

    # Basic Subtraction
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '2', 'Subtraction result is incorrect'

    # Basic Multiplication
    driver.find_element(By.XPATH, "//button[text()='4']").click()
    driver.find_element(By.XPATH, "//button[text()='*']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '8', 'Multiplication result is incorrect'

    # Basic Division
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '4', 'Division result is incorrect'

    # Division by Zero
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert 'Error' in result, 'Division by zero should result in an error'

    # Clear Display
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '', 'Clear display should result in an empty display'

    # Square Root of Positive Number
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '3', 'Square root calculation is incorrect'

    # Square Root of Negative Number
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert 'Error' in result, 'Square root of negative number should result in an error'

    # Exponentiation
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='^']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '8', 'Exponentiation result is incorrect'

    # Invalid Operation Sequence
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert 'Error' in result, 'Invalid operation should result in an error'

    driver.quit()

if __name__ == '__main__':
    test_calculator_operations()