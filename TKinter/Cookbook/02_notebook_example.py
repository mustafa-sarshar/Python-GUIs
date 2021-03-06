# In[] Libs
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter.constants import W
from utils.custom_classes import createToolTip

# In[] Functions and Methods
def show_info():
    msg_1 = ""
    if var_gender.get() == "female": msg_1 = " Mrs."
    elif var_gender.get() == "male": msg_1 = " Mr."
    msg_2 = var_nationality.get()
    msg_3 = "but not a student"
    if var_student.get() == True: msg_3 = "and a student"
    msg = f"Dear{msg_1} {var_name.get()}\nYou are from {msg_2} {msg_3}!"
    messagebox.showinfo(title="Info!", message=msg)

def _exit():
    window.quit()
    window.destroy()
    exit()

def _about():
    messagebox.showinfo(title="About", message="This is a simple Python App\ncreated by Tkinter!")

# In[] Define the Layout and Widgets
window = tk.Tk()
window.wm_title("Python Notebook Example")
window.resizable(True, True)

menu_bar = tk.Menu(master=window)
# Sub-Menu - File
menu_file = tk.Menu(master=menu_bar, tearoff=False)
menu_file.add_command(label="New")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=_exit)
menu_bar.add_cascade(label="File", menu=menu_file)
# Sub-Menu - Help
menu_help = tk.Menu(master=menu_bar, tearoff=False)
menu_help.add_command(label="About", command=_about)
menu_bar.add_cascade(label="Help", menu=menu_help)

# Tab Controller
tab_controller = ttk.Notebook(master=window)
tab_controller.pack(fill=tk.BOTH, expand=True)
# Tabs
tab_contact_info = ttk.Frame(master=tab_controller)
tab_controller.add(child=tab_contact_info, text="Contact Info")
tab_bio = ttk.Frame(master=tab_controller)
tab_controller.add(child=tab_bio, text="Biography")
tab_controller.pack(fill=tk.BOTH, expand=True)
tab_family = ttk.Frame(master=tab_controller)
tab_controller.add(child=tab_family, text="Family")
tab_chess = ttk.Frame(master=tab_controller)
tab_controller.add(child=tab_chess, text="Chess")

# Tab - Contact Info
lblfrm_contact_info = ttk.LabelFrame(master=tab_contact_info, text="Fill in you contact details")
lblfrm_contact_info.grid(row=0, column=0, sticky="EWNS")

lbl_name = ttk.Label(master=lblfrm_contact_info, text="Enter a name:", foreground="black")
lbl_name.grid(row=0, column=0)
var_name = tk.StringVar(value="Your Name")
ent_name = ttk.Entry(master=lblfrm_contact_info, textvariable=var_name)
ent_name.grid(row=1, column=0)

lbl_gender = ttk.Label(master=lblfrm_contact_info, text="Gender:")
lbl_gender.grid(row=0, column=1)
var_gender = tk.StringVar()
cmb_gender = ttk.Combobox(master=lblfrm_contact_info, width=12, textvariable=var_gender, state="readonly")
cmb_gender["values"] = ["male", "female", "diverse"]
cmb_gender.current(0)
cmb_gender.grid(row=1, column=1)

var_student = tk.BooleanVar(value=False)
chk_student = ttk.Checkbutton(master=lblfrm_contact_info, text="student", variable=var_student, offvalue=False, onvalue=True)
chk_student.grid(row=1, column=2)

var_nationality = tk.StringVar(value="U.S")
rad_nationality = ttk.Radiobutton(master=lblfrm_contact_info, text="U.S", variable=var_nationality, value="U.S")
rad_nationality.grid(row=0, column=3, sticky="W")
rad_nationality = ttk.Radiobutton(master=lblfrm_contact_info, text="Non-U.S", variable=var_nationality, value="non-U.S")
rad_nationality.grid(row=1, column=3, sticky="W")

# Tab - Biography
srltxt_bio = scrolledtext.ScrolledText(master=tab_bio, width=45, height=5, wrap=tk.WORD)
srltxt_bio.grid(row=0, column=0, columnspan=4, sticky="WE")

btn_info = ttk.Button(master=window, text="Show Info", command=show_info)
btn_info.pack(side=tk.RIGHT)

# Tab - Family
lbl_family = ttk.Label(master=tab_family, text="Family-related Infos:")
lbl_family.grid(row=0, column=0, sticky="E")
lbl_children = ttk.Label(master=tab_family, text="No. of Children:")
lbl_children.grid(row=1, column=0, sticky="E")
var_children = tk.IntVar(value=0)
spn_children = tk.Spinbox(master=tab_family, from_=0, to=10, relief=tk.RIDGE, width=5, bd=5, textvariable=var_children) # relief property: tk.SUNKEN, tk.RAISED, tk.FLAT, tk.GROOVE, tk.RIDGE
spn_children.grid(row=1, column=1, sticky="W")

# Tab - Chess
frm_chess = tk.Frame(master=tab_chess, bg="black")
frm_chess.pack(fill=tk.Y, expand=False)
_colors = ["black", "orange"]
for _row in range(8):
    for _col in range(8):
        if _row%2: canvas = tk.Canvas(master=frm_chess, width=20, height=10, highlightthickness=0, bg=_colors[_col%2])
        else: canvas = tk.Canvas(master=frm_chess, width=20, height=10, highlightthickness=0, bg=_colors[int(not _col%2)])
        canvas.grid(row=_row, column=_col)

lblfrm_contact_info.grid_configure(padx=3, pady=3)
print(lblfrm_contact_info.winfo_children())
for widget in lblfrm_contact_info.winfo_children():
    widget.grid_configure(padx=3, pady=3)

# Add ToolTips to Widgets
createToolTip(widget=tab_contact_info, text="Personal information")
createToolTip(widget=tab_bio, text="Biography")
createToolTip(widget=tab_family, text="Family-related questions")
createToolTip(widget=tab_chess, text="Chess Style Background")
createToolTip(widget=btn_info, text="Click to see who you are")

window.configure(menu=menu_bar)
window.iconbitmap(r"style/pyc.ico")
window.mainloop()