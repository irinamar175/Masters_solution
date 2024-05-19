from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_with_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("auto")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "auto" in driver.page_source, "Search results do not contain 'auto'"
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Lūdzu, ievadiet meklēšanas vārdu" in driver.page_source, "No error message for empty keyword"
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("@#$%^&*()")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Nekas netika atrasts" in driver.page_source or "Nav rezultātu" in driver.page_source, "Results or error message not as expected for special characters"
    driver.quit()


def test_search_with_valid_section_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_select = Select(driver.find_element(By.NAME, "cid_0"))
    section_select.select_by_visible_text("Transports")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Transports" in driver.page_source, "Search results do not contain 'Transports'"
    driver.quit()


def test_search_with_no_section_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Visas sadaļas" in driver.page_source or "Visi sludinājumi" in driver.page_source, "Results not as expected when no section is selected"
    driver.quit()


def test_search_with_specific_region_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_select = Select(driver.find_element(By.NAME, "search_region"))
    region_select.select_by_visible_text("Rīga")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Rīga" in driver.page_source, "Search results do not contain 'Rīga'"
    driver.quit()


def test_search_with_all_regions_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_select = Select(driver.find_element(By.NAME, "search_region"))
    region_select.select_by_visible_text("Visi sludinājumi")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Visi sludinājumi" in driver.page_source, "Search results do not contain 'Visi sludinājumi'"
    driver.quit()


def test_search_with_specific_time_period_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    time_period_select = Select(driver.find_element(By.NAME, "pr"))
    time_period_select.select_by_visible_text("Pēdējā nedēļā")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Pēdējā nedēļā" in driver.page_source, "Search results do not contain 'Pēdējā nedēļā'"
    driver.quit()


def test_search_with_default_time_period_selected():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    time_period_select = Select(driver.find_element(By.NAME, "pr"))
    time_period_select.select_by_visible_text("Starp visiem sludinājumiem")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[align='center']")))
    assert "Starp visiem sludinājumiem" in driver.page_source, "Search results do not contain 'Starp visiem sludinājumiem'"
    driver.quit()


if __name__ == "__main__":
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters_in_keyword()
    test_search_with_valid_section_selected()
    test_search_with_no_section_selected()
    test_search_with_specific_region_selected()
    test_search_with_all_regions_selected()
    test_search_with_specific_time_period_selected()
    test_search_with_default_time_period_selected()