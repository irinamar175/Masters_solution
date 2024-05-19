from bs4 import BeautifulSoup
from selenium import webdriver


# Template generation based on requirements for model
def create_test_template(requirements: list):
    template = """
from selenium import webdriver
# Imports ...

    """

    for i, requirement in enumerate(requirements):
        template += f"""
def test_scenario_{i}():
    \"\"\"
    {requirement}
    \"\"\"
    driver = webdriver.Chrome()
    # Test implementation...
    driver.quit()
        """

    template += """
if __name__ == "__main__":
    """
    for i in range(len(requirements)):
        template += f"""
    try:
        test_scenario_{i}()
    except AssertionError as e:
        print("Assertion error in test_scenario_{i}:", e)
        """

    print("Template", template)


def filter_page_html(page_url):
    driver = webdriver.Chrome()
    driver.get(page_url)

    response = driver.page_source
    page_html = BeautifulSoup(response, "html.parser")
    # print(page_html)
    # Remove all script and style elements
    for script in page_html(["meta", "noscript", "head", "symbol", "svg", "defs", "iframe"]):
        script.decompose()

    for div in page_html.find_all("div", class_="footer"):
        div.decompose()

    # Remove the div with id 'coverage'
    coverage_div = page_html.find(id="coverage")
    if coverage_div:
        coverage_div.decompose()

    # Convert HTML object back to a string without additional newlines
    text = str(page_html)
    lines = text.splitlines()
    lines_blank = [line for line in lines if line.strip()]
    new_text = '\n'.join(lines_blank)

    return new_text
# create_test_template(["Test scenario 1", "Test scenario 2", "Test scenario 3"])