from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_scenario_0():
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
    hobbies_sports = driver.find_element(By.ID, "hobbies-checkbox-1")
    driver.execute_script("arguments[0].click();", hobbies_sports)
    hobbies_reading = driver.find_element(By.ID, "hobbies-checkbox-2")
    driver.execute_script("arguments[0].click();", hobbies_reading)
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png")
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("123 Main Street, City, Country")
    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("California")
    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys("Los Angeles")
    submit_button = driver.find_element(By.ID, "submit")
    actions = ActionChains(driver)
    actions.move_to_element(submit_button).click().perform()
    driver.quit()


def test_scenario_1():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit_button = driver.find_element(By.ID, "submit")
    actions = ActionChains(driver)
    actions.move_to_element(submit_button).click().perform()
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "First Name" in alert_text, "First Name validation failed!"
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