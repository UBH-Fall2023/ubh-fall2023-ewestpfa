##boyidiot all rights reserved

'''
DISCLAIMER:
        This project's GUI is based on the tkinter and pillow interface

        We do not own this interface and are using it for non-commercial purposes
'''

import tkinter as tk
import parseResponse as pr
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Tell A Joke")
try:
    window.iconbitmap("icons/Tbh.ico")
except:
    pass
tempimg= Image.open("bgimage.png")
BGIMAGE = ImageTk.PhotoImage(tempimg)
BACKGROUND_COLOR="#FEF2FF"
ACCENT_COLOR="#7eabca"
DARK_ACCENT_COLOR="#3a6c8f"
FONT_COLOR="#f8f8ff"
FONT_FAMILY=("Century Gothic", 11 )
FONT_BOLD=("Century Gothic", 11, "bold")
WIDTH = 500
HEIGHT = 360
window.geometry(str(WIDTH)+"x"+str(HEIGHT))
window.resizable(False,False)
chatframe = tk.Label(window, image=BGIMAGE, bg='white')
chatframe.image = BGIMAGE
chatframe.place(x=WIDTH/2, y=HEIGHT/2)
scrollable = tk.Canvas(chatframe)
BUTTON_HEIGHT = 1
BUTTON_WIDTH = 20
INPUT_WIDTH = 50
sent = ""


def send():
    global sent
    if input.get().lower()[0:18] =="i don't like jokes" :
        window.destroy()
    text_box.delete("all")
    sent = input.get() +"\n"
    text_box.create_image(10, 10, anchor="center", image=BGIMAGE)
    text_box.create_text(window.winfo_width()*.9,window.winfo_height()*.12,text="You: ", anchor=tk.E, fill=FONT_COLOR, font=FONT_BOLD)
    text_box.create_text(window.winfo_width()*.9,window.winfo_height()*.14,text=sent, width=(window.winfo_width())*2/3,  anchor=tk.NE, fill=FONT_COLOR, font=FONT_FAMILY)
    text_box.pack(fill=tk.BOTH)
    window.after(500, respond)
    input.delete(0,"end")


def respond():
    global sent
    if(sent != ""):
        response = pr.getResponse(sent)
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2.4, text="boyidiot's Neural Network: ",
                         width=(window.winfo_width()) * 2 / 3, anchor=tk.W,fill=FONT_COLOR, font=FONT_BOLD)
    text_box.create_text(window.winfo_width() * .1, window.winfo_height() / 2.2, text=response, font=FONT_FAMILY,
                         width=(window.winfo_width()) * 2 / 3, anchor=tk.NW,fill=FONT_COLOR)

    text_box.pack(fill=tk.BOTH)


chatframe.pack()
labelBorder = tk.Frame(bg=ACCENT_COLOR)
inputLabel = tk.Label(text="↓ Talk to me and I'll tell you a joke! ↓")
input = tk.Entry(master=labelBorder,width = INPUT_WIDTH,highlightthickness=2,highlightcolor=DARK_ACCENT_COLOR, bd=0, font=FONT_FAMILY)
scrollable.pack()
inputLabel.pack()
labelBorder.pack()
input.pack(fill="both", expand=True,padx=2,pady=2)

enter = tk.Button(text="Send", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, command = send, font=FONT_BOLD)
enter.pack()


def hitenter(event):
    send()

window.bind('<Return>', hitenter)


text_box=tk.Canvas(master=scrollable, width=WIDTH)
text_box.create_image(10,10,anchor="center",image=BGIMAGE)

text_box.create_text(WIDTH/2,HEIGHT/3,text="Welcome to boyidiot's totally advanced (not really) AI chatbot that will tell you jokes based on what you tell it! Let's get started, hello!", anchor=tk.N, width=WIDTH*(2/3),fill=FONT_COLOR, font=FONT_FAMILY)
text_box.pack(fill=tk.BOTH)
window.mainloop()