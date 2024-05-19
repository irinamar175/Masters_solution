from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


def test_empty():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    submit_button = driver.find_element(By.ID, "submit")
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(2)
    submit_button.click()
    time.sleep(3)
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        assert False, "Modal title appeared unexpectedly"
    except TimeoutException:
        pass
    driver.quit()


def test_required_fields():
    name = "Johan"
    last = "Doely"
    mob = "1023456780"
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys(name)
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys(last)
    gender = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", gender)
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys(mob)
    submit_button = driver.find_element(By.ID, "submit")
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(2)
    submit_button.click()
    time.sleep(3)
    modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert 'Thanks for submitting the form' in modal_title.text, 'Form submission failed!'
    student_name = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    assert name + ' ' + last in student_name.text, 'Student name not as expected!'
    student_email = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[2]/td[2]")
    assert '' in student_email.text, 'Student email not as expected!'
    student_mobile = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
    assert mob in student_mobile.text, 'Student mobile number not as expected!'
    student_subjects = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[6]/td[2]")
    assert '' in student_subjects.text, 'Student subjects not as expected!'
    student_adrs = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[9]/td[2]")
    assert '' in student_adrs.text, 'Student address not as expected!'
    student_state = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[10]/td[2]")
    assert '' in student_state.text, 'Student state not as expected!'
    driver.quit()

def test_full_form():
    name = "Jonh"
    last = "Doe"
    ema = "johndoe@example.com"
    mob = "1234567890"
    sbjcts = "Maths"
    adrs = "123 Main Street, City, Country"
    sts = "Rajasthan"
    cty = "Jaipur"
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    assert "https://demoqa.com/automation-practice-form" in driver.current_url, "Link failed!"
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys(name)
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys(last)
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys(ema)
    gender = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", gender)
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys(mob)
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys(sbjcts)
    subjects.send_keys(Keys.RETURN)
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-1")
    driver.execute_script("arguments[0].click();", hobbies)
    hobbies = driver.find_element(By.ID, "hobbies-checkbox-2")
    driver.execute_script("arguments[0].click();", hobbies)
    picture = driver.find_element(By.ID, "uploadPicture")
    picture.send_keys("/Users/irinaozolina/PycharmProjects/GUIAI/master/outputs/Documents/image.png")
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys(adrs)
    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys(sts)
    state.send_keys(Keys.RETURN)
    city = driver.find_element(By.ID, "react-select-4-input")
    driver.execute_script("arguments[0].scrollIntoView();", city)
    time.sleep(1)
    city.send_keys(cty)
    time.sleep(2)
    city.send_keys(Keys.RETURN)
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(2)
    submit_button.click()
    time.sleep(3)
    modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert 'Thanks for submitting the form' in modal_title.text, 'Form submission failed!'
    student_name = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    assert name + ' ' + last in student_name.text, 'Student name not as expected!'
    student_email = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[2]/td[2]")
    assert ema in student_email.text, 'Student email not as expected!'
    student_mobile = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
    assert mob in student_mobile.text, 'Student mobile number not as expected!'
    student_subjects = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[6]/td[2]")
    assert sbjcts in student_subjects.text, 'Student subjects not as expected!'
    student_adrs = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[9]/td[2]")
    assert adrs in student_adrs.text, 'Student address not as expected!'
    student_state = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[10]/td[2]")
    assert sts + ' ' + cty in student_state.text, 'Student state not as expected!'
    driver.quit()


if __name__ == "__main__":
    try:
        test_empty()
    except AssertionError as e:
        print("Assertion error in test_empty:", e)
    try:
        test_required_fields()
    except AssertionError as e:
        print("Assertion error in test_required_fields:", e)
    try:
        test_full_form()
    except AssertionError as e:
        print("Assertion error in test_full_form:", e)