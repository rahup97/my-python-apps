"""
A program that stores the following information about user's current semester
Course name, Internal I, II and III scores along with user's total scores for each course

User can:
View all marks
Search for entry: The user can search for the course by entering the course name
                  or the user can also search details of courses having a certain value of credits
Add entry
Delete entry
Update entry
Close
"""

from tkinter import *
from bkendOOP import Database                #py file containing all the necessary back end functions

database = Database()

def get_selected_course(event):
    global selected
    index = listbox.curselection()[0]
    selected = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected[1])
    e2.delete(0, END)
    e2.insert(END, selected[2])
    e3.delete(0, END)
    e3.insert(END, selected[3])
    e4.delete(0, END)
    e4.insert(END, selected[4])
    e5.delete(0, END)
    e5.insert(END, selected[5])
    e6.delete(0, END)
    e6.insert(END, selected[6])


#defining the functions that links backend function to front end gui for buttons

def view_cmd():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)

def search_cmd():
    listbox.delete(0, END)
    for row in database.search(course_val.get(), credit_val.get()):
        listbox.insert(END, row)

def add_cmd():
    database.insert(course_val.get(), credit_val.get(),int1_val.get(), int2_val.get(), int3_val.get(), labself_val.get())
    view_cmd()

def del_cmd():
    database.delete(selected[0])
    view_cmd()

def update_cmd():
    database.update(selected[0], course_val.get(), credit_val.get(), int1_val.get(), int2_val.get(), int3_val.get(), labself_val.get())
    view_cmd()


window = Tk()

window.wm_title("My Marks")

for i in range(8):
    Grid.rowconfigure(window, i, weight=1)
    Grid.columnconfigure(window, i, weight=1)


#you must do the above for every single widget in that row and column
                    #and also add sticky = N+S+E+W in the grid method

#adding labels and entry forms to the UI
l1 = Label(window, text = "Course name:")
l1.grid(row = 0, column = 0, sticky = N+S+E+W)

course_val = StringVar()
e1 = Entry(window, textvariable = course_val)
e1.grid(row = 0, column = 1, sticky = N+S+E+W)

l2 = Label(window, text = "Credits:")
l2.grid(row = 0, column = 3, sticky = N+S+E+W)

credit_val = StringVar()
e2 = Entry(window, textvariable = credit_val)
e2.grid(row = 0, column = 4, sticky = N+S+E+W)

l3 = Label(window, text = "Internal I:")
l3.grid(row = 1, column = 0, sticky = N+S+E+W)

int1_val = StringVar()
e3 = Entry(window, textvariable = int1_val)
e3.grid(row = 1, column = 1, sticky = N+S+E+W)

l4 = Label(window, text = "Internal II:")
l4.grid(row = 1, column = 3, sticky = N+S+E+W)

int2_val = StringVar()
e4 = Entry(window, textvariable = int2_val)
e4.grid(row = 1, column = 4, sticky = N+S+E+W)

l5 = Label(window, text = "Internal III:")
l5.grid(row = 2, column = 0, sticky = N+S+E+W)

int3_val = StringVar()
e5 = Entry(window, textvariable = int3_val)
e5.grid(row = 2, column = 1, sticky = N+S+E+W)

l5 = Label(window, text = "Lab + SelfStudy:")
l5.grid(row = 2, column = 3, sticky = N+S+E+W)

labself_val = StringVar()
e6 = Entry(window, textvariable = labself_val)
e6.grid(row = 2, column = 4, sticky = N+S+E+W)

listbox = Listbox(window, height = 8, width = 35)
listbox.grid(row = 3, column = 0, rowspan = 6, columnspan = 2, padx = (30,0), sticky = N+S+E+W)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row = 3, column = 3, rowspan = 6)

#now to link the scrollbar with the listbox

listbox.configure(yscrollcommand = scrollbar1.set)
scrollbar1.configure(command = listbox.yview)

#using bind method to select a course/entry from the listbox (database)

listbox.bind('<<ListboxSelect>>', get_selected_course)

#now adding buttons to the UI

view = Button(window, text = "View All Courses", width = 12, command = view_cmd)
view.grid(row = 6, column = 4, padx = (0, 10), sticky = N+S+E+W)

search = Button(window, text = "Search for Course", width = 12, command = search_cmd)
search.grid(row = 5, column = 4, padx = (0, 10), sticky = N+S+E+W)

add = Button(window, text = "Add Course", width = 12, command = add_cmd)
add.grid(row = 3, column = 4, padx = (0, 10), sticky = N+S+E+W)

delete = Button(window, text = "Delete Selected", width = 12, command = del_cmd)
delete.grid(row = 7, column = 4, padx = (0, 10), sticky = N+S+E+W)

update = Button(window, text = "Update Selected", width = 12, command = update_cmd)
update.grid(row = 4, column = 4, padx = (0, 10), sticky = N+S+E+W)

exit = Button(window, text = "Exit", width = 12, command = window.destroy)
exit.grid(row = 8, column = 4, padx = (0, 10), sticky = N+S+E+W)

view_cmd()

window.mainloop()
