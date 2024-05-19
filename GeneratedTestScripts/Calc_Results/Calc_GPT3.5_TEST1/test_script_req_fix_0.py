from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the test page
url = driver.get("https://sea-lion-app-q6nwz.ondigitalocean.app/sample1")
assert "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1" in driver.current_url, "Link failed!"

def enter_numbers_test():
    test_steps = [
        {'action': 'Click on the number buttons in the calculator', 'input': '1'},
        {'action': 'Click on the number buttons in the calculator', 'input': '2'},
        {'action': 'Click on the number buttons in the calculator', 'input': '3'},
        {'action': 'Click on the number buttons in the calculator', 'input': '4'},
        {'action': 'Click on the number buttons in the calculator', 'input': '5'}
    ]
    for step in test_steps:
        button = driver.find_element(By.XPATH, f"//button[contains(text(),'{step['input']}')]")
        button.click()

def perform_arithmetic_test():
    test_steps = [
        {'action': 'Click on the number buttons in the calculator', 'input': '5'},
        {'action': 'Click on the operator buttons in the calculator', 'input': '+'},
        {'action': 'Click on the number buttons in the calculator', 'input': '3'},
        {'action': 'Click on the equals button', 'input': '='}
    ]
    for step in test_steps:
        button = driver.find_element(By.XPATH, f"//button[contains(text(),'{step['input']}')]")
        button.click()

def clear_display_test():
    test_steps = [
        {'action': 'Click on the number buttons in the calculator', 'input': '7'},
        {'action': 'Click on the clear button', 'input': 'C'}
    ]
    for step in test_steps:
        button = driver.find_element(By.XPATH, f"//button[contains(text(),'{step['input']}')]")
        button.click()


if __name__ == "__main__":
    try:
        enter_numbers_test()
    except AssertionError as e:
        print("Assertion error in enter_numbers_test:", e)
    try:
        perform_arithmetic_test()
    except AssertionError as e:
        print("Assertion error in perform_arithmetic_test:", e)
    try:
        clear_display_test()
    except AssertionError as e:
        print("Assertion error in clear_display_test:", e)
    driver.quit()