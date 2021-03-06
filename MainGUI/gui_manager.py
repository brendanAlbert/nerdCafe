#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk, messagebox
from Staff.Staff import Staff
from Inventory.Manager.inventory_manager import InventoryManager
from Inventory.Coffee.coffee_sales import *
import pathlib

window = Tk()
window.title("Coffee Geeks Cafe")
window.geometry('800x625')

tab_control = ttk.Notebook(window)

global txt_input
global staff_menu

mintleaf = "#00b894"
robinsegg = "#00cec9"
pure_apple = "#6ab04c"

style = ttk.Style()

style.theme_create("tabtheme", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [45, 8], "background": mintleaf},
    # the 45 and 8 represent the width and height of the tab's padding
        "map": {"background": [("selected", robinsegg)],
                "expand": [("selected", [2, 2, 1, 0])]}}})
style.theme_use("tabtheme")

# TAB 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Staff Manager")
tab_control.tab(tab1, padding=10)  # this line keeps the labels and frames padded away from the widget's edge

# This is the code inside the frame of tab 1
label_frame = LabelFrame(tab1)
label_frame.grid(column=0, row=0, pady=10)

lbl1 = Label(label_frame, text='Staff', font=("Courier", 30), padx=10,
             pady=10)  # padx,pady keep a border between the letters and containing element
lbl1.grid(column=0, row=0)


##### The two staff/manager lists which are populated from the csv and hold
#### staff in memory while the program is running
staff = []
managers = []


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

    display_staff_type_label('employee')


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

        The display_staff_type_label is used to display a label which identifies for the user which type of staff he or
            she is looking at in the listbox.
    """
    staff_menu.grid_forget()
    lb_tasks.delete(0, END)
    for employee in managers:
        lb_tasks.insert(END, employee)
    lb_tasks.bind('<Double-1>', lambda e: on_mgr_dbl(e))

    display_staff_type_label('manager')


def del_employee():
    """
    This function is called when the user clicks the delete employee button.
    delete_confirm_modal() is called which pops up a window asking if the user is sure she wants to delete
    the selected employee.
    It works by deleting the selected employee from the listbox.
    """
    employee = lb_tasks.curselection()
    try:
        if del_confirm_modal(staff[employee[0]]):
            lb_tasks.delete(employee)
            del staff[employee[0]]
    except IndexError:
        print('tried to delete without a staff member selected')

def add_employee():
    """
    This function is called when the user adds a new employees name to the txt_input Entry widget.
    If the entry is not blank then the provided name is added as an employee.
    """
    employee = txt_input.get()
    if employee.strip() != '' and employee.strip() != 'enter name here...':
        new_empl = Staff(employee, 20.0)
        lb_tasks.insert(END, new_empl)
        staff.append(new_empl)
        txt_input.delete(0, END)


def del_confirm_modal(member):
    """
    :param member: the staff member to delete
    :return: True if the user clicks OK, False if he/she clicks cancel
    """
    delete_msg = f"Are you sure you want to delete:\n\n{member}?"
    return messagebox.askokcancel("Deleting Staff Member", delete_msg, icon='warning')


def del_manager():
    """
    del_manager() is the function which is called when the user selects a manager to delete and clicks the
    delete manager button.
    delete_confirm_modal() is called which pops up a window asking if the user is sure she wants to delete
    the selected manager.
    .curselection() returns a tuple with the first element in the tuple being an integer representing the location
    in the listbox of the selected manager.
    The chosen manager is deleted from the listbox and then deleted from the manager list.
    """
    mgr = lb_tasks.curselection()
    try:
        if del_confirm_modal(managers[mgr[0]]):
            lb_tasks.delete(mgr)
            del managers[mgr[0]]
    except IndexError:
        print('tried to delete without a staff member selected')


def add_manager():
    """
    The add_manager() function is called when the user enters a name into the Entry widget and presses the add
    manager button.  If the Entry widget is blank or left untouched, nothing happens.
    """
    mgr = txt_input.get()
    if mgr.strip() != '' and mgr.strip() != 'enter name here...':
        new_mgr = Staff(mgr, 40.0)
        lb_tasks.insert(END, new_mgr)
        managers.append(new_mgr)
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
        staff_menu.grid(column=3, row=3)

    txt_input = Entry(staff_menu, width=15, fg='gray')
    txt_input.insert(0, 'enter name here...')
    txt_input.bind('<FocusIn>', lambda x: edit_input())
    txt_input.grid(column=0, row=2)

    btn_choice = StringVar()
    emp_btn = Radiobutton(staff_menu, text='Employee', variable=btn_choice, value=0, command=use_employee_btns)
    emp_btn.grid(column=0, row=0, sticky='w')
    mgr_btn = Radiobutton(staff_menu, text='Manager', variable=btn_choice, value=1, command=use_mgr_btns)
    mgr_btn.grid(column=0, row=1, sticky='w')


def retrieve_staff_from_csv():
    """
    Retrieve the persisted employees and managers from the staff_list.csv file.
    Fill the respective lists with the staff.
    """
    with open("Staff/staff_list.csv", newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        print(reader)
        for staffer in reader:
            emp = Staff(staffer[1], staffer[2], staffer[0])
            managers.append(emp) if staffer[3] == 'yes' else staff.append(emp)

def load_staff():
    """ Load any persisted staff on app launch """
    try:
        retrieve_staff_from_csv()
    except FileNotFoundError:
        print("file not found")


def save_staff_to_csv():
    """
    save_staff_to_csv is called whenever the user taps the Save Staff to CSV button.
    A modal pops up to inform the user the save was successful.
    """

    headers = ["StaffID", "Name", "Wagerate", "IsManager"]

    with open("Staff/staff_list.csv", "w", newline='') as f:
        # create a writer object
        writer = csv.writer(f)
        # pass it the header and iterate through the records
        writer.writerow(headers)
        for staffer in staff:
            writer.writerow([staffer._id, staffer._name, 20.0, 'no'])
        for mgr in managers:
            writer.writerow([mgr._id, mgr._name, 40.0, 'yes'])

        messagebox.showinfo('Save Successful!', 'Staff Successfully Saved to CSV!')


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

    display_staff_type_label('manager')


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

    display_staff_type_label('employee')


""" These are the four buttons on the left side of the Staff Manager frame."""

style.configure('TButton', background=pure_apple, padding=6, relief=RAISED)
view_employees = ttk.Button(tab1, text="View Employees", command=view_employees)
view_employees.grid(column=0, row=1)

view_managers = ttk.Button(tab1, text="View Managers", command=view_managers)
view_managers.grid(column=0, row=2)

add_staff = ttk.Button(tab1, text="Edit Staff Menu", command=staff_edit_menu)
add_staff.grid(column=0, row=3)

save_staff = ttk.Button(tab1, text="Save Staff to CSV", command=save_staff_to_csv)
save_staff.grid(column=0, row=4)

#### STAFF MENU #####

staff_menu = Frame(tab1)
side_frame = LabelFrame(tab1)
side_frame.grid(column=2, columnspan=1, rowspan=5, row=3, padx=0, pady=0)


####  END STAFF MENU  ####


### "Type of staff" label ###

def display_staff_type_label(employee_or_manager):
    """
    :param employee_or_manager: A staff member is passed in who is either an employee or manager.
    The label above the listbox is updated to reflect which type of staff are being displayed.
    """
    staff_label_text = StringVar()
    staff_label = Label(tab1, textvariable=staff_label_text)
    staff_label_text.set('Employees:') if employee_or_manager == 'employee' else staff_label_text.set('Managers:')
    staff_label.grid(column=2, row=2, sticky='ew')


##### End type of staff label ###

### Listbox ####

lb_tasks = Listbox(side_frame)
lb_tasks.grid(column=0, row=6, sticky='w')


### END Listbox ####


def on_emp_dbl(e):
    """
        :param e: e represents the employee from the listbox that is double clicked on.
        A new Toplevel window pops up, filled with that employee's details.
    """
    widget = e.widget
    selection = widget.curselection()
    tl = Toplevel()
    text = Text(tl)
    text.insert(INSERT, staff[selection[0]])
    text.pack()


def on_mgr_dbl(e):
    """
    :param e: e represents the manager from the listbox that is double clicked on.
    A new Toplevel window pops up, filled with that manager's details.
    """
    widget = e.widget
    selection = widget.curselection()
    tl = Toplevel()
    text = Text(tl)
    text.insert(INSERT, managers[selection[0]])
    text.pack()


def display_footer(tab):
    """
    :param tab: passes either tab1, tab2 or tab3 depending on which tab the used clicked.
    The function displays a little Label at the bottom of the frame.
    """
    footer_frame = LabelFrame(tab)
    footer_frame.grid(column=1, columnspan=2, ipadx=20, row=9, pady=20, sticky='ew')
    made_by_label = Label(footer_frame, text="Coded with ❤️ by the fine folks @ ¯\_(ツ)_/¯", pady=10)
    made_by_label.grid(column=0, row=0, sticky='ew')


display_footer(tab1)

#### End of TAB 1, Staff Manager ######



#### Start of TAB 2, Inventory Manager ######

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Inventory Manager")

lbl2 = Label(tab2, text='Inventory', font=("Courier", 30), padx=10, pady=10)
lbl2.grid(column=0, row=0, sticky='w')
tab_control.tab(tab2, padding=10)
tab_control.pack(expand=1, fill='both')


## Inventory Manager Object
inventory_mgr = InventoryManager()
inventory_mgr.upload_produce_csv("Inventory/Ingredients/produce.csv")
inventory_mgr.upload_liquid_csv("Inventory/Ingredients/liquids.csv")
inventory_mgr.upload_drygood_csv("Inventory/Ingredients/drygoods.csv")
inventory_mgr.upload_meat_csv("Inventory/Ingredients/meats.csv")


#### Tab 2 Functions ###


def view_produce():
    """
    view_produce is called when the user clicks the view produce button.
    The listbox is emptied of any previous contents, and all of the
    produce from the inventory manager object
    is inserted.
    """
    inventory_listbox.delete(0, END)
    for fruit_veg in inventory_mgr._produce:
        inventory_listbox.insert(END, fruit_veg)


def view_liquids():
    """
        view_liquids is called when the user clicks the view liquids button.
        The listbox is emptied of any previous contents, and all of the
        liquids from the inventory manager object
        are inserted.
     """
    inventory_listbox.delete(0, END)
    for liquid in inventory_mgr._liquids:
        inventory_listbox.insert(END, liquid)


def view_drygoods():
    """
        view_drygoods is called when the user clicks the View Dry Goods button.
        The listbox is emptied of any previous contents, and all of the
        dry goods from the inventory manager object
        are inserted.
    """
    inventory_listbox.delete(0, END)
    for drygood in inventory_mgr._drygoods:
        inventory_listbox.insert(END, drygood)


def view_meats():
    """
        view_meats is called when the user clicks the view meats button.
        The listbox is emptied of any previous contents, and all of the
        meats from the inventory manager object
        are inserted.
    """
    inventory_listbox.delete(0, END)
    for meat in inventory_mgr._meat:
        inventory_listbox.insert(END, meat)


def open_file_with_excel():
    """
    opens the provided file using the excel-type program of the calling operating system
    """
    inventory_mgr.open_excel("Inventory/Ingredients/produce.csv")


## SETUP Listbox ###
inventory_listbox = Listbox(tab2, height=20, width=60)
inventory_listbox.grid(column=0, columnspan=10, row=2, sticky='news', pady=20)


### Setup Inventory Manager Buttons

produce_btn = ttk.Button(tab2, text="View Produce", command=view_produce)
produce_btn.grid(column=0, row=1, sticky='w', pady=10)

open_excel_btn = ttk.Button(tab2, text="View Produce in Excel", command=open_file_with_excel)
open_excel_btn.grid(column=1, row=1, sticky='w', pady=10)

liquids_btn = ttk.Button(tab2, text="View Liquids", command=view_liquids)
liquids_btn.grid(column=2, row=1, sticky='w', pady=10)

drygoods_btn = ttk.Button(tab2, text="View Dry Goods", command=view_drygoods)
drygoods_btn.grid(column=3, row=1, sticky='w', pady=10)

meats_btn = ttk.Button(tab2, text="View Meats", command=view_meats)
meats_btn.grid(column=4, row=1, sticky='w', pady=10)


display_footer(tab2)

##### End of TAB 2, Inventory Manager Tab ########


### Start of TAB 3, Coffee Tab ###

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Coffee Manager")

lbl3 = Label(tab3, text='Coffee', font=("Courier", 30), padx=10, pady=10)
lbl3.grid(column=0, row=0, sticky='w')
tab_control.tab(tab3, padding=10)
tab_control.pack(expand=1, fill='both')


### TAB 3 Functions ###


def generate_sales_report():
    """
    generate_sales_report is called when the user clicks on the
    Generate Coffee Sold Report button in the third tab.
    The appropriate csv file is read and a report generated.
    The items are inserted into the listbox in the gui for display.
    The amount of sales are computed and displayed similarly.
    """
    filename = pathlib.Path('Inventory/Coffee/coffee_sales.csv')
    report = generate_inventory_report(filename)
    sold = compute_sales(filename)

    coffee_mgr_listbox.delete(0, END)

    coffee_mgr_listbox.insert(END, "Beverage, #sold")
    coffee_mgr_listbox.insert(END, "")

    for coffee, value in report.items():
        row = f"{coffee}, {value}"
        #row = "{:33s}{}".format(coffee, value) I DONT KNOW WHY THIS WON'T FORMAT GAAHHH
        coffee_mgr_listbox.insert(END, row)

    coffee_mgr_listbox.insert(END, "")
    coffee_mgr_listbox.insert(END, "Number drinks sold: {}".format(sold))
    coffee_mgr_listbox.insert(END, "Total Sales ${:.2f}".format(sold))


## SETUP Listbox ###

coffee_mgr_listbox = Listbox(tab3, height=20, width=50)
coffee_mgr_listbox.grid(column=0, columnspan=10, row=2, sticky='news', pady=20)

### Setup Coffee Manager Buttons

sales_report_btn = ttk.Button(tab3, text="Generate Coffee Sold Report", command=generate_sales_report)
sales_report_btn.grid(column=0, row=1, sticky='w', pady=10)

display_footer(tab3)

### End of TAB 3, Coffee Tab ###



##### RUN APP
load_staff()
window.mainloop()
