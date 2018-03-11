from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Coffee Geeks Cafe")
window.geometry('600x600')

tab_control = ttk.Notebook(window)

mintleaf = "#00b894"
robinsegg = "#00cec9"
pure_apple = "#6ab04c"

style = ttk.Style()

style.theme_create( "tabtheme", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [45, 8], "background": mintleaf}, # the 45 and 8 represent the width and height of the tab's padding
        "map": {"background": [("selected", robinsegg)],
                "expand": [("selected", [2, 2, 1, 0])]}}})
style.theme_use("tabtheme")

# TAB 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Staff Manager")
tab_control.tab(tab1, padding=10) # this line keeps the labels and frames padded away from the widget's edge


# This is the code inside the frame of tab 1
label_frame = LabelFrame(tab1)
label_frame.grid(column=0, row=0, pady=10)

lbl1 = Label(label_frame, text='Staff', font=("Courier", 30), padx=10, pady=10) #padx,pady keep a border between the letters and containing element
lbl1.grid(column=0, row=0)



staff = ["Joe", "Vince", "Andria", "Brendan"]
managers = ["Kathryn", "Gabriela"]


def view_employees():
    staff_menu.grid_forget()
    lb_tasks.delete(0, END)
    for employee in staff:
        lb_tasks.insert(END, employee)


def view_managers():
    staff_menu.grid_forget()
    lb_tasks.delete(0, END)
    for employee in managers:
        lb_tasks.insert(END, employee)


def del_employee():

    employee = lb_tasks.curselection()
    lb_tasks.delete(employee)
    del staff[employee[0]]


def add_employee():
    employee = txt_input.get()
    if employee.strip() != '':
        lb_tasks.insert(END, employee)
        staff.append(employee)
        txt_input.delete(0,END)
    else:
        lb_tasks.insert(END, "\"blank\"")


def edit_input():
    # this is a helper function for deleting the hint text in the entry bar
    # and the color of the text changes from gray to black
    txt_input.delete(0, END)
    txt_input.config(fg='black')


def add_staff_member():

    global txt_input
    global staff_menu

    if staff_menu is None:
        staff_menu = staff_menu
    else:
        staff_menu.grid(column=2, row=0)

    txt_input = Entry(staff_menu, width=15, fg='gray')
    txt_input.insert(0, 'enter name here...')
    txt_input.bind('<FocusIn>', lambda x: edit_input())
    txt_input.grid(column=0, row=1)

    btn_add = Button(staff_menu, text="Add Employee", command=add_employee)
    btn_add.grid(column=0, row=2)

    del_btn = Button(staff_menu, text="Delete Employee", command=del_employee)
    del_btn.grid(column=0, row=3)



# lb_tasks = Listbox(tab1)
# lb_tasks.grid(column=2, row=4)


style.configure('TButton', background=pure_apple, padding=6, relief=RAISED)
view_employees = ttk.Button(tab1, text="View Employees", command=view_employees)
view_employees.grid(column=0, row=1)

view_managers = ttk.Button(tab1, text="View Managers", command=view_managers)
view_managers.grid(column=0, row=2)

add_staff = ttk.Button(tab1, text="Edit Staff Menu", command=add_staff_member)
add_staff.grid(column=0, row=3)

side_frame = LabelFrame(tab1)
global txt_input
global staff_menu
staff_menu = Frame(tab1)
side_frame.grid(column=2, columnspan=2, rowspan=5, row=1, padx=20, pady=20)
lb_tasks = Listbox(side_frame)
lb_tasks.grid(column=0, row=4)

footer_frame = LabelFrame(tab1)
footer_frame.grid(column=1, columnspan=2, row=9, pady=20)
made_by_label = Label(footer_frame, text="Coded with ❤️ by the fine folks @ ¯\_(ツ)_/¯", pady=10)
made_by_label.grid(column=0, row=0)





""" 
    TO DO TASKS
    - see a list of all employees and IDS
    - view and print an employee's schedule
    - view and print an employees details
    - view a csv file of employee's details ( id #, date of hire, name, etc)
    - delete employee ( move to archived area )
    - add a new employee

"""



# TAB 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Inventory Manager")

lbl2 = Label(tab2, text='Inventory', font=("Courier", 30), padx=10, pady=10)
lbl2.grid(column=0, row=0)
tab_control.tab(tab2, padding=10)


tab_control.pack(expand=1, fill='both')
window.mainloop()


"""
add_item()
drop down menu for the various goods
list amounts of each

"""

## color wheel
## visit this website for more nice 'flat' color options
## https://flatuicolors.com/
#/Users/brendantyleralbert/PycharmProjects/python2/SANDBOXthinkgeektkinter.py



# def get_employees():
#
#     tempstring = ""
#     staff_frame = ttk.Labelframe(tab1)
#     for emp in staff:
#         tempstring += emp + '\n'
#     temp_label = ttk.Label(staff_frame, text=tempstring)
#     temp_label.grid(column=1, row=0)
#     staff_frame.grid(column=1, row=0)

# def get_managers():
#
#     tempstring = ""
#     staff_frame = ttk.Labelframe(tab1)
#     var = StringVar()
#     for emp in managers:
#         tempstring += emp + '\n'
#     temp_label = ttk.Label(staff_frame, text=tempstring)
#     temp_label.grid(column=1, row=0)
#     staff_frame.grid(column=1, row=0)


