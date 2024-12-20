#Rock Paper Scissors
import sys
import random

def y():
    print("*"*90)

def main():
    karsilama()
    basla()

#karşılama, isim alma
def karsilama():
    print("#"*50)
    print("#"*13,"Welcome to RPS Game!!","#"*14)
    print("#"*50)


#oyunu başlatma
def basla():
    op=0
    pp=0
    name= input("What is your name?: ").capitalize()
    while True:
        oyuncu_p, program_p = zorluk()
        op+=oyuncu_p
        pp+=program_p
        print(f"{name}'s score: {op}, Program's score: {pp}")
        y()

        if yeniden(op, pp, name):
            pass
def zorluk():
    oyuncu_p=0
    program_p=0
    while True:
        derece= input("Do you wanna play hard mode(h) or easy mode(e) or normal mode(n): ").lower()
        y()
        if derece=="h" or derece=="hard":
            print("According to your answer, the probability of a move that will defeat you will be increased!")
            oyuncu_p, program_p=zor()
            break
        elif derece=="e" or derece=="easy":
            print("According to your answer, the probability of a move that will defeat you will be decreased!")
            oyuncu_p, program_p=kolay()
            break
        elif derece=="n" or derece=="normal":
            print("A normal gameplay. The program won't read your answer for move.")
            oyuncu_p, program_p=normal()
            break
        else:
            print("Did you write it wrong? Hard for 'h', Easy for 'e', normal for 'n': " )

    return oyuncu_p, program_p

#zor
def zor():
    oyuncu_p=0
    program_p=0
    while True:
        secim= input("Rock, Paper, Scissors! CHOOSE ONE!: ").lower()
        if secim == "rock":
            print(f"Your choice: {secim}")
            oyuncu_p, program_p= ihtimal_rock(secim, oyuncu_p, program_p)
            break
        elif secim == "paper":
            print(f"Your choice: {secim}")
            oyuncu_p, program_p = ihtimal_paper(secim, oyuncu_p, program_p)
            break
        elif secim == "scissors":
            print(f"Your choice: {secim}")
            oyuncu_p, program_p = ihtimal_scissors(secim, oyuncu_p, program_p)
            break
        else:
            print("*"*50)
            print("Don't understand what you mean please choose one\n")
    return oyuncu_p, program_p

def ihtimal_rock(secim,oyuncu_p, program_p):
    rps=["rock", "paper","scissors"]
    ihtimal=[0.3, 0.6, 0.1]
    ran = random.choices(rps, weights=ihtimal)
    print(f"Program's choice: ", ran[0])
    oyuncu_p, program_p=kontrol(secim,ran[0],oyuncu_p, program_p)
    return oyuncu_p, program_p

def ihtimal_paper(secim,oyuncu_p, program_p):
    rps=["rock", "paper","scissors"]
    ihtimal=[0.1, 0.3, 0.6]
    ran = random.choices(rps, weights=ihtimal)
    print(f"Program's choice: ", ran[0])
    oyuncu_p, program_p = kontrol(secim,ran[0], oyuncu_p, program_p)
    return oyuncu_p, program_p

def ihtimal_scissors(secim, oyuncu_p, program_p):
    rps= ["rock", "paper","scissors"]
    ihtimal=[0.6, 0.1, 0.3]
    ran = random.choices(rps, weights=ihtimal)
    print(f"Program's choice:", ran[0])
    oyuncu_p, program_p = kontrol(secim,ran[0],oyuncu_p, program_p)
    return oyuncu_p, program_p

#kolay
def kolay():
    oy_p= 0
    pro_p= 0
    while True:
        secim = input("Rock, Paper, Scissors! CHOOSE ONE!: ")
        if secim== "rock":
            print(f"Your choice: {secim}")
            oy_p, pro_p=k_rock(secim, oy_p, pro_p)
            break
        elif secim == "paper":
            print(f"Your choice: {secim}")
            oy_p, pro_p = k_paper(secim, oy_p, pro_p)
            break
        elif secim == "scissors":
            print(f"Your choice: {secim}")
            oy_p, pro_p = k_scissors(secim, oy_p, pro_p)
            break
        else:
            print("*"*50)
            print("Didn't understant what you mean please choose the givin choices!\n")
    return oy_p, pro_p

def k_rock(secim, oy_p, pro_p):
    rps=["rock", "paper", "scissors"]
    ihtimal=[0.3, 0.1, 0.6]
    ran= random.choices(rps, weights=ihtimal)
    print("Program's choice: ", ran[0])
    oy_p, pro_p=kontrol(secim, ran[0], oy_p, pro_p)
    return oy_p, pro_p
def k_paper(secim, oy_p, pro_p):
    rps=["rock", "paper", "scissors"]
    ihtimal = [0.6, 0.3, 0.1]
    ran = random.choices(rps, weights=ihtimal)
    print("Program's choice: ", ran[0])
    oy_p, pro_p=kontrol(secim, ran[0], oy_p, pro_p)
    return oy_p, pro_p
def k_scissors(secim, oy_p, pro_p):
    rps = ["rock", "paper", "scissors"]
    ihtimal = [0.1, 0.6, 0.3]
    ran= random.choices(rps, weights=ihtimal)
    print("Program's choice: ", ran[0])
    oy_p, pro_p=kontrol(secim, ran[0], oy_p, pro_p)
    return oy_p, pro_p

#normal
def normal():
    op=0
    pp=0
    while True:
        secim= input("Rock, Paper, Scissors. CHOOSE ONE!: ").lower()
        if secim =="rock":
            print(f"Your choice: {secim}")
            op, pp = normal_ihtimal(secim,op,pp)
            break
        elif secim =="paper":
            print(f"Your choice: {secim}")
            op,pp = normal_ihtimal(secim, op,pp)
            break
        elif secim == "scissors":
            print(f"Your choice: {secim}")
            op,pp = normal_ihtimal(secim,op,pp)
            break
        else:
            print("*"*50)
            print("Don't understand what you mean please choose one!\n")
    return op, pp
def normal_ihtimal(secim,op,pp):
    rsc=["rock","paper","scissors"]
    ran=random.choice(rsc)
    print(f"Program says: {ran}")
    op, pp = kontrol (secim,ran,op,pp)
    return op, pp

#kontrol
def kontrol(secim, ran,oyuncu_p=0, program_p=0):
    if (secim == "rock" and ran == "rock") or (secim == "paper" and ran == "paper") or (secim == "scissors" and ran == "scissors"):
        kazanan= "draw"
        oyuncu_p=1
        program_p=1
        print("Draw!")
    elif (secim == "rock" and ran == "scissors") or (secim == "scissors" and ran == "paper") or (secim == "paper" and ran == "rock"):
        kazanan= "oyuncu"
        oyuncu_p=2
        print(f"Player won! Congrats!")
    elif (secim == "rock" and ran == "paper") or (secim == "paper" and ran=="scissors") or (secim=="scissors" and ran=="rock"):
        kazanan= "program"
        program_p=2
        print("Program won!")
    return oyuncu_p, program_p

#yeniden?
def yeniden(op, pp,name):
    while True:
        yeniden= input("Wanna play again?: (y)es/(n)o ")
        if yeniden == "y" or yeniden == "yes":
            return True
        elif yeniden == "n" or yeniden == "no":
            print("-"*20)
            print(f"The Final Scores:\n{name}= {op}\nThe Program= {pp}")
            print("-"*20)
            if op>pp:
                print(f"The winner is {name}!")
            elif op<pp:
                print("The winner is Program!")
            elif op==pp:
                print("The match ended in a draw!")
            print(f"Thanks for playing {name}! See you later.")
            y()
            sys.exit()
        else:
            print("what did you mean? yes/no: ")

if __name__ == "__main__":
    main()