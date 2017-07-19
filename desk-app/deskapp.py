"""
A program that stores the following information about user's current semester
Course name, Internal I, II and III scores along with user's total scores for each course

User can:
1)View all marks
2)Search for entry: The user can search for the course by entering the course name
                  or the user can also search details of courses having a certain value of credits
3)Add an entry
4)Delete the entry
5)Update the entry
6)Close
"""

from tkinter import *
import db                #py file containing all the necessary back end functions

def get_selected_course(event):
    global selected
    index = listbox.curselection()[0]
    selected = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected[1])
    e3.delete(0, END)
    e3.insert(END, selected[3])
    e4.delete(0, END)
    e4.insert(END, selected[4])

def clear_button():
    e1.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    position_val.set("Null")
    permit_val.set("Null")
    dept_val.set("Null")

#defining the functions that links backend function to front end gui for buttons

def view_cmd():
    listbox.delete(0, END)
    for row in db.view():
        listbox.insert(END, row)

def search_cmd():
    listbox.delete(0, END)
    for row in db.search(permit_val.get(), name_val.get().lower()):
        listbox.insert(END, row)

def add_cmd():
    db.insert(name_val.get().lower(), position_val.get(), user_val.get(), pass_val.get(), dept_val.get(), permit_val.get())
    view_cmd()

def del_cmd():
    db.delete(selected[0])
    view_cmd()

def update_cmd():
    db.update(selected[0], name_val.get(), position_val.get(), user_val.get(), pass_val.get(), dept_val.get(), permit_val.get())
    view_cmd()


window = Tk()

window.wm_title("Faculty Database for E-Portal App")

for i in range(8):
    Grid.rowconfigure(window, i, weight=1)
    Grid.columnconfigure(window, i, weight=1)


#you must do the above for every single widget in that row and column
                    #and also add sticky = N+S+E+W in the grid method

#adding labels and entry forms to the UI
l1 = Label(window, text = "Faculty Name:")
l1.grid(row = 0, column = 0, sticky = N+S+E+W)

name_val = StringVar()
e1 = Entry(window, textvariable = name_val)
e1.grid(row = 0, column = 1, sticky = N+S+E+W)

l2 = Label(window, text = "Position:")
l2.grid(row = 0, column = 3, sticky = N+S+E+W)

choices = {"Null", "Assistant Professor", "Associate Professor"}
position_val = StringVar()
e2 = OptionMenu(window, position_val, *choices)
e2.grid(row = 0, column = 4, sticky = N+S+E+W)

l3 = Label(window, text = "User ID:")
l3.grid(row = 1, column = 0, sticky = N+S+E+W)

user_val = StringVar()
e3 = Entry(window, textvariable = user_val)
e3.grid(row = 1, column = 1, sticky = N+S+E+W)

l4 = Label(window, text = "Password:")
l4.grid(row = 1, column = 3, sticky = N+S+E+W)

pass_val = StringVar()
e4 = Entry(window, textvariable = pass_val)
e4.grid(row = 1, column = 4, sticky = N+S+E+W)

l5 = Label(window, text = "Department:")
l5.grid(row = 2, column = 0, sticky = N+S+E+W)

choices2 = {"Null", "CSE", "Other"}
dept_val = StringVar()
e5 = OptionMenu(window, dept_val, *choices2)
e5.grid(row = 2, column = 1, sticky = N+S+E+W)

l6 = Label(window, text = "Permission:")
l6.grid(row = 2, column = 3, sticky = N+S+E+W)

choices3 = {"Null", "YES", "NO"}
permit_val = StringVar()
e6 = OptionMenu(window, permit_val, *choices3)
e6.grid(row = 2, column = 4, sticky = N+S+E+W)

listbox = Listbox(window, height = 8, width = 35)
listbox.grid(row = 3, column = 0, rowspan = 7, columnspan = 2, padx = (30,0), sticky = N+S+E+W)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row = 3, column = 3, rowspan = 6)

#now to link the scrollbar with the listbox

listbox.configure(yscrollcommand = scrollbar1.set)
scrollbar1.configure(command = listbox.yview)

#using bind method to select a course/entry from the listbox (database)

listbox.bind('<<ListboxSelect>>', get_selected_course)

#now adding buttons to the UI
clear = Button(window, text = "Reset", width = 12, command = clear_button)
clear.grid(row = 3, column = 4, padx = (0, 10), sticky = N+S+E+W)

view = Button(window, text = "View All", width = 12, command = view_cmd)
view.grid(row = 4, column = 4, padx = (0, 10), sticky = N+S+E+W)

search = Button(window, text = "Search for Faculty", width = 12, command = search_cmd)
search.grid(row = 5, column = 4, padx = (0, 10), sticky = N+S+E+W)

add = Button(window, text = "Add Faculty", width = 12, command = add_cmd)
add.grid(row = 6, column = 4, padx = (0, 10), sticky = N+S+E+W)

delete = Button(window, text = "Delete Selected", width = 12, command = del_cmd)
delete.grid(row = 8, column = 4, padx = (0, 10), sticky = N+S+E+W)

update = Button(window, text = "Update Selected", width = 12, command = update_cmd)
update.grid(row = 7, column = 4, padx = (0, 10), sticky = N+S+E+W)

exit = Button(window, text = "Exit", width = 12, command = window.destroy)
exit.grid(row = 9, column = 4, padx = (0, 10), sticky = N+S+E+W)

view_cmd()

window.mainloop()
