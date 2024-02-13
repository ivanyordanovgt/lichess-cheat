import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from html_elements import menu, dropdown_script
from css_menu import css_menu
from html_menu import html_menu
from javascript import JS
from stockfish import Stockfish
from update_piece_images import JS as update_piece_js
from detect_move_js import DETECT_MOVE_JS as detect_move_js
from detect_move_js import RETURN_BOARD_JS, SUGGEST_MOVE_JS
from detect_current_color_turn import JS as DETECT_COLOR_TO_MOVE


class StateManager:

    def __init__(self):
        self.bot_moved = False
        self.whiteColorSquareValue = None

state_manager = StateManager()

print('yo')
driver = webdriver.Chrome()
driver.get('https://lichess.org/')
cookie = driver.get_cookie("lila2")
cookie['value'] = "17003339bffd9ae76cb4609b819dadb4a213c858-sid=0JlDS9aK6AODoKr6VRbdYM&sessionId=U8PQhUTNo1U27KZJYCbY2r"
driver.delete_cookie("lila2")
driver.add_cookie(cookie)
driver.refresh()
print("yo2")
css_code = css_menu
stockfish_engine = Stockfish(stockfish_color="white")
driver.execute_script(f"window.moveToSuggest = false;")
driver.execute_script("window.gameStarted = false;")
driver.execute_script("window.botCurrentColor = false;")
driver.execute_script("window.suggestColor = '#FF0000';")
driver.execute_script("window['whiteColorPickerValue'] = false;")
driver.execute_script("localStorage.setItem('pylaData', {})")

bot_moved = False


def lichess(state_manager):
    time.sleep(0.1)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    div_with_figures = soup.find('cg-board')
    element = driver.find_element(By.CLASS_NAME, "site-title-nav")
    body_element = driver.find_element(By.TAG_NAME, "body")

    href = "'#'"
    print(element, "YOO")

    if "Cheat" not in element.get_attribute("innerHTML"):
        driver.execute_script(dropdown_script, element)
        driver.execute_script(
            f"var style = document.createElement('style'); style.innerHTML = `{css_code}`; document.head.appendChild(style);")

        cheat_menu_drop_down = driver.find_element(By.CLASS_NAME, "dropdown-content")
        print(cheat_menu_drop_down, "DROPDOWN!!!")
        driver.execute_script("arguments[0].innerHTML = arguments[1];", cheat_menu_drop_down, html_menu)

    time.sleep(1)
    driver.execute_script(JS, body_element)
    whiteColorSquareValue = driver.execute_script("return window['whiteColorPickerValue']")
    if whiteColorSquareValue:
        state_manager.whiteColorSquareValue = whiteColorSquareValue
    else:
        pass

    if len(driver.find_elements(By.CLASS_NAME, "round__app__table")) > 0:
        driver.execute_script(update_piece_js, body_element)
    driver.execute_script(detect_move_js, body_element)
    print('bro')

    driver.execute_script(DETECT_COLOR_TO_MOVE)
    bot_to_move = driver.execute_script("return window['botToTurn']")
    print(bot_to_move, "!!?!?!??!?!")

    if not bot_to_move:
        state_manager.bot_moved = False

    if bot_to_move:
        chess_matrix = driver.execute_script(RETURN_BOARD_JS)
        board = stockfish_engine.set_board_from_matrix(chess_matrix)
        stockfish_engine.board = board
        stockfish_engine.board_to_move = True
        move = stockfish_engine.move()[0]
        if move:
            driver.execute_script(f"window['moveToSuggest'] = '{move}'")
            driver.execute_script(SUGGEST_MOVE_JS)
            print(stockfish_engine.board)
            state_manager.bot_moved = True
        else:
            stockfish_engine.board_to_move = False

    time.sleep(1)


time.sleep(5)
state_manager = StateManager()

while True:
    if "lichess" in driver.current_url:
        lichess(state_manager)

driver.quit()

skins = {'blue': {'skins': ['a','b','c'], 'chance': 85}, 'red': {'skins': ['a','b','c'], 'chance': 5.5}}

random_quality = random.choice(['blue' * skins['blue']['chance']])
random_skin = random.choice(skins[random_quality]['skins'])
