from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scenario_0():
    driver = webdriver.Chrome()
    driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
    assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"
    number_2 = driver.find_element(By.XPATH, "//button[text()='2']")
    number_2.click()
    operator_plus = driver.find_element(By.XPATH, "//button[text()='+']")
    operator_plus.click()
    number_3 = driver.find_element(By.XPATH, "//button[text()='3']")
    number_3.click()
    equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
    equals_button.click()
    result = driver.find_element(By.ID, "display").get_attribute("value")
    assert result == '5', f"Result is not 5, actual result: {result}"
    driver.quit()

def test_scenario_1():
    # Implement test_scenario_1 here

def test_scenario_2():
    # Implement test_scenario_2 here

def test_scenario_3():
    # Implement test_scenario_3 here

def test_scenario_4():
    # Implement test_scenario_4 here

def test_scenario_5():
    # Implement test_scenario_5 here

def test_scenario_6():
    # Implement test_scenario_6 here

def test_scenario_7():
    # Implement test_scenario_7 here

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