# user notes: you may need to update the latest webdriver for your browser in ..\webdrivers\msedgedriver.exe

# beckylin is really good at set

from selenium import webdriver
from typing import List 
import os 
import time

# set up env for webdriver so its on the path
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "webdrivers")
os.environ["PATH"] += os.pathsep + dir_path
driver = webdriver.Edge("msedgedriver")

# web page bindings
set_web_page = "http://setgame.azurewebsites.net/"
card_container = '//*[@id="container"]/div/div[2]'

class game_card(object):
    def __init__(self, element):
        self.web_element = element
        self.classes: List[str] = element.get_attribute("class").split(" ")
        compound_value: List[str] = self.classes[2].split("-")
        new_values = []
        for i in range(0, len(compound_value) - 1):
            new_values.append(compound_value[i])
        self.classes[2] = "-".join(new_values)
        self.classes.append(compound_value[-1])

    def click_element(self):
        self.web_element.click()

def get_all_cards():
    cards = driver.find_elements_by_class_name("set-game-card")
    game_cards = [game_card(x) for x in cards] # can fold in list comprehension if perf sux
    return game_cards

def check_for_match(first: game_card, second: game_card, third: game_card) -> bool:
    for i in range(1, len(first.classes)):
        first_value = first.classes[i]
        second_value = second.classes[i]
        third_value = third.classes[i]

        if first_value == second_value and first_value == third_value:
            pass
        elif first_value != second_value and first_value != third_value and second_value != third_value:
            pass
        else:
            return False

    return True

def find_a_set(cards: List[game_card]):
    for first in range(0, len(cards)):
        for second in range(first + 1, len(cards)):
            for third in range(second + 1, len(cards)):
                if (check_for_match(cards[first], cards[second], cards[third])):
                    return [cards[first], cards[second], cards[third]]

def click_set_members(found_set: List[game_card]):
    for card in found_set:
        card.click_element()
        time.sleep(.01)

def solve_it():
    driver.get(set_web_page)
    while(True):
        cards = get_all_cards()
        found_set = find_a_set(cards)
        if not found_set:
            break
        click_set_members(found_set)
    driver.execute_script('alert("Did I beat beckylin??");')
    input("Press Enter to continue...")
    driver.close()


solve_it()

dummy = 1