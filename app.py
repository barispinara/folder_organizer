import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sv_ttk
from organizer import Organizer

def organizer_folder(folder_path:str):
    if not folder_path:
        messagebox.showwarning("No Folder Selected", "Please select a folder first")
        return
    try:
        organizer = Organizer(given_path=folder_path)
    except Exception as e:
        messagebox.showerror("Error" , e)
        return
    file_count, returned_message = organizer.start_organize_files()
    status_var.set(f"{file_count} files were organized")
    messagebox.showinfo("Message" , returned_message)

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

root = tk.Tk()
root.title("Folder Organizer")
root.geometry("500x180")
root.resizable(False, False)

sv_ttk.use_dark_theme()

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

folder_label = ttk.Label(frame, text="Selected Folder:")
folder_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

folder_var = tk.StringVar()
folder_entry = ttk.Entry(frame, textvariable=folder_var, width=45)
folder_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = ttk.Button(frame, text="...", width=3, command=select_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Organizer button
organize_button = ttk.Button(frame, text="Organize", command=lambda: organizer_folder(folder_var.get()))
organize_button.grid(row=1, column=0, columnspan=3, pady=15)

# Status label for file count which is replaced
status_var = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_var, anchor="center")
status_label.pack(pady=10)

frame.columnconfigure(1, weight=1)

root.mainloop()