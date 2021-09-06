from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)

# Locators:

start_button = driver.find_element_by_id("start")
stop_button = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")
random_color = driver.find_element_by_id("randomColor")
test_color = driver.find_element_by_id("testColorName")


def test_initial_state():
    """TC 1:Helyesen jelenik meg az applikáció betöltéskor
        Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
        A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]>"""

    assert random_color.is_displayed()
    assert test_color.text == ""


def test_function():
    """TC 2:El lehet indítani a játékot a start gommbal.
    Ha elindult a játék akkor a stop gombbal le lehet állítani."""

    assert start_button.is_displayed() and start_button.is_enabled()
    start_button.click()
    assert stop_button.is_displayed() and stop_button.is_enabled()
    stop_button.click()
    assert result.is_displayed()


def test_guess():
    """TC 3:Eltaláltam, vagy nem találtam el.
    Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és a jobb oldal ugyan
    azt a színt tartalmazza akkor a Correct! felirat jelenik meg.
    ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen"""

    if random_color.get_attribute("style") == test_color.get_attribute("style"):
        assert result.text == "Correct!"
    else:
        assert result.text == "Incorrect!"
