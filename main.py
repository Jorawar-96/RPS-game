import tkinter as tk
import random

root = tk.Tk()

root.title("Rock paper scissors")
root.geometry("700x550")
root.resizable(False,False)

win=0
tie=0
lose=0
i=0
choices = ["rock","paper","scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="\n 🧑 You : "+user_choice)
    comp_label.config(text=" 🤖 Computer : "+computer_choice)
    result_label.config(text=result_checker(user_choice,computer_choice),font=("Arial",20,"bold"))

    score_shower()
    show_round()
    
def result_checker(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "Tie"
    elif (user_choice=='rock' and  computer_choice=='scissors') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=="scissors" and computer_choice=='paper'):
        return "You win"   
    else:
        return "Computer win"

def score_shower():
    global win,tie,lose

    if result_label.cget("text")=="You win":
        win+=1
    elif result_label.cget("text")=="Computer win":
        lose+=1
    else:
        tie+=1
    
    score_label.config(text=f"\n\nScore :  Win  {win}, Tie  {tie}, Lose  {lose} ")

def show_round():
    global i
    
    i+=1
    round_label.config(text=f"Round : {i}")

def reset_btn():
    global win,lose,tie,i
    i=0
    win=0
    lose=0
    tie=0

    user_label.config(text="\n 🧑 You : ")
    comp_label.config(text="🤖 Computer : ")
    result_label.config(text="")

    round_label.config(text="Round : 0")

    score_label.config(text="\n\nScore : Win 0 , Tie 0 , Lose 0 ")

def rules_btn():

    tk.Label(root,text="Rules of Rock , Paper and Scissors are : \n 1. Rock beat Scissor  \n2. Scissor beat Paper \n3. Paper beat rock ",font=("Arial",15)).pack(pady=15)
    
tk.Label(root,text="Choose Rock , Paper and Scissors : \n",font=("Arial",15)).pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack()

round_label = tk.Label(root,text="Round : 0",font=("Arial",15))
round_label.pack()

user_label = tk.Label(root,text="\n 🧑 You : ",font=("Arial,15"))
user_label.pack()

comp_label = tk.Label(root,text="🤖 Computer : ",font=("Arial,15"))
comp_label.pack()

result_label = tk.Label(root,text="" ,font=("Arial,15"))
result_label.pack()


tk.Button(button_frame, text= " 🪨  Rock" ,width=20,font=("monospaced",15),background=("green"),command=lambda:play("rock")).grid(row=0,column=0)
tk.Button(button_frame,text= " 📄  Paper",width=20,font=("monospaced",15),background=("Red"),command=lambda:play("paper")).grid(row=0,column=1)
tk.Button(button_frame,text = "✂️  Scissors",width=20,font=("monospaced",15),background=("Blue"),command=lambda:play("scissors")).grid(row=0,column=2)

score_label = tk.Label(root,text="\n\nScore : Win 0 , Tie 0 , Lose 0 ",font=("Arial",15))
score_label.pack(pady=10)

tk.Button(root,text="Play Again(reset)",font=("Arial",15),command=lambda:reset_btn()).pack()
tk.Button(root,text="Rules",command=lambda:rules_btn(),font=("Arial",15)).pack()

root.mainloop()