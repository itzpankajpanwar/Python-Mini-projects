#pip -m install win10toast
inp=input(" enter your notifiacatoin message : ")
import win10toast
toaster = win10toast.ToastNotifier()
toaster.show_toast(inp, duration=10)

import pyjokes
import time
from win10toast import ToastNotifier 

while 1:
    notify = ToastNotifier()
    notify.show_toast("Time to laugh!", pyjokes.get_joke(), duration = 20)
    time.sleep(1800)