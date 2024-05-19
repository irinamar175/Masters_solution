from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that user can search for ads by entering a keyword or phrase
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("Car")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "Search results related to the entered keyword or phrase are displayed" in driver.page_source, "Search results failed!"
    driver.quit()


def test_scenario_1():
    """
    Verify that user can select a category for the search
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, "cid_0"))
    category_dropdown.select_by_visible_text("Darbs un bizness")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "Search results related to the selected category are displayed" in driver.page_source, "Category search failed!"
    driver.quit()


def test_scenario_2():
    """
    Verify that user can select a subcategory for the search
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, "cid_0"))
    category_dropdown.select_by_visible_text("Darbs un bizness")
    subcategory_dropdown = Select(driver.find_element(By.NAME, "cid_1"))
    subcategory_dropdown.select_by_visible_text("Pārdod")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "Search results related to the selected subcategory are displayed" in driver.page_source, "Subcategory search failed!"
    driver.quit()


def test_scenario_3():
    """
    Verify that user can select a region for the search
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_dropdown = Select(driver.find_element(By.NAME, "search_region"))
    region_dropdown.select_by_visible_text("Rīga")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "Search results related to the selected region are displayed" in driver.page_source, "Region search failed!"
    driver.quit()


def test_scenario_4():
    """
    Verify that user can search for ads within a specific time period
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    time_period_dropdown = Select(driver.find_element(By.NAME, "pr"))
    time_period_dropdown.select_by_visible_text("Pēdējās 3 dienās")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "Search results within the selected time period are displayed" in driver.page_source, "Time period search failed!"
    driver.quit()


def test_scenario_5():
    """
    Verify that user cannot search without entering a keyword or phrase
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "An error message is displayed indicating that a keyword or phrase is required" in driver.page_source, "Empty search failed!"
    driver.quit()


def test_scenario_6():
    """
    Verify that user cannot search with an invalid category
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, "cid_0"))
    category_dropdown.select_by_visible_text("Invalid Category")
    search_button = driver.find_element(By.ID, "sbtn")
    search_button.click()
    assert "An error message is displayed indicating that the selected category is invalid" in driver.page_source, "Invalid category search failed!"
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