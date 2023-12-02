import tkinter as tk
import threading
import time
#from win10toast import ToastNotifier
from winotify import Notification,audio
import schedule
import screen_brightness_control as sbc
#toaster=ToastNotifier()

setBrightness = 0; #Brightness variable

#Tkinter for Interface
root = tk.Tk()
root.title('Eye Rest Reminder')
my_label = tk.Label(root,text='')
my_label.pack(pady=20)

#clock counter
def clock():

    hour = time.strftime("%H")
    minute = time.strftime('%M')
    second =time.strftime('%S')
    my_label.config(text=f"{hour}:{minute}:{second}") 
    my_label.after(1000,clock)

#Notification function
def eye_rest_reminder():

    
    #toaster.show_toast("Eye rest reminder","Now is the time to rest your eyes",duration=5)
    noty = Notification(app_id='Take rest',title='Eye Rest Reminder',msg='Now is the time to rest your eyes',duration='short')
    noty.set_audio(audio.LoopingAlarm,loop=True)
    noty.show()
    sbc.fade_brightness(setBrightness)



    start_timer()
    brightSet()

#Brightness set to 0%
def brightSet():
    
    duration = threading.Timer(5, resetBright) #brightness set to 75% after 5 seconds
    duration.daemon = True
    duration.start()

#For Notify repeatly  
def start_timer():


    timer = threading.Timer(20, eye_rest_reminder)
    timer.daemon = True
    timer.start()
'''
#testing code parts
schedule.every(10).seconds.do(eye_rest_reminder)  

while 1:
  schedule.run_pending()
'''
#set brightness to 75% 
def resetBright():
    sbc.fade_brightness(75, start=setBrightness)  

#calling to functions
start_timer()
clock()
root.mainloop()


