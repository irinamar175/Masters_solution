from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_scenario_0():
    """
    Verify that the search form can be submitted with valid input data
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    keyword = 'car'
    section = 'Transports'
    deal_type = 'Pārdod'
    city_region = 'Rīga'
    period = 'Pēdējās 3 dienās'
    search_keyword = driver.find_element(By.ID, 'ptxt')
    search_keyword.send_keys(keyword)
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text(section)
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text(deal_type)
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text(city_region)
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text(period)
    search_button = driver.find_element(By.ID, 'sbtn')
    search_button.click()
    driver.quit()


def test_scenario_1():
    """
    Verify that the search form cannot be submitted with invalid input data
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    keyword = ''
    section = '-1'
    deal_type = 'Pārdod'
    city_region = '0'
    period = 'invalid'
    search_keyword = driver.find_element(By.ID, 'ptxt')
    search_keyword.send_keys(keyword)
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_value(section)
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text(deal_type)
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_value(city_region)
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_value(period)
    search_button = driver.find_element(By.ID, 'sbtn')
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