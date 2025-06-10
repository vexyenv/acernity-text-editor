import tkinter as tk
from tkinter import messagebox, font
from tkinter.filedialog import askopenfilename, asksaveasfilename

themes = {
    "dark": {
        "bg": "#1a1a1a",
        "text_bg": "#2b2b2b",
        "text_fg": "#ffffff",
        "cursor": "#00BFFF",
    },
    "light": {
        "bg": "#f0f0f0",
        "text_bg": "#ffffff",
        "text_fg": "#000000",
        "cursor": "#1900FF",
    },
}

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
    default_font_family = "Consolas"
    current_font = font.Font(family=default_font_family, size=16)
    textEdit = tk.Text(
        window,
        font=current_font,
        bg="#2b2b2b",
        fg="#ffffff",
        insertbackground="#00BFFF",
    )
    textEdit.grid(row=0, column=1)
    currentTheme = {"mode": "dark"}

    def apply_theme(mode):
        theme = themes[mode]
        window.configure(bg=theme["bg"])
        textEdit.configure(
            bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["cursor"]
        )
        currentTheme["mode"] = mode

    # Toggle function
    def toggle_theme():
        new_mode = "light" if currentTheme["mode"] == "dark" else "dark"
        apply_theme(new_mode)

    apply_theme("dark")

    scrollbar = tk.Scrollbar(window, command=textEdit.yview)
    textEdit.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky="ns")

    menubar = tk.Menu(window)
    fileMenu = tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label="New", command=lambda: textEdit.delete(1.0, tk.END))
    fileMenu.add_command(label="Open", command=lambda: openFile(window, textEdit))
    fileMenu.add_command(label="Save", command=lambda: saveFile(window, textEdit))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=fileMenu)

    viewMenu = tk.Menu(menubar, tearoff=0)
    viewMenu.add_command(label="Toggle Theme", command=toggle_theme)
    menubar.add_cascade(label="View", menu=viewMenu)

    fontMenu = tk.Menu(menubar, tearoff=0)
    font_families = [
        "Consolas",
        "Courier",
        "Arial",
        "Times New Roman",
        "Calibri",
        "Lucida Console",
    ]

    def change_font(family):
        current_font.configure(family=family)

    for fam in font_families:
        fontMenu.add_command(label=fam, command=lambda f=fam: change_font(f))
    menubar.add_cascade(label="Font", menu=fontMenu)

    helpMenu = tk.Menu(menubar, tearoff=0)
    helpMenu.add_command(
        label="About",
        command=lambda: messagebox.showinfo(
            "About", "Acernity Text Editor\nVersion 1.0"
        ),
    )

    menubar.add_cascade(label="Help", menu=helpMenu)

    window.config(menu=menubar)

    window.bind("<Control-s>", lambda event: saveFile(window, textEdit))
    window.bind("<Control-o>", lambda event: openFile(window, textEdit))
    window.bind("<Control-n>", lambda event: textEdit.delete(1.0, tk.END))
    window.bind("<Control-t>", lambda event: toggle_theme())

    window.mainloop()

main()