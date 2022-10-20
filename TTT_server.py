from cgitb import enable
from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 1
turn = 0

def win(player):
    messagebox.showinfo(title = "CONGRATULATIONS",message = f"WINNER IS {player}")
    window.destroy()

def tie():
    messagebox.showinfo(title = "OPS",message = "IT'S A TIE")
    window.destroy()
    

def check_win():
    
    global turn
    
    b1=bt1['text']
    b2=bt2['text']
    b3=bt3['text']
    b4=bt4['text']
    b5=bt5['text']
    b6=bt6['text']
    b7=bt7['text']
    b8=bt8['text']
    b9=bt9['text']
    
    if (b1==b2 and b2==b3 and b1 =='O') or (b1==b2 and b2==b3 and b1 =='X'):
        win(b1)
    elif (b4==b5 and b5==b6 and b4 =='O') or (b4==b5 and b5==b6 and b4 =='X'):
        win(b4)
    elif (b7==b8 and b8==b9 and b7 =='O') or (b7==b8 and b8==b9 and b7 =='X'):
        win(b7)
    elif (b1==b4 and b4==b7 and b1 =='O') or (b1==b4 and b4==b7 and b1 =='X'):
        win(b1)
    elif (b2==b5 and b5==b8 and b2 =='O') or (b2==b5 and b5==b8 and b2 =='X'):
        win(b2)
    elif (b3==b6 and b6==b9 and b3 =='O') or (b3==b6 and b6==b9 and b3 =='X'):
        win(b3)
    elif (b1==b5 and b5==b9 and b1 =='O') or (b1==b5 and b5==b9 and b1 =='X'):
        win(b1)
    elif (b3==b5 and b5==b7 and b3 =='O') or (b3==b5 and b5==b7 and b3 =='X'):
        win(b3)
    else: turn += 1
    
    if turn == 9:
        tie()
        
        
def clicked1():
    global player
    if (bt1['text']==" "):
        if (player == 1):
            player=2
            bt1['text']='X'
            bt1['state']=DISABLED
            disable_buttons()
            send_play(1)
        check_win()

def clicked2():
    global player
    if (bt2['text']==" "):
        if (player == 1):
            player=2
            bt2['text']='X'
            bt2['state']=DISABLED
            disable_buttons()
            send_play(2)
        check_win()
        
def clicked3():
    global player
    if (bt3['text']==" "):
        if (player == 1):
            player=2
            bt3['text']='X'
            bt3['state']=DISABLED
            disable_buttons()
            send_play(3)
        check_win()
        
def clicked4():
    global player
    if (bt4['text']==" "):
        if (player == 1):
            player=2
            bt4['text']='X'
            bt4['state']=DISABLED
            disable_buttons()
            send_play(4)
        check_win()
        
def clicked5():
    global player
    if (bt5['text']==" "):
        if player == 1:
            player=2
            bt5['text']='X'
            bt5['state']=DISABLED
            disable_buttons()
            send_play(5)
        check_win()
        
def clicked6():
    global player
    if (bt6['text']==" "):
        if( player == 1):
            player=2
            bt6['text']='X'
            bt6['state']=DISABLED
            disable_buttons()
            send_play(6)
        check_win()
        
def clicked7():
    global player
    if (bt7['text']==" "):
        if (player == 1):
            player=2
            bt7['text']='X'
            bt7['state']=DISABLED
            disable_buttons()
            send_play(7)
        check_win()
        
def clicked8():
    global player
    if (bt8['text']==" "):
        if (player == 1):
            player=2
            bt8['text']='X'
            bt8['state']=DISABLED
            disable_buttons()
            send_play(8)
        check_win()
        
def clicked9():
    global player
    if (bt9['text']==" "):
        if (player == 1):
            player = 2
            bt9['text']='X'
            bt9['state']=DISABLED
            disable_buttons()
            send_play(9)
        check_win()


def enable_buttons():
    for i in range(0,9):
        if button_list [i]['text'] == " ":
            button_list [i]['state'] = NORMAL

def disable_buttons():
    for i in range(0,9):
        button_list [i]['state'] = DISABLED

def send_play(n):
    n = str(n)
    n = n.encode() 
    conn.send(n)
    
def handle_play(n):
    global player
    n = n-1
    button_list [n]['text'] = "O"
    button_list [n]['fg'] = "black"
    button_list [n]['disabledforeground'] = "black"
    button_list [n]['state'] = DISABLED
    player = 1
    enable_buttons()
    check_win()

def apply_play(p):
    p = p.decode()
    p = int(p)
    handle_play(p)


window = Tk()

window.title('Server: Tic Tac Toe')
window.geometry('414x456')
window.resizable(False, False)



button_list = list()

bt1=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked1)
bt1.grid(row = 0, column=0)

bt2=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked2)
bt2.grid(row = 0, column=1)

bt3=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked3)
bt3.grid(row = 0, column=2)

bt4=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked4)
bt4.grid(row = 1, column=0)

bt5=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked5)
bt5.grid(row = 1, column=1)

bt6=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked6)
bt6.grid(row = 1, column=2)

bt7=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked7)
bt7.grid(row = 2, column=0)

bt8=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked8)
bt8.grid(row = 2, column=1)

bt9=Button(window, text=" ",bg="grey",fg="red", disabledforeground="red",width = 8, height = 4,font=('Helvetica','20'),command = clicked9)
bt9.grid(row = 2, column=2)

button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)

my_sock = socket(AF_INET,SOCK_STREAM)


my_sock.bind(('127.0.0.1', 5001))
my_sock.listen(1)
conn=None

def handle_client():
    global player
    global conn
    player = 1
    conn,addr = my_sock.accept()
    receive = Thread(target = receive_message, args = [conn,])
    receive.start()
    
def receive_message(c):
    while True:
        p = conn.recv(10)
        apply_play(p)

# interfaccia in cui incapsulare una funzione e che corrisponde a un thread.
# Definiamo il codice di implementazione del thread all'interno di una funzione che chiameremo handle client() 
# e che assegneremo all'interfaccia tramite il parametro target . Mentre args viene utilizzato per passare parametri all'interno del thread.
acc = Thread(target=handle_client)
acc.start()
    
window.mainloop()