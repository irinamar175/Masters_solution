from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scenario_0():
    """
    Verify that a user can successfully login with valid credentials
    """
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
    assert 'inventory.html' in driver.current_url, 'Login failed!'
    driver.quit()


def test_scenario_1():
    """
    Verify that a user cannot login with invalid credentials
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'invalid_user'
    password = 'invalid_password'
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CSS_SELECTOR, '.error-message-container').text
    assert 'Epic sadface: Username and password do not match any user in this service' in error_message, 'Error message not displayed!'
    driver.quit()


def test_scenario_2():
    """
    Verify that a user cannot login with a locked out account
    """
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
    error_message = driver.find_element(By.CSS_SELECTOR, '.error-message-container').text
    assert 'Epic sadface: Sorry, this user has been locked out.' in error_message, 'Error message not displayed!'
    driver.quit()


def test_scenario_3():
    """
    Verify that a user cannot login with empty username and password fields
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = driver.find_element(By.CSS_SELECTOR, '.error-message-container').text
    assert 'Epic sadface: Username is required' in error_message, 'Error message not displayed!'
    assert 'Epic sadface: Password is required' in error_message, 'Error message not displayed!'
    driver.quit()


def test_scenario_4():
    """
    Verify that the login page displays the list of accepted usernames and password
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    accepted_usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
    accepted_password = 'secret_sauce'
    login_credentials = driver.find_element(By.ID, 'login_credentials').text
    assert all(username in login_credentials for username in accepted_usernames), 'Accepted usernames not displayed!'
    login_password = driver.find_element(By.ID, 'login_credentials').text
    assert accepted_password in login_password, 'Accepted password not displayed!'
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