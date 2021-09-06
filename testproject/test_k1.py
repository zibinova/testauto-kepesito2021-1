from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html "

driver.get(URL)

# Lokátorok:

a_field = driver.find_element_by_id("a")
b_field = driver.find_element_by_id("b")
calc_button = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")
result_text = driver.find_element_by_id("result").text
result_block = driver.find_element_by_id("results")

# Test data:

test_data_valid = [2, 3]
test_data_invalid = ["", ""]

ref_data = ["False", "10", "NaN"]


# Számítás kódja:


def pit_calc(a, b):
    a_field.clear()
    b_field.clear()
    a_field.send_keys(a)
    b_field.send_keys(b)


def test_initial_state():
    """TC 1: Helyesen jelenik meg az applikáció betöltéskor:
    a: <üres>
    b: <üres>
    c: <nem látszik>"""

    calc_button.click()
    assert result.is_displayed()


def test_valid():
    """Számítás helyes, megfelelő bemenettel
    a: 2
    b: 3
    c: 10"""

    pit_calc(test_data_valid[0], test_data_valid[1])
    calc_button.click()
    assert result.text == ref_data[1]


def test_invalid():
    """Üres kitöltés:
    a: <üres>
    b: <üres>
    c: NaN"""

    pit_calc(test_data_invalid[0], test_data_invalid[1])
    calc_button.click()
    assert result.text == ref_data[2]

# test_initial_state()
# test_valid()
# test_invalid()
