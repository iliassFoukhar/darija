#Modules used
from tkinter import *
from tkinter import filedialog
from tkinter import ttk




#My tools
import Lexer
import Parser

#Variables
bg_lines = "#232323"
bg_text = "#121212"
textcolor = "lightgreen"
active_color = "lightgreen"
h = 33
w = 150


#Functions
def save_as():
    global text
    t = text.get("1.0", "end-1c")
    ftypes = [('Codat b darija', '.darija'),('All files', '*')]
    savelocation=filedialog.asksaveasfilename(filetypes=ftypes,defaultextension=".darija")
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

def run_parser():
    global text
    source_code = text.get("1.0", "end")
    if "ma7ed" not in source_code and "fkoula" not in source_code:
        Parser.build_parser(source_code)
    update_variables()


def insert_line_numbers():
    global lines
    data = ""
    for i in range(1, 1000):
        data += str(i) + "\n"
    lines.insert(END,data)

def viewall(*args):
    global lines, text
    lines.yview(args[0])
    text.yview(args[0])

def update_variables():
    global variables
    vs = Parser.variables
    
    data = "Motaghayriat dyalk\n\n"
    #Get data
    for k in vs:
        line = f'{str(vs[k].get_type())} := {vs[k].get_name()} := {vs[k].get_value()} \n\n'
        data += line
    
    #Update the widget
    variables.configure(state='normal')
    variables.delete("1.0", END)
    variables.insert(END, data)
    variables.configure(state='disabled')

#IDE Implementation
root = Tk("Text Editor")
#root.state('zoomed')
root.title("IDE b darija: Untitled")
root.configure(bg='#333333')


#Line numbers
lines = Text(root, background=bg_lines, foreground=textcolor, pady=5, padx=5, width=5, height=h, insertbackground="#232323")
lines.grid(row=0, column=0, sticky=(N, W, E, S))
insert_line_numbers()
lines.configure(state='disabled')


#Text widget
text = Text(root, background=bg_text, foreground=textcolor, pady=5, padx=5, width=w, height=h, insertbackground="#eee")
text.grid( row=0, column=1, sticky=(N, W, E, S))

#Variables used
variables = Text(root, background="#343434", foreground=textcolor, height=h, pady=5, padx=15)
variables.grid(row=0, column=3, sticky=(N, W, E, S))
variables_title = "Motaghayriat dyalk"
variables.insert(END,variables_title)
variables.configure(state='disabled')


#Same scrolling for the two text widgets 
rolly = ttk.Scrollbar(root, orient=VERTICAL, command=viewall)
text['yscrollcommand'] = rolly.set
lines['yscrollcommand'] = rolly.set
rolly.grid(row=0, column=2, sticky=(N, W, E, S))

#Menu
menubar = Menu(root, activebackground=active_color) 
menubar.add_command(label="Fte7", command=open_file)  
menubar.add_command(label="Sjjl", command=save_as)  
menubar.add_command(label="Lexer", command=run_code)  
menubar.add_command(label="Khddm", command=run_parser)  
root.config(menu=menubar)  


#Loop
root.mainloop()



#Buttons
#saveButton = Button(root, text="Save", command=save_as,padx=15, pady=3,background=textcolor)
#saveButton.grid(column=0, row=1) 

# openButton = Button(root, text="Open", command=open_file,padx=15, pady=3, background="#666", foreground="skyblue")
# openButton.grid(column=1, row=1, rowspan=1)

# runButton = Button(root, text="Run", command=run_code,padx=15, pady=3, background=textcolor)
# runButton.grid(column=2, row=1)