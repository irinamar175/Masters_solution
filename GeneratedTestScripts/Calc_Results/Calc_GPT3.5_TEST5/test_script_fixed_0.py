from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def test_scenario_0():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="2"]').click()
    driver.find_element(By.XPATH, '//button[text()="+"]').click()
    driver.find_element(By.XPATH, '//button[text()="3"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '5', f"Result is not 5, actual result: {result}"
    driver.quit()

def test_scenario_1():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="8"]').click()
    driver.find_element(By.XPATH, '//button[text()="-"]').click()
    driver.find_element(By.XPATH, '//button[text()="4"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '4', f"Result is not 4, actual result: {result}"
    driver.quit()

# Add implementation for the remaining test scenarios

def test_scenario_2():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="5"]').click()
    driver.find_element(By.XPATH, '//button[text()="*"]').click()
    driver.find_element(By.XPATH, '//button[text()="6"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '30', f"Result is not 30, actual result: {result}"
    driver.quit()


def test_scenario_3():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="9"]').click()
    driver.find_element(By.XPATH, '//button[text()="/"]').click()
    driver.find_element(By.XPATH, '//button[text()="3"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '3', f"Result is not 3, actual result: {result}"
    driver.quit()


def test_scenario_4():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="2"]').click()
    driver.find_element(By.XPATH, '//button[text()="^"]').click()
    driver.find_element(By.XPATH, '//button[text()="3"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '8', f"Result is not 8, actual result: {result}"
    driver.quit()


def test_scenario_5():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="9"]').click()
    driver.find_element(By.XPATH, '//button[text()="sqrt"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    result = driver.find_element(By.ID, 'display').get_attribute('value')
    assert result == '3', f"Result is not 3, actual result: {result}"
    driver.quit()


def test_scenario_6():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="7"]').click()
    driver.find_element(By.XPATH, '//button[text()="C"]').click()
    display = driver.find_element(By.ID, 'display').get_attribute('value')
    assert display == '', f"Display is not cleared, actual display: {display}"
    driver.quit()


def test_scenario_7():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    driver.find_element(By.XPATH, '//button[text()="8"]').click()
    driver.find_element(By.XPATH, '//button[text()="/"]').click()
    driver.find_element(By.XPATH, '//button[text()="0"]').click()
    driver.find_element(By.XPATH, '//button[text()="="]').click()
    alert = Alert(driver)
    assert "Cannot divide by zero!" in alert.text, "Error message not displayed"
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

    try:
        test_scenario_3()
    except AssertionError as e:
        print("Assertion error in test_scenario_3:", e)

    try:
        test_scenario_4()
    except AssertionError as e:
        print("Assertion error in test_scenario_4:", e)

    try:
        test_scenario_5()
    except AssertionError as e:
        print("Assertion error in test_scenario_5:", e)

    try:
        test_scenario_6()
    except AssertionError as e:
        print("Assertion error in test_scenario_6:", e)

    try:
        test_scenario_7()
    except AssertionError as e:
        print("Assertion error in test_scenario_7:", e)