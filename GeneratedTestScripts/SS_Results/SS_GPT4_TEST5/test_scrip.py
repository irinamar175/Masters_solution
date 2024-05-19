from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_with_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_field = driver.find_element(By.ID, 'ptxt')
    search_field.send_keys('auto')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'auto' in driver.page_source
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.d1')))
    assert 'Lūdzu, ievadiet meklēšanas frāzi' in driver.page_source
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_field = driver.find_element(By.ID, 'ptxt')
    search_field.send_keys('!@#$%^&*()')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg2')))
    assert 'Nav atrasts neviens sludinājums' in driver.page_source
    driver.quit()


def test_search_with_valid_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_select = Select(driver.find_element(By.NAME, 'cid_0'))
    section_select.select_by_visible_text('Transports')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Transports' in driver.page_source
    driver.quit()


def test_search_with_default_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.d1')))
    assert 'Lūdzu, izvēlieties sadaļu' in driver.page_source
    driver.quit()


def test_search_with_valid_region_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_select = Select(driver.find_element(By.NAME, 'search_region'))
    region_select.select_by_visible_text('Rīga')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Rīga' in driver.page_source
    driver.quit()


def test_search_with_default_region_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Visi sludinājumi' in driver.page_source
    driver.quit()


def test_search_with_valid_period_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    period_select = Select(driver.find_element(By.NAME, 'pr'))
    period_select.select_by_visible_text('Pēdējā nedēļā')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Pēdējā nedēļā' in driver.page_source
    driver.quit()


def test_search_with_default_period_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msga2')))
    assert 'Starp visiem sludinājumiem' in driver.page_source
    driver.quit()


if __name__ == '__main__':
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters_in_keyword()
    test_search_with_valid_section_selection()
    test_search_with_default_section_selection()
    test_search_with_valid_region_selection()
    test_search_with_default_region_selection()
    test_search_with_valid_period_selection()
    test_search_with_default_period_selection()
