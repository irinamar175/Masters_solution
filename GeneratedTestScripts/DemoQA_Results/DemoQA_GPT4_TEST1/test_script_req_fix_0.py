from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
    driver.find_element(By.ID, 'gender-radio-1').click()
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1994')
    date_input.send_keys(Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    Select(driver.find_element(By.ID, 'state')).select_by_visible_text('NCR')
    Select(driver.find_element(By.ID, 'city')).select_by_visible_text('Delhi')
    driver.find_element(By.ID, 'submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'example-modal-sizes-title-lg')))
    assert 'Thanks for submitting the form' in driver.find_element(By.ID, 'example-modal-sizes-title-lg').text
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
    assert len(errors) > 0, 'Error: Required fields are not validated.'
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
    driver.find_element(By.ID, 'gender-radio-1').click()
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1994')
    date_input.send_keys(Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    Select(driver.find_element(By.ID, 'state')).select_by_visible_text('NCR')
    Select(driver.find_element(By.ID, 'city')).select_by_visible_text('Delhi')
    driver.find_element(By.ID, 'submit').click()
    email_field = driver.find_element(By.ID, 'userEmail')
    assert 'Please include an '@' in the email address.' in email_field.get_attribute('validationMessage'), 'Error: Invalid email format not detected.'
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
    driver.find_element(By.ID, 'gender-radio-1').click()
    driver.find_element(By.ID, 'userNumber').send_keys('12345')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1994')
    date_input.send_keys(Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png')
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    Select(driver.find_element(By.ID, 'state')).select_by_visible_text('NCR')
    Select(driver.find_element(By.ID, 'city')).select_by_visible_text('Delhi')
    driver.find_element(By.ID, 'submit').click()
    mobile_field = driver.find_element(By.ID, 'userNumber')
    assert 'Please lengthen this text to 10 characters or more' in mobile_field.get_attribute('validationMessage'), 'Error: Invalid mobile number format not detected.'
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