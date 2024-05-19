from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that the search functionality works correctly with valid input data
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    keyword = 'car'
    search_keyword = driver.find_element(By.NAME, 'txt')
    search_keyword.send_keys(keyword)
    section = 'Transports'
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text(section)
    deal_type = 'Pārdod'
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text(deal_type)
    city_region = 'Rīga'
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text(city_region)
    period = 'Pēdējās 3 dienās'
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text(period)
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    driver.quit()


def test_scenario_1():
    """
    Verify that the search functionality handles empty search keyword field
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section = 'Nekustamie īpašumi'
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text(section)
    deal_type = 'Pārdod'
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text(deal_type)
    city_region = 'Rīga'
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text(city_region)
    period = 'Pēdējās 3 dienās'
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text(period)
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    driver.quit()


def test_scenario_2():
    """
    Verify that the search functionality handles invalid input data
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    keyword = '!!!'
    search_keyword = driver.find_element(By.NAME, 'txt')
    search_keyword.send_keys(keyword)
    section = 'Darbs un bizness'
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text(section)
    deal_type = 'Pārdod'
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text(deal_type)
    city_region = 'Rīga'
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text(city_region)
    period = 'Pēdējās 3 dienās'
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text(period)
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
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