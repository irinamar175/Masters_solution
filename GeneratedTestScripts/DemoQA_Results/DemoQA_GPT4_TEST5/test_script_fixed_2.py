from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_scenario_0():
    """
    Submit form with all valid inputs
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.XPATH, '//label[text()="Male"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    driver.execute_script("document.getElementById('dateOfBirthInput').value='15 May 1995';")
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//label[text()="Sports"]').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, Anytown, USA')
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR')
    driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi')
    driver.find_element(By.ID, 'react-select-4-input').send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    driver.quit()


def test_scenario_1():
    """
    Submit form with missing required fields
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'submit').click()
    errors = driver.find_elements(By.CLASS_NAME, 'was-validated')
    assert len(errors) > 0, 'Form should display errors for missing required fields'
    driver.quit()


def test_scenario_2():
    """
    Submit form with invalid email format
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe')
    driver.find_element(By.XPATH, '//label[text()="Male"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    driver.execute_script("document.getElementById('dateOfBirthInput').value='15 May 1995';")
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//label[text()="Sports"]').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, Anytown, USA')
    driver.find_element(By.ID, 'state').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "NCR")]').click()
    driver.find_element(By.ID, 'city').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "Delhi")]').click()
    driver.find_element(By.ID, 'submit').click()
    email_error = driver.find_element(By.ID, 'userEmail').get_attribute('validationMessage')
    assert 'Please include an "@" in the email address' in email_error, 'Form should display an error for invalid email format'
    driver.quit()


def test_scenario_3():
    """
    Submit form with invalid mobile number
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.XPATH, '//label[text()="Male"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys('12345')
    driver.execute_script("document.getElementById('dateOfBirthInput').value='15 May 1995';")
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//label[text()="Sports"]').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, Anytown, USA')
    driver.find_element(By.ID, 'state').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "NCR")]').click()
    driver.find_element(By.ID, 'city').click()
    driver.find_element(By.XPATH, '//div[contains(text(), "Delhi")]').click()
    driver.find_element(By.ID, 'submit').click()
    mobile_error = driver.find_element(By.ID, 'userNumber').get_attribute('validationMessage')
    assert 'Please fill out this field.' in mobile_error, 'Form should display an error for invalid mobile number'
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
