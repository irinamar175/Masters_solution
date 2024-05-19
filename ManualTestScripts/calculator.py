from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")


#  Positive scenarios
def test_numbers():
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='4']").click()
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='6']").click()
    driver.find_element(By.XPATH, "//button[text()='7']").click()
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '1234567890', "Numbers Failed"


def test_clear_display():
    driver.find_element(By.XPATH, "//button[text()='C']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '', "Clear display failed"


def test_addition():
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='7']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '12', "Addition failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_subtraction():
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='6']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '-4', "Subtraction failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_multiplication():
    driver.find_element(By.XPATH, "//button[text()='4']").click()
    driver.find_element(By.XPATH, "//button[text()='*']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '12', "Multiplication failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_division():
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '0.38095238095238093', "Division failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_power():
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='^']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '8', "Power calculation failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_square_root():
    driver.find_element(By.XPATH, "//button[text()='9']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '3', "Square root calculation failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


def test_combo():
    driver.find_element(By.XPATH, "//button[text()='6']").click()
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='1']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == '2.5', "Combo failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()


#  Negative scenarios
def test_division_by_zero():
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='/']").click()
    driver.find_element(By.XPATH, "//button[text()='0']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    alert = Alert(driver)
    assert "Cannot divide by zero" in alert.text, "Alert message mismatch"
    alert.accept()


def test_square_root_of_negative():
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    driver.find_element(By.XPATH, "//button[text()='sqrt']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    alert = Alert(driver)
    assert "Cannot take square root of a negative number!" in alert.text, "Alert message mismatch"
    alert.accept()


def test_invalid_operations():
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    assert driver.find_element(By.ID, "display").get_attribute('value') == 'NaN', "Invalid operation failed"
    driver.find_element(By.XPATH, "//button[text()='C']").click()

def test_equal():
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    alert = Alert(driver)
    assert "Invalid operator!" in alert.text, "Alert message mismatch"
    alert.accept()
    driver.quit()

if __name__ == "__main__":
    try:
        test_numbers()
    except AssertionError as e:
        print("Assertion error in test_numbers:", e)
    try:
        test_clear_display()
    except AssertionError as e:
        print("Assertion error in test_clear_display:", e)
    try:
        test_addition()
    except AssertionError as e:
        print("Assertion error in test_addition:", e)
    try:
        test_subtraction()
    except AssertionError as e:
        print("Assertion error in test_subtraction:", e)
    try:
        test_multiplication()
    except AssertionError as e:
        print("Assertion error in test_multiplication:", e)
    try:
        test_division()
    except AssertionError as e:
        print("Assertion error in test_division:", e)
    try:
        test_power()
    except AssertionError as e:
        print("Assertion error in test_power:", e)
    try:
        test_square_root()
    except AssertionError as e:
        print("Assertion error in test_square_root:", e)
    try:
        test_combo()
    except AssertionError as e:
        print("Assertion error in test_combo:", e)
    try:
        test_division_by_zero()
    except AssertionError as e:
        print("Assertion error in test_division_by_zero:", e)
    try:
        test_square_root_of_negative()
    except AssertionError as e:
        print("Assertion error in test_square_root_of_negative:", e)
    try:
        test_invalid_operations()
    except AssertionError as e:
        print("Assertion error in test_invalid_operations:", e)
    try:
        test_equal()
    except AssertionError as e:
        print("Assertion error in test_equal:", e)

