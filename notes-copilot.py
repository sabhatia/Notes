import tkinter as tk
import json

root = tk.Tk()
notes = []

def save_notes():
    with open('notes-copilot.json', 'w') as f:
        json.dump(notes, f)

def add_note():
    note = note_entry.get()
    notes.append(note)
    note_entry.delete(0, tk.END)
    save_notes()

def edit_note():
    selected_note = notes_listbox.curselection()[0]
    note_entry.delete(0, tk.END)
    note_entry.insert(0, notes[selected_note])

def delete_note():
    selected_note = notes_listbox.curselection()[0]
    notes.pop(selected_note)
    save_notes()

notes_label = tk.Label(root, text="Notes")
notes_label.pack()

notes_listbox = tk.Listbox(root)
notes_listbox.pack()

note_entry = tk.Entry(root)
note_entry.pack()

add_button = tk.Button(root, text="Add Note", command=add_note)
add_button.pack()

edit_button = tk.Button(root, text="Edit Note", command=edit_note)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Note", command=delete_note)
delete_button.pack()

root.mainloop()
