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
    """
    This function is called when the user clicks the View Employees button.
    The staff menu is removed from the grid using .grid_forget().
    All of the names in the Listbox are removed using .delete().
    A for loop is used to insert all of the employee staff into the Listbox.
    The bind function is called on the Listbox.  We give it two parameters, the first argument listens for double clicks
        on any element in the Listbox, the second argument calls the on_emp_dbl(e) method.  This is short for
        on employee double click, and we pass it the employee who was clicked on.  This will open a pop-up window
        with that employee's information.

    The last four lines are used to display a label which identifies for the user which type of staff he or
        she is looking at in the listbox.
    """
    staff_menu.grid_forget()
    lb_tasks.delete(0, END)
    for employee in staff:
        lb_tasks.insert(END, employee)
    lb_tasks.bind('<Double-1>', lambda e: on_emp_dbl(e))

    type = StringVar()
    staff_type = Label(tab1, textvariable=type)
    type.set('Employees:')
    staff_type.grid(column=2, row=7, sticky='ew')


def view_managers():
    """
        This function is called when the user clicks the View Managers button.
        The staff menu is removed from the grid using .grid_forget().
        All of the names in the listbox are removed using .delete().
        A for loop is used to insert all of the manager staff into the listbox.
        The bind function is called on the listbox.  We give it two parameters, the first argument listens for double clicks
            on any element in the listbox, the second argument calls the on_mgr_dbl(e) method.  This is short for
            on manager double click, and we pass it the manager who was clicked on.  This will open a pop-up window
            with that managers information.

        The last four lines are used to display a label which identifies for the user which type of staff he or
            she is looking at in the listbox.
    """
    staff_menu.grid_forget()
    lb_tasks.delete(0, END)
    for employee in managers:
        lb_tasks.insert(END, employee)
    lb_tasks.bind('<Double-1>', lambda e: on_mgr_dbl(e))

    type = StringVar()
    staff_type = Label(tab1, textvariable=type)
    type.set('Managers:')
    staff_type.grid(column=2, row=7, sticky='ew')


def del_employee():
    """
    This function is called when the user clicks the delete employee button.
    It works by deleting the selected employee from the listbox.
    """
    employee = lb_tasks.curselection()
    lb_tasks.delete(employee)
    del staff[employee[0]]


def add_employee():
    """
    This function is called when the user adds a new employees name to the txt_input Entry widget.
    If the entry is not blank then the provided name is added as an employee.
    """
    employee = txt_input.get()
    if employee.strip() != '' and employee.strip() != 'enter name here...':
        lb_tasks.insert(END, employee)
        staff.append(employee)
        txt_input.delete(0, END)


def del_manager():
    """
    del_manager() is the function which is called when the user selects a manager to delete and clicks the
    delete manager button.
    .curselection() returns a tuple with the first element in the tuple being an integer representing the location
    in the listbox of the selected manager.
    The chosen manager is deleted from the listbox and then deleted from the manager list.
    """
    mgr = lb_tasks.curselection()
    lb_tasks.delete(mgr)
    del managers[mgr[0]]


def add_manager():
    """
    The add_manager() function is called when the user enters a name into the Entry widget and presses the add
    manager button.  If the Entry widget is blank or left untouched, nothing happens.
    """
    mgr = txt_input.get()
    if mgr.strip() != '' and mgr.strip() != 'enter name here...':
        lb_tasks.insert(END, mgr)
        managers.append(mgr)
        txt_input.delete(0, END)


def edit_input():
    """
    # this is a helper function for deleting the hint text in the entry bar
    # and the color of the text changes from gray to black
    """
    txt_input.delete(0, END)
    txt_input.config(fg='black')


def staff_edit_menu():
    """
    The staff_edit_menu() function is called when the user clicks the edit staff menu button.
    A frame appears with two radio buttons and an entry widget.  If the manager radiobutton
    is selected then the user can add or remove a manager using the respective buttons.
    The user must click to select the employee/manager she wishes to delete.
    A name must be provided in the entry widget to add an employee/manager.

    """
    global txt_input
    global staff_menu

    if staff_menu is None:
        staff_menu = staff_menu
    else:
        staff_menu.grid(column=2, row=1)

    txt_input = Entry(staff_menu, width=15, fg='gray')
    txt_input.insert(0, 'enter name here...')
    txt_input.bind('<FocusIn>', lambda x: edit_input())
    txt_input.grid(column=0, row=2)

    btn_choice = StringVar()
    emp_btn = Radiobutton(staff_menu, text='Employee', variable=btn_choice, value=0, command=use_employee_btns)
    emp_btn.grid(column=0, row=0, sticky='w')
    mgr_btn = Radiobutton(staff_menu, text='Manager', variable=btn_choice, value=1, command=use_mgr_btns)
    mgr_btn.grid(column=0, row=1, sticky='w')


def use_mgr_btns():
    """
    The use_mgr_btns() function is called when the Manager radio button is selected.
    This allows the appropriate add/delete manager buttons to appear.
    """
    lb_tasks.delete(0, END)
    for employee in managers:
        lb_tasks.insert(END, employee)
    btn_add = Button(staff_menu, text="Add Manager", command=add_manager)
    btn_add.grid(column=0, row=3, sticky='ew')
    del_btn = Button(staff_menu, text="Delete Manager", command=del_manager)
    del_btn.grid(column=0, row=4, sticky='ew')
    lb_tasks.bind('<Double-1>', lambda e: on_mgr_dbl(e))

    type = StringVar()
    staff_type = Label(tab1, textvariable=type)
    type.set('Managers:')
    staff_type.grid(column=2, row=7, sticky='ew')


def use_employee_btns():
    """
        The use_employee_btns() function is called when the Employee radio button is selected.
        This allows the appropriate add/delete employee buttons to appear.
        """
    lb_tasks.delete(0, END)
    for employee in staff:
        lb_tasks.insert(END, employee)
    btn_add = Button(staff_menu, text="Add Employee", command=add_employee)
    btn_add.grid(column=0, row=3, sticky='ew')
    del_btn = Button(staff_menu, text="Delete Employee", command=del_employee)
    del_btn.grid(column=0, row=4, sticky='ew')
    lb_tasks.bind('<Double-1>', lambda e: on_emp_dbl(e))

    type = StringVar()
    staff_type = Label(tab1, textvariable=type)
    type.set('Employees:')
    staff_type.grid(column=2, row=7, sticky='ew')


""" These are the three buttons on the left side of the Staff Manager frame."""

style.configure('TButton', background=pure_apple, padding=6, relief=RAISED)
view_employees = ttk.Button(tab1, text="View Employees", command=view_employees)
view_employees.grid(column=0, row=1)

view_managers = ttk.Button(tab1, text="View Managers", command=view_managers)
view_managers.grid(column=0, row=2)

add_staff = ttk.Button(tab1, text="Edit Staff Menu", command=staff_edit_menu)
add_staff.grid(column=0, row=3)


global txt_input
global staff_menu

staff_menu = Frame(tab1)
side_frame = LabelFrame(tab1)
side_frame.grid(column=2, columnspan=2, rowspan=5, row=2, padx=20, pady=20)

type = StringVar()
staff_type = Label(tab1, textvariable=type)

lb_tasks = Listbox(side_frame)
lb_tasks.grid(column=0, row=6, sticky='w')


def on_emp_dbl(e):
    widget = e.widget
    selection = widget.curselection()
    tl = Toplevel()
    text = Text(tl)
    text.insert(INSERT, staff[selection[0]])
    text.pack()


def on_mgr_dbl(e):
    widget = e.widget
    selection = widget.curselection()
    tl = Toplevel()
    text = Text(tl)
    text.insert(INSERT, managers[selection[0]])
    text.pack()


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

