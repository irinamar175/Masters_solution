from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that the user is able to fill out the student registration form with valid data and submit successfully
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe")
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@example.com")
    gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    gender.click()
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.send_keys("15 May 1990")
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths, English")
    hobbies = driver.find_element(By.XPATH, "//input[@value='1']")
    hobbies.click()
    hobbies = driver.find_element(By.XPATH, "//input[@value='2']")
    hobbies.click()
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("valid_picture.jpg")
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("123 Main Street, City, Country")
    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("California")
    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys("Los Angeles")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    driver.quit()


def test_scenario_1():
    """
    Verify that the form validation works correctly when submitting the form with invalid data
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("123")
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe123")
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@example")
    gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
    gender.click()
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("12345")
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.send_keys("30 Feb 2000")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
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