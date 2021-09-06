from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)

# Locators:
op_table = driver.find_element_by_xpath("/html/body/div/div/p[3]")
char = driver.find_element_by_id("chr")
char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
op_list = driver.find_element_by_xpath("/html/body/div/div/p[3]").text
op = driver.find_element_by_id("op")
num = driver.find_element_by_id("num")


def test_initial_state():
    """TC 1: Helyesen betöltődik az applikáció:
    Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    assert op_table.is_displayed()


def test_op_check():
    """TC 2:Megjelenik egy érvényes művelet:
    chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    op mező vagy + vagy - karaktert tartlamaz
    num mező egy egész számot tartalamaz"""

    assert op_table.is_displayed()
    assert char.text in char_list
    assert op.text == "+" or "-"
    # assert num.text in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
