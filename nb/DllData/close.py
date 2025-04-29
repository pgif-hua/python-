import os
import psutil
import keyboard
import time

def kill_other_python_processes():
    current_pid = os.getpid()  
    print(f"PID：{current_pid}")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == 'python.exe' and proc.info['pid'] != current_pid:
                print(f"找到其他Python进程，PID为：{proc.info['pid']}")
                os.system(f"taskkill /F /PID {proc.info['pid']}")
                print(f"已结束PID为{proc.info['pid']}的Python进程")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
while True:
    if keyboard.is_pressed('f6'):  
        print("已按下 F6，开始执行关闭其他 Python 进程的操作...")
        kill_other_python_processes()
        print("操作完成，程序即将退出...")
        break
    time.sleep(0.1)  

print("程序已退出。")