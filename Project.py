import tkinter as tk
import threading
import datetime
root = tk.Tk()

def eye_rest_reminder():
    print("It's time to take a break and rest your eyes!")
def start_timer():
    timer = threading.Timer(30, eye_rest_reminder)
    timer.start()
start_timer()


root.mainloop()
