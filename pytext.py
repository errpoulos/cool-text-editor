import tkinter as tk


class Menubar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File", command=parent.set_window_title)
        file_dropdown.add_command(label="Open File", command=parent.new_file)
        file_dropdown.add_command(label="Save", command=parent.open_file)
        file_dropdown.add_command(label="Save As", command=parent.save)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit")

        menubar.add_cascade(label="File", menu=file_dropdown)


class PyText:
    def __init__(self, master):
        # Default title
        master.title("Untitled-pytext")
        # Default canvas size
        master.geometry("1200x700")
        # set font
        font_specs = ("ubuntu", 18)
        self.master = master

        # initialize textarea
        self.textarea = tk.Text(master, font=font_specs)
        # initialize scrollbar
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview())
        # initialize vertical scroll
        self.textarea.configure(yscrollcommand=self.scroll.set)
        # constrain textarea and scroll to size of widget
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)


def set_window_title(self):
    pass


def new_file(self):
    pass


def open_file(self):
    pass


def save(self):
    pass


def save_as(self):
    pass


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
