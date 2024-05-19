from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that user can successfully fill out the student registration form with valid data
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
    gender = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", gender)
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.send_keys("15 May 1990")
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths, English")
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-1")
    hobbies.click()
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-2")
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
    Verify that validation messages are displayed for each field when submitting the form with invalid data
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please enter first name' in alert_text, 'Validation message for first name failed!'
    alert.accept()
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please enter last name' in alert_text, 'Validation message for last name failed!'
    alert.accept()
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please enter email' in alert_text, 'Validation message for email failed!'
    alert.accept()
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@example.com")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please select gender' in alert_text, 'Validation message for gender failed!'
    alert.accept()
    gender = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", gender)
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please enter mobile number' in alert_text, 'Validation message for mobile number failed!'
    alert.accept()
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please select date of birth' in alert_text, 'Validation message for date of birth failed!'
    alert.accept()
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.send_keys("15 May 1990")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please select subjects' in alert_text, 'Validation message for subjects failed!'
    alert.accept()
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths, English")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please select hobbies' in alert_text, 'Validation message for hobbies failed!'
    alert.accept()
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-1")
    hobbies.click()
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-2")
    hobbies.click()
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please upload a picture' in alert_text, 'Validation message for picture failed!'
    alert.accept()
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("valid_picture.jpg")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please enter current address' in alert_text, 'Validation message for current address failed!'
    alert.accept()
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("123 Main Street, City, Country")
    submit_button.click()
    alert = Alert(driver)
    alert_text = alert.text
    assert 'Please select state and city' in alert_text, 'Validation message for state and city failed!'
    alert.accept()
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