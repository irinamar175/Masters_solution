from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_search_with_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_field = driver.find_element(By.ID, 'ptxt')
    search_field.send_keys('auto')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'auto' in driver.page_source, 'Search results do not contain the keyword'
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    try:
        error_message = driver.find_element(By.CSS_SELECTOR, 'div.msg_div')
        assert 'Lauks ir obligāts' in error_message.text, 'Expected error message not found'
    except NoSuchElementException:
        assert False, 'Error message element not found'
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_field = driver.find_element(By.ID, 'ptxt')
    search_field.send_keys('@#$%^&*()')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg2')))
    assert 'Nav rezultātu' in driver.page_source or 'Nederīgi simboli' in driver.page_source, 'Expected error message not found'
    driver.quit()


def test_search_with_valid_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text('Transports')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Transports' in driver.page_source, 'Search results do not match the section'
    driver.quit()


def test_search_with_default_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    try:
        error_message = driver.find_element(By.CSS_SELECTOR, 'div.msg_div')
        assert 'Izvēlieties sadaļu' in error_message.text, 'Expected error message not found'
    except NoSuchElementException:
        assert False, 'Error message element not found'
    driver.quit()


def test_search_with_valid_city_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_dropdown.select_by_visible_text('Rīga')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Rīga' in driver.page_source, 'Search results do not match the city'
    driver.quit()


def test_search_with_all_cities_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_dropdown.select_by_visible_text('Visi sludinājumi')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Visi sludinājumi' in driver.page_source, 'Search results do not match the selection of all cities'
    driver.quit()


def test_search_with_valid_period_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text('Pēdejā nedēļā')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Pēdejā nedēļā' in driver.page_source, 'Search results do not match the period'
    driver.quit()


def test_search_with_default_period_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    driver.execute_script("arguments[0].click();", search_button)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Starp visiem sludinājumiem' in driver.page_source, 'Search results do not match the default period selection'
    driver.quit()


if __name__ == '__main__':
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters_in_keyword()
    test_search_with_valid_section_selection()
    test_search_with_default_section_selection()
    test_search_with_valid_city_selection()
    test_search_with_all_cities_selection()
    test_search_with_valid_period_selection()
    test_search_with_default_period_selection()
