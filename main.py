BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
new_vocabulary = {}
data_list = {}


try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data =pandas.read_csv("data/Kaydedilen işlemler - Kaydedilen işlemler.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")


def pass_word():
    global new_vocabulary,wait_time
    window.after_cancel(wait_time)
    new_vocabulary = random.choice(data_list)
    english_word = new_vocabulary["İngilizce"]
    canvas.itemconfig(make,image=front_image)
    canvas.itemconfig(word,text=english_word,fill="black")
    canvas.itemconfig(tıtle,text="English", fill="black")
    wait_time=window.after(3000, turn_card)

def turn_card():
    canvas.itemconfig(make,image=back_image)
    canvas.itemconfig(tıtle, text="Turkısh", fill="white")
    turkıs_word = new_vocabulary["Turkısh"]
    canvas.itemconfig(word,text = turkıs_word, fill="white")

def know_word():
   data_list.remove(new_vocabulary)
   data=pandas.DataFrame(data_list)
   data.to_csv("data/to_to_learn list")
   pass_word()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

wait_time = window.after(3000, turn_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0  )
back_image = PhotoImage(file="images/card_back.png")
front_image =PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

make = canvas.create_image(410,273, image=front_image)
tıtle= canvas.create_text(400,150, text="English", font=("Arial", 40, "italic"))
word = canvas.create_text(400,265, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_image, highlightthickness=0, command=know_word)
right_button.grid(row=1, column=1, columnspan=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=pass_word)
wrong_button.grid(row=1, column=0, columnspan=1)

pass_word()









window.mainloop()

