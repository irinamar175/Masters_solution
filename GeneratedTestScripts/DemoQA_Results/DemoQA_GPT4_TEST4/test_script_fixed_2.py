from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_search_with_valid_keyword():
    """
    Test the search functionality with a valid keyword.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.NAME, 'txt')
    search_input.send_keys('auto')
    search_button = driver.find_element(By.NAME, 'btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btn')))
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming 'msga2-o' is a class for search results
    assert 'auto' in driver.page_source, "Search results related to 'auto' are not displayed."
    driver.quit()


def test_search_with_empty_keyword():
    """
    Test the search functionality with an empty keyword.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    try:
        driver.find_element(By.CLASS_NAME, 'msga2-o')
        assert False, "Results should not be displayed for empty search."
    except NoSuchElementException:
        assert True
    driver.quit()


def test_search_with_special_characters():
    """
    Test the search functionality with special characters.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_input = driver.find_element(By.NAME, 'txt')
    search_input.send_keys('@#$%^&*()')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    try:
        driver.find_element(By.CLASS_NAME, 'msga2-o')
        assert False, "Results should not be displayed for special character search."
    except NoSuchElementException:
        assert True
    driver.quit()


def test_search_with_specific_category():
    """
    Test the search functionality with a specific category selected.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    category_dropdown.select_by_visible_text('Transports')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming 'msga2-o' is a class for search results
    assert 'Transports' in driver.page_source, "Search results related to 'Transports' are not displayed."
    driver.quit()


def test_search_with_invalid_category():
    """
    Test the search functionality with an invalid category.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    category_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    # Manipulate DOM to add invalid option
    driver.execute_script("var select = arguments[0]; var option = document.createElement('option'); option.text = 'InvalidCategory'; option.value = 'invalid'; select.add(option);", category_dropdown)
    category_dropdown.select_by_value('invalid')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    try:
        driver.find_element(By.CLASS_NAME, 'msga2-o')
        assert False, "Results should not be displayed for invalid category."
    except NoSuchElementException:
        assert True
    driver.quit()


def test_search_with_specific_transaction_type():
    """
    Test the search functionality with a specific transaction type selected.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    transaction_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    transaction_type_dropdown.select_by_visible_text('Pārdod')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming 'msga2-o' is a class for search results
    assert 'Pārdod' in driver.page_source, "Search results related to 'Pārdod' are not displayed."
    driver.quit()


def test_search_with_specific_region():
    """
    Test the search functionality with a specific region selected.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    region_dropdown.select_by_visible_text('Rīga')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming 'msga2-o' is a class for search results
    assert 'Rīga' in driver.page_source, "Search results related to 'Rīga' are not displayed."
    driver.quit()


def test_search_with_specific_period():
    """
    Test the search functionality with a specific period selected.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    period_dropdown.select_by_visible_text('Pēdējā nedēļā')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'msga2-o')))  # Assuming 'msga2-o' is a class for search results
    assert 'Pēdējā nedēļā' in driver.page_source, "Search results from the last week are not displayed."
    driver.quit()


if __name__ == '__main__':
    test_search_with_valid_keyword()
    test_search_with_empty_keyword()
    test_search_with_special_characters()
    test_search_with_specific_category()
    test_search_with_invalid_category()
    test_search_with_specific_transaction_type()
    test_search_with_specific_region()
    test_search_with_specific_period()
