import tkinter as tk
import parseResponse as pr
import time
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
send = ""


def send():
    text_box.delete("all")
    sent = input.get() +"\n"
    text_box.create_text(window.winfo_width()*.9,window.winfo_height()*.2,text=sent, width=(window.winfo_width())*2/3, anchor=tk.E)
    text_box.pack(fill=tk.BOTH)
    window.after(500, respond)


def respond():
    global send
    response = (send)
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2, text=response, width=(window.winfo_width()) * 2 / 3, anchor=tk.W)
    text_box.pack(fill=tk.BOTH)



hello = tk.Label(text="Want to hear a joke?")
hello.pack()
chatframe.pack()
inputLabel = tk.Label(text="Talk to me!")
scrollable.pack()
input = tk.Entry(width = INPUT_WIDTH)

inputLabel.pack()
inputLabel.pack()
input.pack(fill=tk.BOTH)
enter = tk.Button(text="Send", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, command = send)
enter.pack()

text_box=tk.Canvas(master=scrollable, width=LEFTRIGHT_WIDTH)

window.mainloop()