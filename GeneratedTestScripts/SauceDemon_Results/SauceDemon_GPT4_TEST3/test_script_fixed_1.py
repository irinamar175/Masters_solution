from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url, "Login failed!"
    driver.quit()


def test_login_with_invalid_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("invalid_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("wrong_password")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_empty_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username is required" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_empty_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Password is required" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_all_fields_empty():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username is required" in error_message or "Epic sadface: Password is required" in error_message, "Error messages not displayed!"
    driver.quit()


def test_login_with_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("locked_out_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message, "Error message not displayed!"
    driver.quit()


if __name__ == "__main__":
    test_login_with_valid_credentials()
    test_login_with_invalid_username()
    test_login_with_invalid_password()
    test_login_with_empty_username()
    test_login_with_empty_password()
    test_login_with_all_fields_empty()
    test_login_with_locked_out_user()
