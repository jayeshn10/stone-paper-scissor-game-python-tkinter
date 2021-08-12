import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Stone Paper Scissors Game")
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    if (human_choice == comp_choice):
        print("Tie")
    elif (human_choice == 'stone' and comp_choice == 'scissor'):
        print("You win")
        USER_SCORE += 1
    elif (human_choice == 'paper' and comp_choice == 'stone'):
        print("You win")
        USER_SCORE += 1
    elif (human_choice == 'scissor' and comp_choice == 'paper'):
        print("You win")
        USER_SCORE += 1
    else:
        print("Comp wins")
        COMP_SCORE += 1
    text_area = tk.Text(master=window, height=12, width=30, bg="#e8eced")
    text_area.grid(column=0, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(
        uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)

    text_area.insert(tk.END, answer)

    if (USER_SCORE == 10 or COMP_SCORE == 10):

        if (USER_SCORE == 10):
            answer2 = "You Win"
            text_area.delete("1.0", "end")
            text_area.insert(tk.END, answer2)
        elif (COMP_SCORE == 10):
            answer3 = "Computer Win"
            text_area.delete("1.0", "end")
            text_area.insert(tk.END, answer3)
        else:
            pass
        USER_SCORE = 0
        COMP_SCORE = 0


def random_computer_choice():
    rdm = random.choice(['stone', 'paper', 'scissor'])
    return rdm


def stone():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'stone'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text="      Stone       ", bg="#888c8d", command=stone)
button1.grid(column=0, row=1)
button2 = tk.Button(text="       Paper      ", bg="#f2eecb", command=paper)
button2.grid(column=0, row=2)
button3 = tk.Button(text="      Scissor     ", bg="#d2d9db", command=scissor)
button3.grid(column=0, row=3)
window.mainloop()
