import time
from plyer import notification

user_input=input("When do you want us to notify you: ")

while True:
    t = time.strftime("%I:%M %p")
    if str(t) == str(user_input):
        notification.notify(title="DRINK WATER", message="its been five hours pls drink water", timeout=2)
        break
