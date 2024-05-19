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
    gender = driver.find_element(By.XPATH, "//input[@value='Male']")
    gender.click()
    mobile_number = driver.find_element(By.ID, "userNumber")
    mobile_number.send_keys("1234567890")
    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.send_keys("15 May 1990")
    sports_checkbox = driver.find_element(By.XPATH, "//input[@value='Sports']")
    sports_checkbox.click()
    music_checkbox = driver.find_element(By.XPATH, "//input[@value='Music']")
    music_checkbox.click()
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png")
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("123 Main Street, City, Country")
    state = Select(driver.find_element(By.ID, "state"))
    state.select_by_visible_text("NCR")
    city = Select(driver.find_element(By.ID, "city"))
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


if __name__ == "__main__":

    try:
        test_scenario_0()
    except AssertionError as e:
        print("Assertion error in test_scenario_0:", e)

    try:
        test_scenario_1()
    except AssertionError as e:
        print("Assertion error in test_scenario_1:", e)