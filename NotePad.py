import tkinter as tk 
from tkinter import filedialog


# call back function

def New_file():
    TextArea.delete(1.0, tk.END)
def Open_file():
    global File_path
    File_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    TextArea.delete(1.0, tk.END)
    with open(File_path, "r", encoding="utf8") as file:
        TextArea.insert(tk.INSERT, file.read())
    print(File_path)    
    
def Save_file():
    global File_path
    if File_path:
        try:
            with open(File_path, "w", encoding="utf-8") as file:
                file.write(TextArea.get(1.0, tk.END))
        except:
            print("Error while saving the file.")        
def Save_as():
    global File_path
    File_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if File_path:
        try:
            with open(File_path, "w", encoding="utf8") as file:
                file.write(TextArea.get(1.0, tk.END))
        except:
            print("Error while saving the file.")

def Copy():
    TextArea.event_generate(("Copy"))

def Cut():
    TextArea.event_generate(("Cut"))
def Paste():
    TextArea.event_generate(("Paste"))    
#---------------------------------------------------------------- 


window = tk.Tk()
window.title = ("Bloc de Notas")
window.geometry("900x600")

menu = tk.Menu(window)
window.config(menu=menu)

archive = tk.Menu(menu)
menu.add_cascade(label="Archives", menu=archive)

edit = tk.Menu(menu)
menu.add_cascade(label="edit", menu=edit)

TextArea = tk.Text(window)
TextArea.pack(fill=tk.BOTH, expand = True)

archive.add_command(label="New file", command= New_file)
archive.add_command(label="Open file", command= Open_file)
archive.add_command(label="Save file", command= Save_file)
archive.add_command(label="Save as", command= Save_as)

edit.add_command(label="Copy", command= Copy)
edit.add_command(label="Paste", command= Paste)
edit.add_command(label="Cut", command = Cut)

window.mainloop()