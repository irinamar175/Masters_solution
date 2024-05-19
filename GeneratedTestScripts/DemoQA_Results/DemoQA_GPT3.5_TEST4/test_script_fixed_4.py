from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("1234567890")
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.send_keys("15 May 1990")
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys("\n")
    subjects.send_keys("English")
    hobbies = driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]')
    driver.execute_script("arguments[0].click();", hobbies)
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("123 Main Street, City, Country")
    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("California")
    state.send_keys("\n")
    city = driver.find_element(By.ID, "react-select-4-input")
    driver.execute_script("arguments[0].click();", city)
    city.send_keys("Los Angeles")
    city.send_keys("\n")
    upload = driver.find_element(By.ID, "uploadPicture")
    upload.send_keys("/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png")
    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit)
    driver.quit()


def test_scenario_1():
    """
    Verify that user cannot submit the form without entering mandatory fields
    """
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit = driver.find_element(By.ID, "submit")
    submit.click()
    error_message = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    assert "Thanks for submitting the form" not in error_message, "Form submitted with empty fields!"
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