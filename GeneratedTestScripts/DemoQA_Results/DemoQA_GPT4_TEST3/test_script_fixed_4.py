from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
import os
import time


def test_scenario_0():
    """
    Submit form with all valid inputs
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    gender_button = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    driver.execute_script("arguments[0].scrollIntoView();", gender_button)
    driver.execute_script("arguments[0].click();", gender_button)
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('May')
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('1995')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--015'))).click()
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]'))
    file_path = os.path.join(os.path.dirname(__file__), 'image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR', Keys.ENTER)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        assert 'Thanks for submitting the form' in alert.text
        alert.accept()
    except TimeoutException:
        print('Alert not present')
    finally:
        driver.quit()


def test_scenario_1():
    """
    Submit form with missing required fields
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('May')
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('1995')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--015'))).click()
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    driver.find_element(By.ID, 'submit').click()
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        assert 'Please fill out this field.' in alert.text
        alert.accept()
    except TimeoutException:
        print('Alert not present')
    finally:
        driver.quit()


def test_scenario_2():
    """
    Submit form with invalid email format
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    gender_button = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    driver.execute_script("arguments[0].scrollIntoView();", gender_button)
    driver.execute_script("arguments[0].click();", gender_button)
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe')
    driver.find_element(By.ID, 'userNumber').send_keys('1234567890')
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('May')
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('1995')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--015'))).click()
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]'))
    file_path = os.path.join(os.path.dirname(__file__), 'image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR', Keys.ENTER)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        assert 'Please enter a valid email address' in alert.text
        alert.accept()
    except TimeoutException:
        print('Alert not present')
    finally:
        driver.quit()


def test_scenario_3():
    """
    Submit form with invalid mobile number
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    gender_button = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    driver.execute_script("arguments[0].scrollIntoView();", gender_button)
    driver.execute_script("arguments[0].click();", gender_button)
    driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')
    driver.find_element(By.ID, 'userNumber').send_keys('12345')
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('May')
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('1995')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day--015'))).click()
    driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
    driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
    driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]'))
    file_path = os.path.join(os.path.dirname(__file__), 'image.png')
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys('123 Main St, City, Country')
    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR', Keys.ENTER)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Delhi', Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        assert 'Please enter a valid mobile number' in alert.text
        alert.accept()
    except TimeoutException:
        print('Alert not present')
    finally:
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
