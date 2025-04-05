from tkinter import *
from SoccerAPI import *
from SoccerAPI import getPlayerData
"""window = Tk()
window.title("Hello Tkinter")
button_1 = Button(text="submit")
button_1.pack()
label_1 = Label(text= "this is a label")
label_1.pack()
entry_1 = Entry()
entry_1.pack()
window.mainloop()"""
smallfont = ["Helvetica", 14]
mediumfont = ["Helvetica", 18]
bigfont = ["Helvetica", 30]
window = Tk()
window.config(bg= "red")
window.title("BarcaDex")

instuction_label = Label(window,text="Enter a player's jersy number")
instuction_label.config(bg= "red",fg= "black", font= smallfont)
instuction_label.pack()

jersy_entry = Entry(window)
jersy_entry.pack()

'''showplayerbutton = Button(window, text= "Show player")
showplayerbutton.config(bg= "blue",fg= "white", font= smallfont)
showplayerbutton.pack()'''

namelbl = Label(window, text= "Name")
namelbl.config(bg= "red",fg= "black", font= smallfont)
namelbl.pack()
namelbl = Label(window, text= "???")
namelbl.config(bg= "red",fg= "black", font= smallfont)
namelbl.pack()

positionlbl = Label(window, text= "position")
positionlbl.config(bg= "red",fg= "black", font= smallfont)
positionlbl.pack()
positionlbl = Label(window, text= "???")
positionlbl.config(bg= "red",fg= "black", font= smallfont)
positionlbl.pack()

citsenship = Label(window, text= "citsenship")
citsenship.config(bg= "red",fg= "black", font= smallfont)
citsenship.pack()
citsenship = Label(window, text= "???")
citsenship.config(bg= "red",fg= "black", font= smallfont)
citsenship.pack()

appearances = Label(window, text= "appearances")
appearances.config(bg= "red",fg= "black", font= smallfont)
appearances.pack()
appearances = Label(window, text= "???")
appearances.config(bg= "red",fg= "black", font= smallfont)
appearances.pack()

goals = Label(window, text= "goals")
goals.config(bg= "red",fg= "black", font= smallfont)
goals.pack()
goals = Label(window, text= "???")
goals.config(bg= "red",fg= "black", font= smallfont)
goals.pack()

resetbtn = Button(window, text= "reset")
resetbtn.config(bg= "blue",fg= "white", font= smallfont)
resetbtn.pack()

def showplayer():
    jersynumber = int(jersy_entry.get())
    playerdata = getPlayerData(jersynumber)
    namelbl.config(text= playerdata["name"], fg= "Blue")
    positionlbl.config(text= playerdata["position"], fg= "Blue")
    citsenship.config(text= playerdata["citizenship"], fg= "Blue")
    appearances.config(text= playerdata["appearances"], fg= "Blue")
    goals.config(text= playerdata["goals"], fg= "Blue")

def reset():
    namelbl.config(text= '???', fg= 'black')
    positionlbl.config(text= '???', fg= 'black')
    citsenship.config(text= '???', fg= 'black')
    appearances.config(text= '???', fg= 'black')
    goals.config(text= '???', fg= 'black')
    
showplayerbutton=Button(window, text='show player')
showplayerbutton.config(bg= "blue",fg= "white", font= smallfont, command=showplayer)
showplayerbutton.pack()

resetbtn=Button(window, text='reset')
resetbtn.config(bg= "blue",fg= "white", font= smallfont, command=reset)
resetbtn.pack()

window.mainloop()
