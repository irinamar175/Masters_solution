from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_search_with_valid_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("auto")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "auto" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for search results to load.")
    driver.quit()


def test_search_with_empty_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.msg_div")))
        error_message = driver.find_element(By.CSS_SELECTOR, "div.msg_div").text
        assert "obligāts" in error_message.lower()
    except TimeoutException:
        print("Timeout waiting for error message.")
    driver.quit()


def test_search_with_special_characters_in_keyword():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.ID, "ptxt")
    search_input.send_keys("!@#$%^&*()")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        no_results_message = driver.find_element(By.CSS_SELECTOR, "div.content").text
        assert "nav rezultātu" in no_results_message.lower()
    except TimeoutException:
        print("Timeout waiting for no results message.")
    driver.quit()


def test_search_with_valid_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_dropdown = Select(driver.find_element(By.NAME, "cid_0"))
    section_dropdown.select_by_visible_text("Transports")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "Transports" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for section results.")
    driver.quit()


def test_search_with_default_section_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.msg_div")))
        error_message = driver.find_element(By.CSS_SELECTOR, "div.msg_div").text
        assert "ir jāizvēlas sadaļa" in error_message.lower()
    except TimeoutException:
        print("Timeout waiting for section error message.")
    driver.quit()


def test_search_with_valid_city_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, "search_region"))
    city_dropdown.select_by_visible_text("Rīga")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "Rīga" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for city results.")
    driver.quit()


def test_search_with_all_cities_selection():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    city_dropdown = Select(driver.find_element(By.NAME, "search_region"))
    city_dropdown.select_by_visible_text("Visi sludinājumi")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "Visi sludinājumi" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for all cities results.")
    driver.quit()


def test_search_with_a_specific_time_period():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    time_period_dropdown = Select(driver.find_element(By.NAME, "pr"))
    time_period_dropdown.select_by_visible_text("Pēdejā nedēļā")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "Pēdejā nedēļā" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for time period results.")
    driver.quit()


def test_search_with_default_time_period():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, "btn")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn")))
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content")))
        assert "Starp visiem sludinājumiem" in driver.find_element(By.CSS_SELECTOR, "div.content").text
    except TimeoutException:
        print("Timeout waiting for default time period results.")
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
