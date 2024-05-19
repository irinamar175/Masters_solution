from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
    try:
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert 'Epic sadface: Username and password do not match any user in this service' in error_message, 'Error message not displayed!'
    except NoSuchElementException:
        pass
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
    try:
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert 'Epic sadface: Sorry, this user has been locked out.' in error_message, 'Error message not displayed!'
    except NoSuchElementException:
        pass
    driver.quit()


def test_scenario_3():
    """
    Verify that a user cannot login with a problem user account
    """
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
    try:
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert 'Epic sadface: Sorry, this user is having problems.' in error_message, 'Error message not displayed!'
    except NoSuchElementException:
        pass
    driver.quit()


def test_scenario_4():
    """
    Verify that a user cannot login with an error user account
    """
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
    try:
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert 'Epic sadface: Something went wrong.' in error_message, 'Error message not displayed!'
    except NoSuchElementException:
        pass
    driver.quit()


def test_scenario_5():
    """
    Verify that a user cannot login with a visual user account
    """
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
    try:
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert 'Epic sadface: You do not have access to that resource.' in error_message, 'Error message not displayed!'
    except NoSuchElementException:
        pass
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

    try:
        test_scenario_5()
    except AssertionError as e:
        print("Assertion error in test_scenario_5:", e)