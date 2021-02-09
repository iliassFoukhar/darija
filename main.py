#Modules used
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

#My tools
import Lexer
import Parser

#Variables
root_bg = ('#333333', '#DDDDDD')
bg_lines = ("#232323", "#FEFEFE")
bg_text = ("#121212", "#EDEDED")
textcolor = ("lightgreen", "black")
active_color = ("lightgreen", "black")
insert_color = ('#EEEEEE', '#111111')
variables_bg = ('#343434', '#DCDCDC')
h = 33
w = 150
color = 0

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
    empty_variables()
    source_code = ""
    source_code = text.get("1.0", "end")
    Parser.run_the_code(source_code) #ll=
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

def empty_variables():
    Parser.variables.clear()
    update_variables()

def change_colors():
    global variables, text, lines, color
    if color == 0:
        color = 1
    else:
        color = 0
    variables.configure(bg=variables_bg[color])
    variables.configure(fg=textcolor[color])
    text.configure(bg=bg_text[color])
    text.configure(fg=textcolor[color])
    text.configure(insertbackground=insert_color[color])
    lines.configure(bg=bg_lines[color])
    lines.configure(fg=textcolor[color])

#IDE Implementation
root = Tk("Text Editor")
#root.state('zoomed')
root.title("IDE b darija: Untitled")
root.configure(bg=root_bg[color])


#Line numbers
lines = Text(root, background=bg_lines[color], foreground=textcolor[color], pady=5, padx=5, width=5, height=h, insertbackground=insert_color[color])
lines.grid(row=0, column=0, sticky=(N, W, E, S))
insert_line_numbers()
lines.configure(state='disabled')


#Text widget
text = Text(root, background=bg_text[color], foreground=textcolor[color], pady=5, padx=5, width=w, height=h, insertbackground=insert_color[color])
text.grid( row=0, column=1, sticky=(N, W, E, S))

#Variables used
variables = Text(root, background=variables_bg[color], foreground=textcolor[color], height=h, pady=5, padx=15)
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
menubar = Menu(root, activebackground=active_color[color]) 
menubar.add_command(label=" Fte7 ", command=open_file)  
menubar.add_command(label=" Sjjl  ", command=save_as)  
menubar.add_command(label=" Khwi Motaghayirat ", command=empty_variables)
menubar.add_command(label=" Bddel Lwanat ", command=change_colors)
menubar.add_command(label=" Lexer  ", command=run_code)  
menubar.add_command(label=" Khddm  ", command=run_parser)
root.config(menu=menubar)  


#Loop
root.mainloop()

