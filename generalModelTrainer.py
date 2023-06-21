from tkinter import *
from tkinter.filedialog import askopenfilename as openFile
from os.path import splitext
import pandas as pd
from tkinter import messagebox

root = Tk()
root.title("General Model Trainer")
root.geometry("1920x1080")

df = None

def chooseDataset():
    fPath = openFile(title = "Choose Dataset", filetypes = (("CSV Files", "*.csv"), ("Excel File", "*.xlsx")))
    fName, fExtn = splitext(fPath)
    if fExtn == ".csv":
        data = pd.read_csv(fPath)
    elif fExtn == ".xlsx":
        data = pd.read_excel(fPath)
    else:
        messagebox.showerror(title = "Format Not Supported!", message = "The slected file format is not supported.")
    df = data

def dataPrint():
    if df:
        print(df)
    else:
        messagebox.showerror(title = "File Not Chosen!", message = "File has not been selected.")

titleFont = ("Calibri", 36, "bold")

titleLabel = Label(root, text = "Generalized Model Trainer", font = titleFont, pady = 5).pack()#grid(row = 0, column = 8)

chooseDatasetButton = Button(root, text = "Choose Dataset", command = chooseDataset).pack()
chooseDatasetButto = Button(root, text = "Print Data", command = dataPrint).pack()
root.mainloop()