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
    WebDriverWait(driver, 10).until(EC.title_contains("auto"))
    assert "auto" in driver.title
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    error_message = driver.find_element(By.CSS_SELECTOR, "div.error").text
    assert "required" in error_message.lower()
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("!@#$%^&*()")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    no_results_message = driver.find_element(By.CSS_SELECTOR, "div.no-results").text
    assert "no results" in no_results_message.lower()
    driver.quit()


def test_search_with_valid_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_dropdown = Select(driver.find_element(By.NAME, "cid_0"))
    section_dropdown.select_by_visible_text("Transports")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Transports"))
    assert "Transports" in driver.title
    driver.quit()


def test_search_with_default_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    error_message = driver.find_element(By.CSS_SELECTOR, "div.error").text
    assert "section selection is required" in error_message.lower()
    driver.quit()


def test_search_with_valid_city_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, "search_region"))
    city_dropdown.select_by_visible_text("Rīga")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Rīga"))
    assert "Rīga" in driver.title
    driver.quit()


def test_search_with_all_cities_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, "search_region"))
    city_dropdown.select_by_visible_text("Visi sludinājumi")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Visi sludinājumi"))
    assert "Visi sludinājumi" in driver.title
    driver.quit()


def test_search_with_a_specific_time_period():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    time_period_dropdown = Select(driver.find_element(By.NAME, "pr"))
    time_period_dropdown.select_by_visible_text("Pēdejā nedēļā")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Pēdejā nedēļā"))
    assert "Pēdejā nedēļā" in driver.title
    driver.quit()


def test_search_with_default_time_period():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Starp visiem sludinājumiem"))
    assert "Starp visiem sludinājumiem" in driver.title
    driver.quit()


if __name__ == "__main__":
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters_in_keyword()
    test_search_with_valid_section_selection()
    test_search_with_default_section_selection()
    test_search_with_valid_city_selection()
    test_search_with_all_cities_selection()
    test_search_with_a_specific_time_period()
    test_search_with_default_time_period()
