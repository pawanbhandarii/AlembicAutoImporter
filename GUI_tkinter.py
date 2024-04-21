import tkinter as tk
from tkinter import filedialog

class FileUpdateCheckerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Update Checker")
        
        self.directory_to_check = tk.StringVar()
        self.extension = ".fbx"
        self.json_file = ""
        
        self.create_widgets()

    def create_widgets(self):
        # Directory to check label and entry
        tk.Label(self.root, text="Directory to Check:").grid(row=0, column=0, sticky="w")
        self.dir_entry = tk.Entry(self.root, textvariable=self.directory_to_check, width=50)
        self.dir_entry.grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2)

        # Extension label and entry
        tk.Label(self.root, text="File Extension:").grid(row=1, column=0, sticky="w")
        self.extension_entry = tk.Entry(self.root, width=10)
        self.extension_entry.insert(tk.END, self.extension)
        self.extension_entry.grid(row=1, column=1)

        # JSON file label and entry
        tk.Label(self.root, text="JSON File:").grid(row=2, column=0, sticky="w")
        self.json_entry = tk.Entry(self.root, width=50)
        self.json_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_json_file).grid(row=2, column=2)

        # Check button
        tk.Button(self.root, text="Check for Updates", command=self.check_updates).grid(row=3, column=1)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_to_check.set(directory)

    def browse_json_file(self):
        json_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if json_file:
            self.json_file = json_file
            self.json_entry.insert(tk.END, json_file)

    def check_updates(self):
        directory = self.directory_to_check.get()
        extension = self.extension_entry.get()
        json_file = self.json_entry.get()

        if directory and json_file:
            # Your code to check updates goes here
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FileUpdateCheckerGUI()
    app.run()
