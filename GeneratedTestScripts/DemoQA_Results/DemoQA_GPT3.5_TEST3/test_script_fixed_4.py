from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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
    gender_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    driver.execute_script("arguments[0].scrollIntoView();", gender_label)
    gender_label.click()
    mobile_number = driver.find_element(By.ID, "userNumber")
    mobile_number.send_keys("1234567890")
    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.send_keys("15 May 1990")
    sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
    driver.execute_script("arguments[0].click();", sports_checkbox)
    music_checkbox = driver.find_element(By.XPATH, "//label[text()='Music']")
    driver.execute_script("arguments[0].click();", music_checkbox)
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png")
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("123 Main Street, City, Country")
    state_dropdown = driver.find_element(By.ID, "state")
    state = Select(state_dropdown)
    state.select_by_visible_text("NCR")
    city_dropdown = driver.find_element(By.ID, "city")
    city = Select(city_dropdown)
    city.select_by_visible_text("Delhi")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    driver.quit()


def test_scenario_1():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    driver.quit()


def test_scenario_2():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    alert = driver.switch_to.alert
    assert "Please enter your first name" in alert.text, "First Name validation message not displayed!"
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

    try:
        test_scenario_2()
    except AssertionError as e:
        print("Assertion error in test_scenario_2:", e)