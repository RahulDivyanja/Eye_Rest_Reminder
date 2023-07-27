import tkinter as tk
import threading
import time
#from win10toast import ToastNotifier
from winotify import Notification,audio

#toaster=ToastNotifier()

root = tk.Tk()
root.title('Eye Rest Reminder')
my_label = tk.Label(root,text='')
my_label.pack(pady=20)

def clock():
    hour = time.strftime("%H")
    minute = time.strftime('%M')
    second =time.strftime('%S')
    my_label.config(text=f"{hour}:{minute}:{second}")
    my_label.after(1000,clock)

def eye_rest_reminder():
    #toaster.show_toast("Eye rest reminder","Now is the time to rest your eyes",duration=5)
    toast = Notification(app_id='Take rest',title='Eye Rest Reminder',msg='Now is the time to rest your eyes',duration='long')
    toast.set_audio(audio.LoopingAlarm,loop=True)
    toast.show()

def start_timer():
    timer = threading.Timer(5, eye_rest_reminder)
    timer.start()

start_timer()
clock()

root.mainloop()
