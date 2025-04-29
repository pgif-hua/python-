
import tkinter as tk
import random
import time

def random_popup():
    window = tk.Tk()
    window.title("You don't exist in this world")
    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    label = tk.Label(window, text="You don't exist in this world", font=("Arial", 16))
    label.pack(expand=True)
    window.attributes("-topmost", True)
    window.after(100, window.destroy)
    window.mainloop()
for i in range(70):
    random_popup()
