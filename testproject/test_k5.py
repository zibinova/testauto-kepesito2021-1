from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)

bingo_box = driver.find_elements_by_xpath("//*[@id='bingo-body']/tr/td")
number_list = driver.find_elements_by_xpath("//*[@id='numbers-list']/li")
play_button = driver.find_element_by_id("spin")
first_bingo = driver.find_elements_by_xpath("//*[@id='messages']/li[1]/text()")

test_data = [25, 75]


def test_initial_state():
    """TC 1:Az applikáció helyesen megjelenik:
    A bingo tábla 25 darab cellát tartalmaz
    A számlista 75 számot tartalmaz"""

    assert int(len(bingo_box)) == test_data[0]
    assert int(len(number_list)) == test_data[1]


def test_bingo_check():
    """TC2:Bingo számok ellenőzrzése:
    Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
    Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki"""

    # while True:
    #     play_button.click()


def test_replay():
    """Új játékot tudunk indítani
    az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    új bingo szelvényt kapunk más számokkal."""
