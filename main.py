##boyidiot all rights reserved

'''
DISCLAIMER:
        This project's GUI is based on the tkinter interface

        We do not own this interface and are using it for non-commercial purposes
'''

import tkinter as tk
import parseResponse as pr
window = tk.Tk()
window.title("Tell A Joke")

WIDTH = 500
HEIGHT = 360
window.geometry(str(WIDTH)+"x"+str(HEIGHT))
window.resizable(False,False)
chatframe = tk.Frame(window)
scrollable = tk.Canvas(chatframe)
BUTTON_HEIGHT = 1
BUTTON_WIDTH = 20
INPUT_WIDTH = 50
BACKGROUND_COLOR="#FFFFFF"
sent = ""


def send():
    global sent
    text_box.delete("all")
    sent = input.get() +"\n"
    text_box.create_text(window.winfo_width()*.9,window.winfo_height()*.12,text="You: ", anchor=tk.E)
    text_box.create_text(window.winfo_width()*.9,window.winfo_height()*.2,text=sent, width=(window.winfo_width())*2/3, anchor=tk.E)
    text_box.pack(fill=tk.BOTH)
    window.after(500, respond)
    input.delete(0,"end")

def respond():
    global sent
    if(sent != ""):
        response = pr.getResponse(sent)
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2.4, text="boyidiot's Neural Network: ", width=(window.winfo_width()) * 2 / 3, anchor=tk.W,fill="#4df0ff")
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2, text=response, width=(window.winfo_width()) * 2 / 3, anchor=tk.W)
    text_box.pack(fill=tk.BOTH)



chatframe.pack()
inputLabel = tk.Label(text="↓ Talk to me and I'll tell you a joke! ↓")
scrollable.pack()
input = tk.Entry(width = INPUT_WIDTH)

inputLabel.pack()
inputLabel.pack()
input.pack(fill=tk.BOTH)
enter = tk.Button(text="Send", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, command = send)
enter.pack()

def hitenter(event):
    send()
window.bind('<Return>', hitenter)

text_box=tk.Canvas(master=scrollable, width=WIDTH)
text_box.create_text(WIDTH/2,HEIGHT/2.5,text="Welcome to boyidiot's totally advanced AI chatbot that will tell you jokes based on what you tell it! Let's get started, hello!", anchor=tk.N, width=WIDTH*(2/3))
text_box.pack(fill=tk.BOTH)
window.mainloop()