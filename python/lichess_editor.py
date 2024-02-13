import json
import os
import random
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from html_elements import menu, dropdown_script
from css_menu import css_menu
from html_menu import html_menu
from javascript import JS
from update_piece_images import JS as update_piece_js
from detect_move_js import DETECT_MOVE_JS as detect_move_js
from detect_move_js import RETURN_BOARD_JS, SUGGEST_MOVE_JS
from detect_current_color_turn import JS as DETECT_COLOR_TO_MOVE
from get_local_storage_js import JS as getLocalStorageJs
from datetime import datetime, timedelta

with open('./config.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        # Process each line (e.g., print it)
        SAVE_TO = line.strip()


class StateManager:

    def __init__(self):
        self.bot_moved = False
        self.count_of_data_saving = 0


print('yo')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://lichess.org/')
driver.refresh()
print("yo2")
css_code = css_menu
driver.execute_script(f"window.moveToSuggest = false;")
driver.execute_script("window.gameStarted = false;")
driver.execute_script("window.botCurrentColor = false;")
driver.execute_script("window.suggestColor = '#FF0000';")
driver.execute_script("localStorage.setItem('pylaData', {'test1': 23})")
bot_moved = False

with open(SAVE_TO, "r") as json_file:
    data = json.load(json_file)

# Iterate over key-value pairs and add them to local storage
for key, value in data.items():
    if key == "cookie":
        continue
    if key == "chessPieces":
        driver.execute_script(f"window.editedChessPhotos = {value}")
        for color in value.keys():
            for piece_name in value[color].keys():
                dataURL = value[color][piece_name]
                driver.execute_script(f"localStorage['PYLA|{color}-{piece_name}'] = '{dataURL}'")
        continue
    driver.execute_script(f"localStorage.setItem('{key}', '{value}')")
driver.delete_cookie("lila2")
expiry_time = (datetime.utcnow() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

if "cookie" in data.keys():
    if isinstance(data["cookie"], str):
        cookie = {
            'name': 'lila2',
            'value': data["cookie"],
            'expiry': (int(time.time()) + 3600) * 24 * 930,  # 30 days
            'httpOnly': True,
            'domain': ".lichess.org",
            'path': '/',
        }
        driver.delete_cookie("lila2")
        driver.add_cookie(cookie)
        driver.refresh()
driver.refresh()


def lichess(state_manager):
    if "login" in driver.current_url:
        driver.delete_cookie("lila2")
        driver.delete_cookie("lila2")

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    div_with_figures = soup.find('cg-board')
    element = driver.find_element(By.CLASS_NAME, "site-title-nav")
    body_element = driver.find_element(By.TAG_NAME, "body")

    if "Cheat" not in element.get_attribute("innerHTML"):
        driver.execute_script(dropdown_script, element)
        driver.execute_script(
            f"var style = document.createElement('style'); style.innerHTML = `{css_code}`; document.head.appendChild(style);")

        cheat_menu_drop_down = driver.find_element(By.CLASS_NAME, "dropdown-content")
        driver.execute_script("arguments[0].innerHTML = arguments[1];", cheat_menu_drop_down, html_menu)
        driver.execute_script(JS, body_element)

    if len(driver.find_elements(By.CLASS_NAME, "round__app__table")) > 0:
        pass
    driver.execute_script(detect_move_js, body_element)

    time.sleep(1)
    if state_manager.count_of_data_saving == 5:
        state_manager.count_of_data_saving = 0
        localStorage = driver.execute_script(getLocalStorageJs)
        saved_data = {"chessPieces": {"white": {}, "black": {}}}
        for lsKey in list(localStorage.keys()):
            print("hellooo??", random.randint(1, 99999))
            key_split = lsKey.split("PYLA|")
            key_joined = "".join(key_split)
            print(localStorage.keys(), key_joined, "pawn" in key_joined)
            if len(key_split) > 1:
                if "pawn" in key_joined or "rook" in key_joined or "knight" in key_joined or "bishop" in key_joined \
                        or "king" in key_joined or "queen" in key_joined:
                    piece_color, piece_name = key_joined.split('-')
                    saved_data['chessPieces'][piece_color][piece_name] = localStorage[lsKey]
                    print("went in!")
                    continue
                saved_data[lsKey] = localStorage[lsKey]

        saved_data['cookie'] = driver.get_cookie('lila2')['value']

        file_path = SAVE_TO

        with open(file_path, "w") as json_file:
            json.dump(saved_data, json_file)

        state_manager.count_of_data_saving = 0

        driver.execute_script(f"window.editedChessPhotos = {saved_data['chessPieces']}")
    state_manager.count_of_data_saving += 1

    driver.execute_script(update_piece_js)


state_manager = StateManager()

while True:
    try:
        if "lichess" in driver.current_url:
            lichess(state_manager)
    except:
        print("error")
