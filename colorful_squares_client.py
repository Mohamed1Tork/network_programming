# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:24:00 2023

@author: mohamed saeed
"""

import numpy as np
from tkinter import *
from tkinter import messagebox
from socket import * 
from threading import Thread 

player = 0 

def create_board():
    board = np.zeros((5 , 5))
    return board

def clicked1():
        global player
        if(btn1["bg"]=="white"):
            if(player==1):
                player=0
                btn1["bg"] = "blue"
                sendPlay(1)	
                board[0][0]=2
                print(board)
                check(board)

def clicked2():
        global player
        if(btn2["bg"]=="white"):
                if(player==1):
                        player=0
                        btn2["bg"] = "blue"
                        sendPlay(2)	
                        board[0][1]=2
                        print(board)
                        check(board)
            
def clicked3():
        global player
        if(btn3["bg"]=="white"):
                if(player==1):
                        player=0
                        btn3["bg"] = "blue"
                        sendPlay(3)	
                        board[0][2]=2
                        print(board)
                        check(board)
            
def clicked4():
        global player
        if(btn4["bg"]=="white"):
                if(player==1):
                        player=0
                        btn4["bg"] = "blue"
                        sendPlay(4)	
                        board[0][3]=2
                        print(board)
                        check(board)
            
def clicked5():
        global player
        if(btn5["bg"]=="white"):
                if(player==1):
                        player=0
                        btn5["bg"] = "blue"
                        sendPlay(5)	
                        board[0][4]=2
                        print(board)
                        check(board)
            
def clicked6():
        global player
        if(btn6["bg"]=="white"):
                if(player==1):
                        player=0
                        btn6["bg"] = "blue"
                        sendPlay(6)	    
                        board[1][0]=2
                        print(board)
                        check(board)
            
def clicked7():
        global player
        if(btn7["bg"]=="white"):
                if(player==1):
                        player=0
                        btn7["bg"] = "blue"
                        sendPlay(7)	
                        board[1][1]=2
                        print(board)
                        check(board)
            
def clicked8():
        global player
        if(btn8["bg"]=="white"):
                if(player==1):
                        player=0
                        btn8["bg"] = "blue"
                        sendPlay(8)
                        board[1][2]=2
                        print(board)
                        check(board)
            
def clicked9():
        global player
        if(btn9["bg"]=="white"):
                if(player==1):
                        player=0
                        btn9["bg"] = "blue"
                        sendPlay(9)	
                        board[1][3]=2
                        print(board)
                        check(board)  
            
def clicked10():
        global player
        if(btn10["bg"]=="white"):
                if(player==1):
                        player=0
                        btn10["bg"] = "blue"
                        sendPlay(10)	
                        board[1][4]=2
                        print(board)
                        check(board)                
        
def clicked11():
        global player
        if(btn11["bg"]=="white"):
                if(player==1):
                        player=0
                        btn11["bg"] = "blue"
                        sendPlay(11)	
                        board[2][0]=2
                        print(board)
                        check(board)
        
def clicked12():
        global player
        if(btn12["bg"]=="white"):
                if(player==1):
                        player=0
                        btn12["bg"] = "blue"
                        sendPlay(12)	
                        board[2][1]=2
                        print(board)
                        check(board)
                
def clicked13():
        global player
        if(btn13["bg"]=="white"):
                if(player==1):
                        player=0
                        btn13["bg"] = "blue"
                        sendPlay(13)	
                        board[2][2]=2
                        print(board)
                        check(board)
                        
def clicked14():
        global player
        if(btn14["bg"]=="white"):
                if(player==1):
                        player=0
                        btn14["bg"] = "blue"
                        sendPlay(14)	
                        board[2][3]=2
                        print(board)
                        check(board)
                        
def clicked15():
        global player
        if(btn15["bg"]=="white"):
                if(player==1):
                        player=0
                        btn15["bg"] = "blue"
                        sendPlay(15)	
                        board[2][4]=2
                        print(board)
                        check(board)
                                
def clicked16():
        global player
        if(btn16["bg"]=="white"):
                if(player==1):
                        player=0
                        btn16["bg"] = "blue"
                        sendPlay(16)	
                        board[3][0]=2
                        print(board)
                        check(board)
                                
def clicked17():
        global player
        if(btn17["bg"]=="white"):
                if(player==1):
                        player=0
                        btn17["bg"] = "blue"
                        sendPlay(17)	
                        board[3][1]=2
                        print(board)
                        check(board)
                                
def clicked18():
        global player
        if(btn18["bg"]=="white"):
                if(player==1):
                        player=0
                        btn18["bg"] = "blue"
                        sendPlay(18)	
                        board[3][2]=2
                        print(board)
                        check(board)
                                
def clicked19():
        global player
        if(btn19["bg"]=="white"):
                if(player==1):
                        player=0
                        btn19["bg"] = "blue"
                        sendPlay(19)	
                        board[3][3]=2
                        print(board)
                        check(board)
                                
def clicked20():
        global player
        if(btn20["bg"]=="white"):
                if(player==1):
                        player=0
                        btn20["bg"] = "blue"
                        sendPlay(20)	
                        board[3][4]=2
                        print(board)
                        check(board)
                                
def clicked21():
        global player
        if(btn21["bg"]=="white"):
                if(player==1):
                        player=0
                        btn21["bg"] = "blue"
                        sendPlay(21)	
                        board[4][0]=2
                        print(board)
                        check(board)
                                
def clicked22():
        global player
        if(btn22["bg"]=="white"):
                if(player==1):
                        player=0
                        btn22["bg"] = "blue"
                        sendPlay(22)	
                        board[4][1]=2
                        print(board)
                        check(board)  
                
def clicked23():
        global player
        if(btn23["bg"]=="white"):
                if(player==1):
                        player=0
                        btn23["bg"] = "blue"
                        sendPlay(23)	
                        board[4][2]=2
                        print(board)
                        check(board)
                
def clicked24():
        global player
        if(btn24["bg"]=="white"):
                if(player==1):
                        player=0
                        btn24["bg"] = "blue"
                        sendPlay(24)	
                        board[4][3]=2
                        print(board)
                        check(board)  
                
def clicked25():
        global player
        if(btn25["bg"]=="white"):
                if(player==1):
                        player=0
                        btn25["bg"] = "blue"
                        sendPlay(25)	
                        board[4][4]=2
                        print(board)
                        check(board) 
                


def check(board):
    # Check horizontal locations for win
    for c in range(3):
        for r in range(5):
            if (board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1)or(board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2):
                if(board[r][c] == 1):
                    win("red player")
                else:
                    win("blue player")
                return

    # Check vertical locations for win
    for c in range(5):
        for r in range(3):
            if(board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1)or(board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2):
                if(board[r][c] == 1):
                    win("red player")
                else:
                    win("blue player")
                return 
            
def win(player):
    messagebox.showinfo("winner", player +" is win")
    gui.destroy()

def sendPlay(n):
    n = str(n)
    n = n.encode()
    soc.send(n)
    
def rec():
    while True:
      p = soc.recv(10)
      applayPlay(p)

def applayPlay(p):
    p = p.decode()
    p = int(p)
    handlePlay(p)
      
def handlePlay(n):
    global player
    player = 1 
    butList[n-1]["bg"] = "red"
    array1 = board.ravel()
    array1[n-1]=1
    
board = create_board()
butList = list()
# build the GUI window 
gui = Tk()
gui.title("Colorful Squares Game Client")
gui.configure(background='black')
gui.geometry("580x460+500+100") 
# create the label for the player
lb1 = Label(gui,text="player2" ,font=('Helvetiica',15),bg='black',fg='white')
lb1.grid(row = 0)
# first line of buttons(1-5)
btn1=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked1)
btn1.grid(row=1,column=1)
btn2=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked2)
btn2.grid(row=1,column=2)
btn3=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked3)
btn3.grid(row=1,column=3)
btn4=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked4)
btn4.grid(row=1,column=4)
btn5=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked5)
btn5.grid(row=1,column=5)
# second line of buttons(6-10)
btn6=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked6)
btn6.grid(row=2,column=1)
btn7=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked7)
btn7.grid(row=2,column=2)
btn8=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked8)
btn8.grid(row=2,column=3)
btn9=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked9)
btn9.grid(row=2,column=4)
btn10=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked10)
btn10.grid(row=2,column=5)
# third line of buttons(11-15)
btn11=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked11)
btn11.grid(row=3,column=1)
btn12=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked12)
btn12.grid(row=3,column=2)
btn13=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked13)
btn13.grid(row=3,column=3)
btn14=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked14)
btn14.grid(row=3,column=4)
btn15=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked15)
btn15.grid(row=3,column=5)
# fourth line of buttons(16-20)
btn16=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked16)
btn16.grid(row=4,column=1)
btn17=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked17)
btn17.grid(row=4,column=2)
btn18=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked18)
btn18.grid(row=4,column=3)
btn19=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked19)
btn19.grid(row=4,column=4)
btn20=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked20)
btn20.grid(row=4,column=5)
# fifth line of buttons(21-25)
btn21=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked21)
btn21.grid(row=5,column=1)
btn22=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked22)
btn22.grid(row=5,column=2)
btn23=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked23)
btn23.grid(row=5,column=3)
btn24=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked24)
btn24.grid(row=5,column=4)
btn25=Button(gui,text=" ",bg="white",fg="black",width=6,height=3,font='Helvetiica',command=clicked25)
btn25.grid(row=5,column=5)


butList.append(btn1) 
butList.append(btn2)
butList.append(btn3)
butList.append(btn4)
butList.append(btn5)
butList.append(btn6)
butList.append(btn7)
butList.append(btn8)
butList.append(btn9)
butList.append(btn10)
butList.append(btn11)
butList.append(btn12)
butList.append(btn13)
butList.append(btn14)
butList.append(btn15)
butList.append(btn16)
butList.append(btn17)
butList.append(btn18)
butList.append(btn19)
butList.append(btn20)
butList.append(btn21)
butList.append(btn22)
butList.append(btn23)
butList.append(btn24)
butList.append(btn25)


soc = socket(AF_INET , SOCK_STREAM)
soc.connect(("127.0.0.1" , 12221) )

thread = Thread(target = rec )
thread.start()

gui.mainloop()



    