from tkinter import Tk, ttk, TOP, LEFT, mainloop, Label, LabelFrame, Button, Grid, Pack, filedialog, messagebox, Entry
from functions import ves_to_srm, srm_to_ves, os

root = Tk()
root.title('3DS SNES Save Converter')
root.resizable(False, False)

ves = None
srm = None

#
# GUI FUNCTIONS
#
def select_ves():
    global ves
    inputf = filedialog.askopenfilename(initialdir = "/",title = "Select .VES file", filetypes = ((".VES File","*.ves"),("All files","*.*")))
    base = os.path.basename(inputf)
    if os.path.splitext(base)[1] == '.ves':
        ves = inputf
    else:
        messagebox.showerror("Error: File not valid", "You must select a .VES File")
    pass

def select_srm():
    global srm
    inputf = filedialog.askopenfilename(initialdir = "/",title = "Select .SRM file", filetypes = ((".SRM File","*.srm"),("All files","*.*")))
    base = os.path.basename(inputf)
    if os.path.splitext(base)[1] == '.srm':
        srm = inputf
    else:
        messagebox.showerror("Error: File not valid", "You must select a .SRM File")
    pass

def convert_ves_to_srm():
    if ves != None:
        output1['text'] = ves_to_srm(ves)
    else:
        output1['text'] = 'No file selected.'
    pass

def convert_srm_to_ves():
    if srm != None and gpid.get() != '':
        if len(gpid.get()) == 4:
            output2['text'] = srm_to_ves(srm, gpid.get())
        else:
            output2['text'] = 'Invalid GPID.'
    else:
        output2['text'] = 'Missing variable.'
    pass

#
# INFO
#
info = LabelFrame(root, text='Info', padx=5, pady=5)
info.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

infolbl = Label(info, text = '3DS SNES Save Converter\ngithub.com/manuGMG/3ds-snes-sc', pady=12)
infolbl.pack(side = TOP)

#
# ACTIONS
# 
actions = LabelFrame(root, text='Actions', padx=5, pady=5)
actions.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

output1 = Label(actions, text = '(Output File)', padx=5)
output1.grid(row=0, column=1, sticky='nsew')

btn = Button(actions, text ='VES to SRM', command=convert_ves_to_srm)
btn.grid(row=0, column=0, pady=3, sticky='nsew')

btn = Button(actions, text ='SRM to VES', command=convert_srm_to_ves)
btn.grid(row=1, column=0, sticky='nsew')

output2 = Label(actions, text = '(Output File)', padx=5)
output2.grid(row=1, column=1, sticky='nsew')

#
# VES TO SRM
# 
frame = LabelFrame(root, text='Convert from .VES to .SRM', padx=5, pady=5)
frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

lbl = Label(frame, text = 'Select .VES File:')
lbl.pack(side = LEFT)

btn = Button(frame, text ='Select..', width='7', command=select_ves)
btn.pack(side = LEFT)

#
# SRM TO VES
# 
frame2 = LabelFrame(root, text='Convert from .SRM to .VES', padx=5, pady=5)
frame2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

lbl = Label(frame2, text = 'Select .SRM File:')
lbl.grid(row=0, column=0, sticky='nsew')

btn = Button(frame2, text ='Select..', width='7', command=select_srm)
btn.grid(row=0, column=1, pady=3, sticky='nsew')

lbl2 = Label(frame2, text = 'Game Preset ID:')
lbl2.grid(row=1, column=0, sticky='nsew')

gpid = Entry(frame2, width='7')
gpid.grid(row=1, column=1, sticky='nsew')

mainloop()
