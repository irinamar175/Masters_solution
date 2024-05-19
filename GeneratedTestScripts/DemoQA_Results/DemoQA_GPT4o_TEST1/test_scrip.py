from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


def fill_form(driver, input_data):
    driver.find_element(By.ID, 'firstName').send_keys(input_data['firstName'])
    driver.find_element(By.ID, 'lastName').send_keys(input_data['lastName'])
    driver.find_element(By.ID, 'userEmail').send_keys(input_data['email'])
    if input_data['gender']:
        driver.find_element(By.XPATH, f"//label[text()='{input_data['gender']}']").click()
    driver.find_element(By.ID, 'userNumber').send_keys(input_data['mobile'])
    date_of_birth_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_input.click()
    date_of_birth_input.send_keys(Keys.CONTROL + 'a')
    date_of_birth_input.send_keys(Keys.BACKSPACE)
    date_of_birth_input.send_keys(input_data['dateOfBirth'])
    date_of_birth_input.send_keys(Keys.ENTER)
    for subject in input_data['subjects']:
        subject_input = driver.find_element(By.ID, 'subjectsInput')
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)
    for hobby in input_data['hobbies']:
        driver.find_element(By.XPATH, f"//label[text()='{hobby}']").click()
    if input_data['picture']:
        driver.find_element(By.ID, 'uploadPicture').send_keys(input_data['picture'])
    driver.find_element(By.ID, 'currentAddress').send_keys(input_data['currentAddress'])
    if input_data['state']:
        state_input = driver.find_element(By.ID, 'react-select-3-input')
        state_input.send_keys(input_data['state'])
        state_input.send_keys(Keys.ENTER)
    if input_data['city']:
        city_input = driver.find_element(By.ID, 'react-select-4-input')
        city_input.send_keys(input_data['city'])
        city_input.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'submit').click()


def test_scenario_0():
    """
    Submit form with valid data
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' in driver.page_source, 'Form submission failed'
    driver.quit()


def test_scenario_1():
    """
    Submit form with missing required fields
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': '',
        'lastName': '',
        'email': '',
        'gender': '',
        'mobile': '',
        'dateOfBirth': '',
        'subjects': [],
        'hobbies': [],
        'picture': '',
        'currentAddress': '',
        'state': '',
        'city': ''
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_2():
    """
    Submit form with invalid email format
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@invalid',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_3():
    """
    Submit form with invalid mobile number (less than 10 digits)
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '12345',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_4():
    """
    Submit form with invalid mobile number (more than 10 digits)
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '123456789012',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_5():
    """
    Submit form with invalid date of birth format
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': 'invalid date',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_6():
    """
    Submit form with no subjects selected
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': [],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' in driver.page_source, 'Form submission failed'
    driver.quit()


def test_scenario_7():
    """
    Submit form with no hobbies selected
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': [],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' in driver.page_source, 'Form submission failed'
    driver.quit()


def test_scenario_8():
    """
    Submit form with no picture uploaded
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': '',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' in driver.page_source, 'Form submission failed'
    driver.quit()


def test_scenario_9():
    """
    Submit form with no current address
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '',
        'state': 'NCR',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' in driver.page_source, 'Form submission failed'
    driver.quit()


def test_scenario_10():
    """
    Submit form with no state selected
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': '',
        'city': 'Delhi'
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


def test_scenario_11():
    """
    Submit form with no city selected
    """
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form')
    input_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'mobile': '1234567890',
        'dateOfBirth': '15 May 2000',
        'subjects': ['Maths', 'Physics'],
        'hobbies': ['Sports', 'Reading'],
        'picture': 'path/to/picture.jpg',
        'currentAddress': '123 Main St, Springfield',
        'state': 'NCR',
        'city': ''
    }
    fill_form(driver, input_data)
    time.sleep(2)
    assert 'Thanks for submitting the form' not in driver.page_source, 'Form submission should have failed'
    driver.quit()


if __name__ == '__main__':
    try:
        test_scenario_0()
    except AssertionError as e:
        print('Assertion error in test_scenario_0:', e)

    try:
        test_scenario_1()
    except AssertionError as e:
        print('Assertion error in test_scenario_1:', e)

    try:
        test_scenario_2()
    except AssertionError as e:
        print('Assertion error in test_scenario_2:', e)

    try:
        test_scenario_3()
    except AssertionError as e:
        print('Assertion error in test_scenario_3:', e)

    try:
        test_scenario_4()
    except AssertionError as e:
        print('Assertion error in test_scenario_4:', e)

    try:
        test_scenario_5()
    except AssertionError as e:
        print('Assertion error in test_scenario_5:', e)

    try:
        test_scenario_6()
    except AssertionError as e:
        print('Assertion error in test_scenario_6:', e)

    try:
        test_scenario_7()
    except AssertionError as e:
        print('Assertion error in test_scenario_7:', e)

    try:
        test_scenario_8()
    except AssertionError as e:
        print('Assertion error in test_scenario_8:', e)

    try:
        test_scenario_9()
    except AssertionError as e:
        print('Assertion error in test_scenario_9:', e)

    try:
        test_scenario_10()
    except AssertionError as e:
        print('Assertion error in test_scenario_10:', e)

    try:
        test_scenario_11()
    except AssertionError as e:
        print('Assertion error in test_scenario_11:', e)
