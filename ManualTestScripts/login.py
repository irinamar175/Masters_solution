from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Webpage scenarios
def test_standard_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'standard_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    title_element = driver.find_element(By.CSS_SELECTOR, '.title')
    assert 'Products' in title_element.text, 'Login failed!'
    driver.quit()


def test_locked_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'locked_out_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
    assert 'Epic sadface: Sorry, this user has been locked out.' in error_message, 'Error message not displayed!'
    driver.quit()


def test_problem_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'problem_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    title_element = driver.find_element(By.CSS_SELECTOR, '.title')
    assert 'Products' in title_element.text, 'Login failed!'
    driver.quit()


def test_performance_glitch():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'performance_glitch_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    time.sleep(5)
    title_element = driver.find_element(By.CSS_SELECTOR, '.title')
    assert 'Products' in title_element.text, 'Login failed!'
    driver.quit()

def test_error_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'error_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    title_element = driver.find_element(By.CSS_SELECTOR, '.title')
    assert 'Products' in title_element.text, 'Login failed!'
    driver.quit()


def test_visual_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'visual_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    title_element = driver.find_element(By.CSS_SELECTOR, '.title')
    assert 'Products' in title_element.text, 'Login failed!'
    driver.quit()

#  Additional scenarios
def test_empty():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = ''
    password = ''
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
    assert 'Epic sadface: Username is required' in error_message, 'Error message not displayed!'
    driver.quit()

def test_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'standard_user'
    password = 'invalid_password'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
    assert 'Epic sadface: Username and password do not match any user in this service' in error_message, 'Error message not displayed!'
    driver.quit()

def test_invalid_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'invalid_user'
    password = 'secret_sauce'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
    assert 'Epic sadface: Username and password do not match any user in this service' in error_message, 'Error message not displayed!'
    driver.quit()

if __name__ == "__main__":
    try:
        test_standard_user()
    except AssertionError as e:
        print("Assertion error in test_standard_user:", e)

    try:
        test_locked_user()
    except AssertionError as e:
        print("Assertion error in test_locked_user:", e)

    try:
        test_problem_user()
    except AssertionError as e:
        print("Assertion error in test_problem_user:", e)

    try:
        test_performance_glitch()
    except AssertionError as e:
        print("Assertion error in test_performance_glitch:", e)

    try:
        test_error_user()
    except AssertionError as e:
        print("Assertion error in test_error_user:", e)

    try:
        test_visual_user()
    except AssertionError as e:
        print("Assertion error in test_visual_user:", e)

    try:
        test_empty()
    except AssertionError as e:
        print("Assertion error in test_empty:", e)
    try:
        test_invalid_password()
    except AssertionError as e:
        print("Assertion error in test_invalid_password:", e)
    try:
        test_invalid_username()
    except AssertionError as e:
        print("Assertion error in test_invalid_username:", e)
