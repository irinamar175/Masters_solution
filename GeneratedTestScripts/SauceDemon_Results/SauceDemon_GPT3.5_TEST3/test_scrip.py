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
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
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
    password = 'secret_sauce'
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert 'Epic sadface' in driver.page_source, 'Invalid login succeeded!'
    driver.quit()


def test_scenario_2():
    """
    Verify that a user cannot login with a locked out user account
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'locked_out_user'
    password = 'secret_sauce'
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert 'Epic sadface' in driver.page_source, 'Locked out user login succeeded!'
    driver.quit()


def test_scenario_3():
    """
    Verify that error message is displayed for incorrect login attempts
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = 'invalid_user'
    password = 'invalid_password'
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert 'Epic sadface' in driver.page_source, 'Incorrect login error message not displayed!'
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