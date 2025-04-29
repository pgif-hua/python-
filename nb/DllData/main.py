import pygetwindow as gw
import pyautogui
import random
import time

def random_move_window(window):
    screen_width, screen_height = pyautogui.size()
    window_width, window_height = window.width, window.height
    if window_width > screen_width or window_height > screen_height:
        print("无法移动。")
        return
    new_x = random.randint(0, max(0, screen_width - window_width))
    new_y = random.randint(0, max(0, screen_height - window_height))
    window.moveTo(new_x, new_y)
    print(f"窗口 '{window.title}' 已移动到: ({new_x}, {new_y})")

def main():
    while True:
        windows = gw.getAllWindows()
        if not windows:
            print("无窗口")
            continue
        target_window = random.choice(windows)
        random_move_window(target_window)

if __name__ == "__main__":
    main()