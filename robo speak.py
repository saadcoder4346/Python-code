import win32com.client as cl
a=cl.dispatch("sapi.spvoice")
a.speak(input("what do u want to say?"))

