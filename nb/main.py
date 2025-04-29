import os
import tkinter.messagebox
import subprocess
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

def main():
    folder_path = "DllData"
    original_file_name = "com.ui"
    new_file_name = "com.py"
    original_file_path = os.path.join(folder_path, original_file_name)
    new_file_path = os.path.join(folder_path, new_file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("Folder created.")
    else:
        print("Folder already exists.")

    if os.path.exists(original_file_path):
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
        os.rename(original_file_path, new_file_path)
        print(f"文件 {original_file_name} 已重命名为 {new_file_name}。")
    else:
        with open(original_file_path, "w") as file:
            file.write("""
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
""")

    if os.path.exists(new_file_path):
        subprocess.Popen(["python", new_file_path])
    else:
        print("Error: com.py file does not exist.")
    subprocess.Popen(["python", "DllData\\main2.py"])
    subprocess.Popen(["python", "DllData\\main3.py"])
    subprocess.Popen(["python", "DllData\\main4.py"])
    subprocess.Popen(["python", "DllData\\close.py"])

if __name__ == "__main__":
    tkinter.messagebox.showinfo("公告","注意这是一个恶搞程序！")
    tkinter.messagebox.showinfo("info","再按3下开始")
    tkinter.messagebox.showinfo("info","再按2下开始")
    tkinter.messagebox.showinfo("info","再按1开始")
    main()
    subprocess.Popen(["python", "DllData\\main.py"])