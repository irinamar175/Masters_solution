from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_operations():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")  # Corrected URL

    # Basic Addition
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '3'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '3', 'Addition result is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Basic Subtraction
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '2'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '2', 'Subtraction result is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Basic Multiplication
    driver.find_element(By.XPATH, "//button[text()='4']").click()
    driver.find_element(By.XPATH, "//button[text()='*']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '8'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '8', 'Multiplication result is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Basic Division
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '4'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '4', 'Division result is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Division by Zero
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), 'Error'))
    result = driver.find_element(By.ID, 'display').text
    assert 'Error' in result, 'Division by zero should result in an error'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Clear Display
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()
    result = driver.find_element(By.ID, 'display').text
    assert result == '', 'Clear display should result in an empty display'

    # Square Root of Positive Number
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '3'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '3', 'Square root calculation is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Square Root of Negative Number
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), 'Error'))
    result = driver.find_element(By.ID, 'display').text
    assert 'Error' in result, 'Square root of negative number should result in an error'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Exponentiation
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='^']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), '8'))
    result = driver.find_element(By.ID, 'display').text
    assert result == '8', 'Exponentiation result is incorrect'
    driver.find_element(By.CLASS_NAME, 'clear-btn').click()

    # Invalid Operation Sequence
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.CLASS_NAME, 'equals-btn').click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'display'), 'Error'))
    result = driver.find_element(By.ID, 'display').text
    assert 'Error' in result, 'Invalid operation should result in an error'

    driver.quit()

if __name__ == '__main__':
    test_calculator_operations()