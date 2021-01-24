#Modules used
from tkinter import *
from tkinter import filedialog
#import importlib
import Lexer

#Functions
def save_as():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def open_file():
    global text
    file_path = filedialog.askopenfilename()
    file_name = file_path.split("/")
    with open(file_path,'r') as file:
        data = file.read()
        text.delete("1.0", END)
        text.insert(END,data)
        root.title("IDE b darija: {0}".format(file_name[-1]))

def run_code():
    global text
    Lexer.build_lexer(text.get("1.0","end"))
 

#IDE Implementation
root = Tk("Text Editor")
root.title("IDE b darija: Untitled")
text = Text(root, background="#eee", foreground="#000", pady=3, padx=3)

text.grid( row=0, column = 1)

#Buttons
saveButton = Button(root, text="Save", command=save_as,padx=15, pady=3,background="lightgreen")
saveButton.grid(column=0, row=1) 

openButton = Button(root, text="Open", command=open_file,padx=15, pady=3, background="skyblue")
openButton.grid(column=1, row=1)

runButton = Button(root, text="Run", command=run_code,padx=15, pady=3, background="lightgreen")
runButton.grid(column=2, row=1)
#Loop
root.mainloop()