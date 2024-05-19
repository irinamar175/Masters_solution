from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_with_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.NAME, 'topt[8][min]')
    search_input.send_keys('auto')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'auto' in driver.page_source, "Search results do not contain 'auto'"
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    error_message = driver.find_element(By.CLASS_NAME, 'error')  # Assuming there's an error class
    assert 'keyword cannot be empty' in error_message.text, "No error message for empty keyword"
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.NAME, 'topt[8][min]')
    search_input.send_keys('!@#$%^&*()')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    assert 'No results found' in driver.page_source or 'error' in driver.page_source, "Special characters handled incorrectly"
    driver.quit()


def test_search_with_a_valid_category_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    category_dropdown.select_by_visible_text('Transports')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'Transports' in driver.page_source, "Search results do not contain 'Transports'"
    driver.quit()


def test_search_with_no_category_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    assert 'All categories are searched' in driver.page_source or 'error' not in driver.page_source, "Error message or incorrect handling when no category is selected"
    driver.quit()


def test_search_with_a_specific_region_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    region_dropdown.select_by_visible_text('Rīga')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'Rīga' in driver.page_source, "Search results do not contain 'Rīga'"
    driver.quit()


def test_search_with_all_regions_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    region_dropdown.select_by_visible_text('Visi sludinājumi')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'All regions' in driver.page_source, "Search results do not contain 'All regions'"
    driver.quit()


def test_search_with_a_specific_period_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text('Pēdējās 3 dienās')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'last 3 days' in driver.page_source, "Search results do not contain 'last 3 days'"
    driver.quit()


def test_search_with_default_period_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text('Starp visiem sludinājumiem')
    search_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming results have a specific class
    assert 'all periods' in driver.page_source, "Search results do not contain 'all periods'"
    driver.quit()

if __name__ == '__main__':
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters_in_keyword()
    test_search_with_a_valid_category_selected()
    test_search_with_no_category_selected()
    test_search_with_a_specific_region_selected()
    test_search_with_all_regions_selected()
    test_search_with_a_specific_period_selected()
    test_search_with_default_period_selected()
