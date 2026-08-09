from tkinter import filedialog
import tkinter as tk

# tkinter needs a root window to exist, even if we never show it
root = tk.Tk()
root.withdraw()  # hide the empty root window - we only want the dialog

path = filedialog.askopenfilename(
    title="Select CAD export file",
    filetypes=[("Text files", "*.txt")]
)

print(path)