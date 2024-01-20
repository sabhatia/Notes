import tkinter as tk

def save_note():
    note = note_entry.get("1.0", tk.END)
    with open("notes-bard.txt", "a") as f:
        f.write(note + "\n")
    note_entry.delete("1.0", tk.END)

# Create main window and widgets
window = tk.Tk()
window.title("Note Taking App")
note_entry = tk.Text(window)
save_button = tk.Button(window, text="Save", command=save_note)

# Display widgets
note_entry.pack()
save_button.pack()

window.mainloop()
  