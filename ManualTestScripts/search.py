from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_search_by_all():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_keyword = driver.find_element(By.NAME, 'txt')
    search_keyword.send_keys('audi')
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text('Transports')
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_1'))
    section_dropdown.select_by_visible_text('Vieglie auto')
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text('Pārdod')
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text('Rīga')
    search_period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    search_period_dropdown.select_by_visible_text('Pēdējās 3 dienās')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    assert 'Audi' in driver.find_element(By.CLASS_NAME, 'msg2').text, 'Search keyword not found!'
    driver.quit()


def test_search_by_combo_w_word():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_keyword = driver.find_element(By.NAME, 'txt')
    search_keyword.send_keys('dzīvokļi')
    deal_type_dropdown = Select(driver.find_element(By.NAME, 'sid'))
    deal_type_dropdown.select_by_visible_text('Īrē')
    city_region_dropdown = Select(driver.find_element(By.NAME, 'search_region'))
    city_region_dropdown.select_by_visible_text('Jūrmala')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    subtitle = driver.find_element(By.XPATH, '//*[@id="tr_54898326"]/td[3]/div[1]/span')
    assert 'Dzīvokļi : Jūrmala' in subtitle.text, 'Search keyword not found!'
    driver.quit()


def test_search_by_combo():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_0'))
    section_dropdown.select_by_visible_text('Atpūta, hobiji')
    section_dropdown = Select(driver.find_element(By.NAME, 'cid_1'))
    section_dropdown.select_by_visible_text('Tūrisms')
    search_period_dropdown = Select(driver.find_element(By.NAME, 'pr'))
    search_period_dropdown.select_by_visible_text('Starp šodienas sludinājumiem')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    assert 'Tūrism' in driver.page_source, 'Search keyword not found!'
    driver.quit()


def test_search_by_default():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    section_dropdown = Select(driver.find_element(By.ID, 's_region_select'))
    selected_region = section_dropdown.first_selected_option
    assert 'Visi sludinājumi' in selected_region.text, 'Region title not as expected!'
    period_selection = Select(driver.find_element(By.NAME, 'pr'))
    selected_period = period_selection.first_selected_option
    assert 'Starp visiem sludinājumiem' in selected_period.text, 'Period not as expected!'
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    notif = driver.find_element(By.XPATH, '//*[@id="page_main"]/tbody/tr/td/table[2]/tbody/tr/td')
    assert 'Pēc Jūsu pieprasījuma netika atrasts neviens sludinājums' in notif.text, 'Notification not as expected!'


def search_by_field(driver, field_name, field_value):
    section_dropdown = Select(driver.find_element(By.NAME, field_name))
    section_dropdown.select_by_visible_text(field_value)
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    if not field_value == 'Mājai':
        notif = driver.find_element(By.XPATH, '//*[@id="page_main"]/tbody/tr/td/table[2]/tbody/tr/td')
        assert 'Pēc Jūsu pieprasījuma netika atrasts neviens sludinājums' in notif.text, 'Notification not as expected!'
        driver.get("https://www.ss.lv/lv/search/")
def test_search_by_each():
    driver = webdriver.Chrome()
    driver.get("https://www.ss.lv/lv/search/")
    search_keyword = driver.find_element(By.NAME, 'txt')
    search_keyword.send_keys('test')
    search_button = driver.find_element(By.NAME, 'btn')
    search_button.click()
    assert 'Test' in driver.page_source, 'Search keyword not found!'
    driver.get("https://www.ss.lv/lv/search/")
    search_by_field(driver, 'cid_0', 'Mājai')
    assert 'Mājai' in driver.find_element(By.XPATH, '//*[@id="page_main"]/tbody/tr/td/div[1]/div[1]/h2/a').text, 'Search keyword not found!'
    driver.get("https://www.ss.lv/lv/search/")
    search_by_field(driver, 'sid', 'Rezerves daļas')
    search_by_field(driver, 'search_region', 'Rīga')
    search_by_field(driver, 'pr', 'Pēdējā mēnesī')
    driver.quit()


if __name__ == "__main__":
    try:
        test_search_by_all()
    except AssertionError as e:
        print("Assertion error in test_search_by_all:", e)
    try:
        test_search_by_combo_w_word()
    except AssertionError as e:
        print("Assertion error in test_search_by_combo_w_word:", e)
    try:
        test_search_by_combo()
    except AssertionError as e:
        print("Assertion error in test_search_by_combo:", e)
    try:
        test_search_by_default()
    except AssertionError as e:
        print("Assertion error in test_search_by_default:", e)
    try:
        test_search_by_each()
    except AssertionError as e:
        print("Assertion error in test_search_by_each:", e)
