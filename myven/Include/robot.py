import win32com.client as cl
while True:
    speaker=cl.Dispatch("sapi.spvoice")
    speaker.speak(input("what do u wnna say:"))
