from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Coffee Geeks Cafe")
window.geometry('600x600')


"""
lbl = Label(window, text="hello")
lbl.grid(column=0,row=0)


def clicked():
    lbl.configure(text="Button was clicked!")


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
"""

tab_control = ttk.Notebook(window)

## color wheel
## visit this website for more nice 'flat' color options
## https://flatuicolors.com/

mintleaf = "#00b894"
robinsegg = "#00cec9"

style = ttk.Style()

style.theme_create( "tabtheme", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [45, 8], "background": mintleaf}, # the 45 and 8 represent the width and height of the tab's padding
        "map": {"background": [("selected", robinsegg)],
                "expand": [("selected", [2, 2, 1, 0])]}}})
style.theme_use("tabtheme")

# TAB 1
tab1 = ttk.Frame(tab_control, width=100, height=100)
tab_control.add(tab1, text="Staff Manager")


lbl1 = Label(tab1, text='Staff', font=("Courier", 20), padx=10, pady=10)
lbl1.grid(column=0, row=0)
tab_control.tab(tab1, padding=10)

staff_frame = ttk.Labelframe(tab1, text="")
staff_frame.grid()
var = StringVar()
txt = Message(staff_frame, textvariable=var, width=175)

employees = ["Joe", "Vince", "Andria", "Brendan"]
empstring = ""
for emp in employees:
    empstring += emp + '\n'

var.set(empstring)
txt.grid(column=0, row=4)


# TAB 2
tab2 = ttk.Frame(tab_control, width=100, height=100)
tab_control.add(tab2, text="Inventory Manager")
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=0, row=0)
tab_control.tab(tab2, padding=10)


tab_control.pack(expand=1, fill='both')
window.mainloop()
