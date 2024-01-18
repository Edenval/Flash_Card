from tkinter import *
import json
import csv
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_learn_dict = {}
words_to_remove = []
words_to_remove2 = []
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)


def generate():
    global current_card, flip_timer, words_learn_dict
    global words_to_remove, words_to_remove2
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #print(current_card)
    # french = kaka["French"]
    # english = kaka["English"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(front, image=cardF)

    flip_timer = window.after(3000, card_flip)
    try:
        data2 = pandas.read_csv("words_to_learn.csv")
        to_learn2 = data2.to_dict(orient="records")
    except FileNotFoundError:
        current_card = random.choice(to_learn)
        print("This is using french_words")
    else:
        current_card = random.choice(to_learn2)
        print("This is using new words")
    finally:
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")




def is_known():
    print(current_card)
    to_learn.remove(current_card)
    print(current_card)
    print(len(to_learn))
    print(to_learn)
    pd = pandas.DataFrame(to_learn)
    pd.to_csv("words_to_learn.csv", index=False)
    generate()


#TODO WE NEED TO MAKE A NEW FUNCTION TO PASS IN THE NEW ENG TEXT EVERY 3 SEC
#We click the button, it starts French, then 3 sec later it becomes Eng, click button resets

def card_flip():

    text_to_eng = canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    background_to_cardB = canvas.itemconfig(front, image=cardB)
    title_to_eng = canvas.itemconfig(card_title, text="English", fill="white")

window = Tk()
window.title("Flashy")

flip_timer = window.after(3000, card_flip)


cardB = PhotoImage(file="./images/card_back.png")
window.config(padx=50,pady=50, bg="#B1DDC6") #background is standard attribute widget


#CANVAS IMAGE
canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6") #canvas takes positions

cardF = PhotoImage(file="./images/card_front.png")
front = canvas.create_image(400, 263, image=cardF) #x and y position
canvas.grid(column=0, row=0, columnspan=2)

#CANVAS TEXT
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="gen", font=("Ariel", 60, "bold"))


#BUTTONS
image_r = PhotoImage(file="./images/right.png")
button_r = Button(image=image_r, highlightthickness=0, borderwidth=0, command=is_known)
button_r.grid(column=1, row=1)

image_w = PhotoImage(file="./images/wrong.png")
button_w = Button(image=image_w, highlightthickness=0, borderwidth=0, command=generate)
button_w.grid(column=0, row=1)

#window.after_cancel(card_flip)



generate()
#card_flip()
window.mainloop()