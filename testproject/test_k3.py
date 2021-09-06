from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)

# Locators:
title_field = driver.find_element_by_id("title")
error_message = driver.find_element_by_xpath("/html/body/form/span")


# function to clear and fill input field:


def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


# Test data:


test_data = ["abcd1234", "teszt233@", "abcd"]
ref_data = ["Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]


def test_valid():
    """TC1:Helyes kitöltés esete:
    title: abcd1234
    Nincs validációs hibazüzenet"""

    clear_and_fill_input(title_field, test_data[0])
    assert error_message.get_attribute("class") == "error"


def test_invalid():
    """TC2:Illegális karakterek esete:
    title: teszt233@
    Only a-z and 0-9 characters allewed."""

    clear_and_fill_input(title_field, test_data[1])
    assert error_message.text == ref_data[0]


def test_invalid2():
    """TC3:Tul rövid bemenet esete:
    title: abcd
    Title should be at least 8 characters; you entered 4."""

    clear_and_fill_input(title_field, test_data[2])
    assert error_message.text == ref_data[1]

# test_valid()
# test_invalid()
# test_invalid2()
