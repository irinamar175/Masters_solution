from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Login failed!"
    driver.quit()


def test_login_with_invalid_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username and password do not match" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username and password do not match" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_empty_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username is required" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_empty_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Password is required" in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_locked_out_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Sorry, this user has been locked out." in error_message, "Error message not displayed!"
    driver.quit()


def test_login_with_special_characters_in_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("user@#")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username and password do not match" in error_message, "Error message not displayed!"
    driver.quit()


if __name__ == "__main__":
    test_login_with_valid_credentials()
    test_login_with_invalid_username()
    test_login_with_invalid_password()
    test_login_with_empty_username()
    test_login_with_empty_password()
    test_login_with_locked_out_user()
    test_login_with_special_characters_in_username()
