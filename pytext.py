import tkinter as tk
from tkinter import filedialog


class Menubar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File", command=parent.set_window_title)
        file_dropdown.add_command(label="Open File", command=parent.open_file)
        file_dropdown.add_command(label="Save", command=parent.save)
        file_dropdown.add_command(label="Save As", command=parent.save_as)
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

        self.filename = None

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

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Untitled - PyText")

    def new_file(self):
        pass

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)


    def save(self):
        pass

    def save_as(self):
        pass


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
