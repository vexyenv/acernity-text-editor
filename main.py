import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openFile(window, textEdit):
    filepath = askopenfilename(filetypes=[("Text files", "*.txt")])

    if not filepath:
        return

    textEdit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        textEdit.insert(tk.END, content)
    window.title(f"Open file: {filepath}")


def saveFile(window, textEdit):
    filepath = asksaveasfilename(filetypes=[("Text files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = textEdit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Save file: {filepath}")


def main():
    window = tk.Tk()
    window.title("Acernity Text Editor")
    window.configure(bg="#1a1a1a")
    window.grid_rowconfigure(0, minsize=400)
    window.grid_columnconfigure(1, minsize=500)
    textEdit = tk.Text(
        window,
        font="Consolas 16",
        bg="#2b2b2b",
        fg="#ffffff",
        insertbackground="#00BFFF",
    )
    textEdit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=1, bg="#1F1F1F")
    saveButton = tk.Button(frame, text="Save", command=lambda: saveFile(window, textEdit))
    openButton = tk.Button(frame, text="Open", command=lambda: openFile(window, textEdit))

    saveButton.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    openButton.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda event: saveFile(window, textEdit))
    window.bind("<Control-o>", lambda event: openFile(window, textEdit))

    window.mainloop()

main()