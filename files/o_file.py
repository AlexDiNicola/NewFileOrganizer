from tkinter import filedialog
def openFile():
    file_path = filedialog.askopenfilename()
    print("File selezionato:", file_path)
    return file_path