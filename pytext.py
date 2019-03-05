import tkinter as tk


class PyText:
    def __init__(self, master):
        # Default title
        master.title("Untitled-pytext")

        #Default canvas size
        master.geometry("1200x700")

        #initialize textarea
        self.textarea = tk.Text(master)

        # initialize scrollbar
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview())

        # initialize vertical scroll
        self.textarea.configure(yscrollcommand=self.scroll.set)

        # constrain textarea and scroll to size of widget
        self.textarea.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.RIGHT)


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
