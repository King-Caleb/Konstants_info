from KahootAPI import *
from tkinter import *

smallfont = ("Helvetica", 14)

# Create window
window = Tk()
window.config(bg="red")
window.title("Kahoot Data Base")

# Instruction Label
instruction_label = Label(window, text="Enter a Member's number", bg="red", fg="black", font=smallfont)
instruction_label.pack()

# Jersey Entry
jersey_entry = Entry(window)
jersey_entry.pack()

# Player Information Labels
namelbl = Label(window, text="Name", bg="red", fg="black", font=smallfont)
namelbl.pack()
name_value = Label(window, text="???", bg="red", fg="black", font=smallfont)
name_value.pack()

positionlbl = Label(window, text="Form", bg="red", fg="black", font=smallfont)
positionlbl.pack()
form_value = Label(window, text="???", bg="red", fg="black", font=smallfont)
form_value.pack()

citizenshiplbl = Label(window, text="Visits", bg="red", fg="black", font=smallfont)
citizenshiplbl.pack()
visits_value = Label(window, text="???", bg="red", fg="black", font=smallfont)
visits_value.pack()

appearanceslbl = Label(window, text="Points", bg="red", fg="black", font=smallfont)
appearanceslbl.pack()
points_value = Label(window, text="???", bg="red", fg="black", font=smallfont)
points_value.pack()


# Function to update player info
def showplayer():
    jersey_number = int(jersey_entry.get())
    playerdata = search(jersey_number)
    name_value.config(text=playerdata["name"], fg="blue")
    form_value.config(text=playerdata["form"], fg="blue")
    visits_value.config(text=playerdata["visits"], fg="blue")
    points_value.config(text=playerdata["points"], fg="blue")

# Function to reset labels
def reset():
    name_value.config(text='???', fg='black')
    form_value.config(text='???', fg='black')
    visits_value.config(text='???', fg='black')
    points_value.config(text='???', fg='black')


# Show player button
showplayerbutton = Button(window, text='Show Member', bg="blue", fg="white", font=smallfont, command=showplayer)
showplayerbutton.pack()

# Reset button
resetbtn = Button(window, text='Reset', bg="blue", fg="white", font=smallfont, command=reset)
resetbtn.pack()

# Main loop to run the application
window.mainloop()
