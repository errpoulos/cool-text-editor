import tkinter as tk

class PyText:
    def __init__(self, master):
        master.title("Untitled-pytext")
        master.geometry("1200x700")
       

if __name__== "__main__":
    master = tk.Tk()
    pt=PyText(master)
    master.mainloop()
