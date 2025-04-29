import pyautogui
import random
import time

def random_mouse_move():
    screen_width, screen_height = pyautogui.size()
    new_x = random.randint(0, screen_width)
    new_y = random.randint(0, screen_height)
    pyautogui.moveTo(new_x, new_y, duration=0.1) 


if __name__ == "__main__":
    try:
        while True:
            random_mouse_move()
    except KeyboardInterrupt:
        print("程序已停止")