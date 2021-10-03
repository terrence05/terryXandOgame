import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
win=tk.Tk()
win.title("Tic tac toc")
global value,cO,Cx,button1, button2, button3, button4, button5, button6, button7, button8, button9
value=True
cO=0
cX=0
Buttons=tk.StringVar()
def Winnercheak(b1,b2,b3,b4,b5,b6,b7,b8,b9):
    if (b1['text'] =='X'and b5['text'] =='X' and b9['text'] =='X'):
        mb.showinfo(title="winner", message="Player X win the game")

    elif b1['text'] =='X' and b2['text'] =='X' and b3['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b4['text'] =='X' and b5['text'] =='X' and b6['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b7['text'] =='X' and b8['text'] =='X' and b9['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b1['text'] =='X' and b4['text'] =='X' and b7['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b2['text'] =='X' and b5['text'] =='X' and b8['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b3['text'] =='X' and b6['text']=='X' and b9['text'] =='X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif b3['text']== 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        mb.showinfo(title="winner", message="Player X win the game")

    elif button1['text'] != '' and button2['text'] != '' and button3['text'] != '' and button4['text'] != '' and \
            button5['text'] != '' and button6['text'] != '' and button7['text'] != '' and button8['text'] != '' and \
            button9['text'] != '':
        mb.showerror(title="DRAW", message="Match is DRAW")
def Winnercheak1(b1,b2,b3,b4,b5,b6,b7,b8,b9):
    if (b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'):
        mb.showinfo(title="winner", message="Player O win the game")
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text']== 'O':
        mb.showinfo(title="winner", message="Player O win the game")
    elif button1['text'] != '' and button2['text'] != '' and button3['text'] != '' and button4['text'] != '' and \
            button5['text'] != '' and button6['text'] != '' and button7['text'] != '' and button8['text'] != '' and \
            button9['text'] != '':
        mb.showinfo(title="DRAW", message="Match is DRAW")
def cheak(Buttons):
    global  button1, button2, button3, button4, button5, button6, button7, button8, button9
    global value,cO,cX
    if Buttons['text']=='' and value==True:
        Buttons['text']="X"
        value=False
        Winnercheak(button1, button2, button3, button4, button5, button6, button7, button8, button9)

    elif Buttons['text']=='' and value==False:
        value=True
        Buttons['text']='O'
        Winnercheak1(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    elif (Buttons['text']=='X' or Buttons['text']=='O') and value==False:
        cO=cO+1
        mb.showinfo(title="Rules", message="if count=3 you will lose")
        mb.showwarning(title="Wronginput",message="plese enter on next button player O count=%d"%(cO))
        if cO>=3:
            mb.showinfo(title="Limit over", message="Player %s Lose the game" % ('O'))
            win.destroy()
    elif (Buttons['text']=='O' or Buttons['text']=='X') and value==True:
        cX=cX+1
        mb.showinfo(title="Rules", message="if count=3 you will lose")
        mb.showwarning(title="Wronginput",message="plese enter on next button player X count=%d"%(cX))
        if cX >=3:
            mb.showinfo(title="Limit over",message="Player %s Lose the game"%('X') )
            win.destroy()

global set2,reset,exi
def tictactow():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button1))
    button1.grid(row=0, column=0)
    button2 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button2))
    button2.grid(row=0, column=1)
    button3 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button3))
    button3.grid(row=0, column=2)
    button4 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button4))
    button4.grid(row=1, column=0)
    button5 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button5))
    button5.grid(row=1, column=1)
    button6 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button6))
    button6.grid(row=1, column=2)
    button7 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button7))
    button7.grid(row=2, column=0)
    button8 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button8))
    button8.grid(row=2, column=1)
    button9 = tk.Button(win, text='', width=10, height=3, font=('Times 26 bold'), bg='black', fg='white',
                        command=lambda: cheak(button9))
    button9.grid(row=2, column=2)


def reset1():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    if button1['text']=='' and  button2['text']=='' and button3['text']=='' and button4['text']=='' and button5['text']=='' and button6['text']=='' and button7['text']=='' and button8['text']=='' and button9['text']=='':
        mb.showerror(title="Reset",message="please start the game first")
    else:
        global set2, reset, exi
        set2.grid(row=3, column=0)
        exi.grid(row=3, column=1)
        reset.grid(row=3, column=2)
        win.update()
        tictactow()
def set():
    global set2, reset, exi
    set2.grid(row=3,column=0)
    exi.grid(row=3,column=1)
    reset.grid(row=3,column=2)
    win.update()
    tictactow()
def exit():
    a=mb.askyesno(title="Exit",message="Do You Want To Exit")
    if a==True:
     win.destroy()
def Game():
    global set2, reset, exi
    reset=tk.Button(win,text='Reset',width=5,font=('Times 26 bold'),bg='skyblue',fg='black',command=reset1)
    reset.grid(row=0,column=0)
    set2=tk.Button(win,text='Start',width=5,font=('Times 26 bold'),bg='skyblue',fg='black',command=set)
    set2.grid(row=0,column=6)
    exi=tk.Button(win,text='Exit',width=5,font=('Times 26 bold'),bg='skyblue',fg='black',command=exit)
    exi.grid(row=0,column=3)
    win.geometry('1920x1080+0+0')
    win.configure(bg='grey')
Game()
win.mainloop()
