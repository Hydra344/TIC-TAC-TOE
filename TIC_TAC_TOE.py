import tkinter as tk

root = tk.Tk()
root.configure(background='#2b2b2b')
root.title("TIC TAC TOE")
Winner = ""
P = "X"

def Button(Z):
    global Winner
    global Arr
    global P
    Arr[Z].configure(text=P)
    Arr[Z]['state'] = "disabled"
    if P == "X":
        P = "O"
        LC['text'] = "Current Player: " + P
    else:
        P = "X"
        LC['text'] = "Current Player: " + P

    #Reihe
    if B0.cget('text') == B1.cget('text') == B2.cget('text'):
        Winner = B0.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD

    if B3.cget('text') == B4.cget('text') == B5.cget('text'):
        Winner = B3.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD
    if B6.cget('text') == B7.cget('text') == B8.cget('text'):
        Winner = B6.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD

    #Spalte
    if B0.cget('text') == B3.cget('text') == B6.cget('text'):
        Winner = B0.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD
    if B1.cget('text') == B4.cget('text') == B7.cget('text'):
        Winner = B1.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD
    if B2.cget('text') == B5.cget('text') == B8.cget('text'):
        Winner = B2.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD

    #Diagonal
    if B0.cget('text') == B4.cget('text') == B8.cget('text'):
        Winner = B0.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD

    if B2.cget('text') == B4.cget('text') == B6.cget('text'):
        Winner = B2.cget('text')
        WinnerD = Winner
        LW['text'] = "Winner is: " + WinnerD

    if Winner == "":
        V = 0
        for i in range(9):
            if Arr[V].cget('text') == "X" or Arr[V].cget('text') == "O":
                V = V + 1
            if V == 9:
                Winner = "Draw"
                WinnerD = Winner
                LW['text'] = "Winner is: " + WinnerD




    if Winner != "":
        Z = 1
        Winner = ""
        for i in range(9):
            Arr[i]['text'] = Z
            Arr[i]['state'] = "normal"
            Z = Z + 1

QuitB = tk.Button(height=1,width=18,borderwidth=10, text="Quit",bg=('#2b2b2b'),fg=('#ff0059'),font=('Arial'),command=lambda: root.destroy())

LA = tk.Label(text=("Tic Tac Toe"),height=1,width=10,bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial'))
LW = tk.Label(text=(""),height=1,width=15,bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial'))
LC = tk.Label(text=("Current Player: "+ P),height=1,width=20,bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial'))

B0 = tk.Button(height=1,width=3,text="1",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(0))
B1 = tk.Button(height=1,width=3,text="2",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(1))
B2 = tk.Button(height=1,width=3,text="3",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(2))

B3 = tk.Button(height=1,width=3,text="4",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(3))
B4 = tk.Button(height=1,width=3,text="5",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(4))
B5 = tk.Button(height=1,width=3,text="6",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(5))

B6 = tk.Button(height=1,width=3,text="7",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(6))
B7 = tk.Button(height=1,width=3,text="8",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(7))
B8 = tk.Button(height=1,width=3,text="9",bg=('#2b2b2b'),fg=('#03a1fc'),font=('Arial',100), command=lambda: Button(8))

Arr = [B0, B1, B2, B3, B4, B5, B6, B7, B8]

QuitB.grid(row=0, column =1)
LA.grid(row=0, column =2)

LC.grid(row=1, column =1)
LW.grid(row=1, column =2)

B0.grid(row=2, column =1)
B1.grid(row=2, column =2)
B2.grid(row=2, column =3)

B3.grid(row=3, column =1)
B4.grid(row=3, column =2)
B5.grid(row=3, column =3)

B6.grid(row=4, column =1)
B7.grid(row=4, column =2)
B8.grid(row=4, column =3)

root.mainloop()
