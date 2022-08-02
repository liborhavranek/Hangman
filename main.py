import tkinter.messagebox
from tkinter import *
import random

life = 7
number_of_games = 0

window = Tk()
window.title("Hangman", )
window.config(background="light blue")
hangman_label = Label(text="Hangman", font=('Arial', 60), background="light blue", highlightthickness=0)
hangman_label.grid(column=0, row=0, columnspan=3)
points_label = Label(text=f"Počet uhodnutych slov: {number_of_games}",
                          font=('Arial', 20),
                          background="light blue",
                          highlightthickness=0)
points_label.grid(column=0, row=1, columnspan=3)

hangman_canvas = Canvas(window, width=520, height=320, background="light blue", highlightthickness=0)
hangman_0_image = PhotoImage(file="art/hangman_0.png")
hangman_1_image = PhotoImage(file="art/hangman_1.png")
hangman_2_image = PhotoImage(file="art/hangman_2.png")
hangman_3_image = PhotoImage(file="art/hangman_3.png")
hangman_4_image = PhotoImage(file="art/hangman_4.png")
hangman_5_image = PhotoImage(file="art/hangman_5.png")
hangman_6_image = PhotoImage(file="art/hangman_6.png")
hangman_7_image = PhotoImage(file="art/hangman_7.png")
hangman_win_image = PhotoImage(file="art/win.png")
hangman_canvas.create_image(260, 160, image=hangman_7_image)
hangman_canvas.grid(column=0, row=2, padx=20, columnspan=3)

words = ["aj"]

random_word = random.choice(words)
print(random_word)

word_letters = []

for letter in random_word:
	word_letters.append(letter)


display = []

for _ in range(len(word_letters)):
	display.append("_")


canvas_text = Canvas(window, width=520, height=120, background="light green", highlightthickness=2, highlightbackground="black")
text = canvas_text.create_text(260, 60, text=f"{' '.join(display)}", fill="black", font=('Arial', 30))
canvas_text.grid(column=0, row=3, pady=10, columnspan=3)


separation_label = Label(text="Vloz písmeno: ", font=('Arial', 40), background="light blue", highlightthickness=0)
separation_label.grid(column=0, row=4)


def win():
	if word_letters == display:
		hangman_canvas.create_image(260, 160, image=hangman_win_image)
		reset()


def loose():
	global life
	if entry_label.get() not in word_letters:
		life -= 1
		if life == 6:
			hangman_canvas.create_image(260, 160, image=hangman_6_image)
		elif life == 5:
			hangman_canvas.create_image(260, 160, image=hangman_5_image)
		elif life == 4:
			hangman_canvas.create_image(260, 160, image=hangman_4_image)
		elif life == 3:
			hangman_canvas.create_image(260, 160, image=hangman_3_image)
		elif life == 2:
			hangman_canvas.create_image(260, 160, image=hangman_2_image)
		elif life == 1:
			hangman_canvas.create_image(260, 160, image=hangman_1_image)
		elif life == 0:
			hangman_canvas.create_image(260, 160, image=hangman_0_image)

def reset():
	global number_of_games
	result = tkinter.messagebox.askquestion(("new game", "Are you sure you want to start a new game ?"))
	if result == "Yes":
		number_of_games += 1
		print(number_of_games)

def send():

	for position in range(len(random_word)):
		pismenko = random_word[position]
		if pismenko == entry_label.get():
			display[position] = pismenko
			canvas_text.itemconfig(text, text=f"{' '.join(display)}")
		win()
	loose()

entry_label = Entry(window, font=('Arial', 25), width=10)
entry_label.grid(column=1, row=4)

send_button = Button(window, text="Odeslat", command=send)
send_button.grid(column=2, row=4, padx=10)

window.mainloop()







