import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('sb')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='牛逼小孩！',  #
             bg='yellow',  
             font=('楷体', 17), 
             width=15, height=2 
             ).pack()  
    window.mainloop()


threads = []
for i in range(20):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()