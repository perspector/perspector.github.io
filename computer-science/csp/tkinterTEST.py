from tkinter import Tk
from tkinter import ttk

unitOptions = []
unitConversions = []

def chooseUnit(units):
    if units == "distance":
        unitOptions = ['pm', 'nm', 'mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'Mm', 'Gm', 'Tm']
        unitConversions = [1000000000000, 1000000000, 1000000, 1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.000001, 0.000000001, 0.000000000001]
    elif units == "weight":
        unitOptions = []

root = Tk()
root.title("Unit Converter")
root.geometry('400x400')
frame = ttk.Frame(root, padding=10)
frame.pack()


ttk.Label(root, text="Unit Type:")
ttk.Combobox(root, values=unitOptions).pack()
ttk.Button(text="Choose", command=chooseUnit).pack()



ttk.Combobox()
ttk.Button(text="Switch")
ttk.Combobox()
ttk.Button(text="Convert")

root.mainloop()

def convert(unitIn, unitOut):
    
    return output
