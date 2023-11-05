##boyidiot all rights reserved

import tkinter as tk
import parseResponse as pr
window = tk.Tk()
window.title("Tell A Joke")


window.geometry("500x360")
window.resizable(False,False)
chatframe = tk.Frame(window)
scrollable = tk.Canvas(chatframe)
LEFTRIGHT_WIDTH =500
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


def respond():
    global sent
    if(sent != ""):
        response = pr.getResponse(sent)
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2.5, text="boyidiot's Neural Network: ", width=(window.winfo_width()) * 2 / 3, anchor=tk.W)
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

text_box=tk.Canvas(master=scrollable, width=LEFTRIGHT_WIDTH)
text_box.create_text(chatframe.winfo_width()/2,chatframe.winfo_height()/2,text="Welcome to boyidiot's totally advanced AI chatbot that will tell you jokes based on what you tell it! Let's get started, hello!", anchor=tk.N, width=window.winfo_width()*2/3)
text_box.pack(fill=tk.BOTH)
window.mainloop()