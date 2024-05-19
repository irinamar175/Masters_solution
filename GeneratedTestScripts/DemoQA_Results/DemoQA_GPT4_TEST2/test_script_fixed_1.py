from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os


def test_submit_form_with_all_valid_inputs():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'gender-radio-1')))
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'gender-radio-1'))
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1995', Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    file_path = os.path.abspath('path/to/image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St')
    state_input = driver.find_element(By.ID, 'react-select-3-input')
    state_input.send_keys('NCR', Keys.ENTER)
    city_input = driver.find_element(By.ID, 'react-select-4-input')
    city_input.send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-title')))
    assert 'Thanks for submitting the form' in driver.find_element(By.CSS_SELECTOR, 'div.modal-title').text
    driver.quit()


def test_submit_form_with_missing_required_fields():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'submit').click()
    errors = driver.find_elements(By.CLASS_NAME, 'was-validated')
    assert len(errors) > 0, 'Error: Required fields are not validated properly.'
    driver.quit()


def test_submit_form_with_invalid_email_format():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'gender-radio-1')))
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'gender-radio-1'))
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1995', Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    file_path = os.path.abspath('path/to/image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St')
    state_input = driver.find_element(By.ID, 'react-select-3-input')
    state_input.send_keys('NCR', Keys.ENTER)
    city_input = driver.find_element(By.ID, 'react-select-4-input')
    city_input.send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-title')))
    assert 'Please enter a valid email' in driver.find_element(By.CLASS_NAME, 'invalid-feedback').text
    driver.quit()


def test_submit_form_with_invalid_mobile_number():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'gender-radio-1')))
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'gender-radio-1'))
    driver.find_element(By.ID, 'userNumber').send_keys('12345')
    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.clear()
    date_input.send_keys('15 May 1995', Keys.ENTER)
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    file_path = os.path.abspath('path/to/image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St')
    state_input = driver.find_element(By.ID, 'react-select-3-input')
    state_input.send_keys('NCR', Keys.ENTER)
    city_input = driver.find_element(By.ID, 'react-select-4-input')
    city_input.send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-title')))
    assert 'Please enter a valid mobile number' in driver.find_element(By.CLASS_NAME, 'invalid-feedback').text
    driver.quit()


if __name__ == '__main__':
    test_submit_form_with_all_valid_inputs()
    test_submit_form_with_missing_required_fields()
    test_submit_form_with_invalid_email_format()
    test_submit_form_with_invalid_mobile_number()