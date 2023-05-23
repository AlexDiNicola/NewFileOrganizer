import tkinter as tk
from files.o_file import openFile

if __name__ == "__main__":
    window = tk.Tk()

    window.title("New File Organizer")

    window.geometry("700x500")

    file = tk.Button(window, text="Open file...", command=openFile())
    file.pack()

    window.mainloop()
