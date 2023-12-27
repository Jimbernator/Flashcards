import tkinter as tk
import os
import subprocess
from tkinter import messagebox, filedialog
from flashcard import load_flashcards
from gui import FlashcardApp

class WelcomeScreen:
    def __init__(self, master, decks_folder):
        self.master = master
        self.master.title("Welcome to Flash Card Game")
        self.decks_folder = decks_folder

        self.refresh_button = tk.Button(master, text="Refresh List", command=self.refresh_list)
        self.refresh_button.pack(pady=10)

        self.deck_listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.deck_listbox.pack(pady=10)

        self.load_decks_button = tk.Button(master, text="Load Flash Card Deck", command=self.load_deck)
        self.load_decks_button.pack(pady=10)

        self.open_folder_button = tk.Button(master, text="Open Decks Folder", command=self.open_decks_folder)
        self.open_folder_button.pack(pady=10)

        self.available_decks = self.get_available_decks()
        self.refresh_list()

    def get_available_decks(self):
        return [f for f in os.listdir(self.decks_folder) if f.endswith(".txt")]

    def load_deck(self):
        selected_index = self.deck_listbox.curselection()
        if selected_index:
            selected_deck = self.deck_listbox.get(selected_index)
            self.master.destroy()  # Close the welcome screen
            run_flashcard_app(selected_deck, self.decks_folder)
        else:
            messagebox.showwarning("No Deck Selected", "Please select a flash card deck.")

    def open_decks_folder(self):
        subprocess.Popen(['explorer', os.path.abspath(self.decks_folder)])

    def refresh_list(self):
        self.available_decks = self.get_available_decks()
        self.deck_listbox.delete(0, tk.END)  # Clear the listbox
        for deck in self.available_decks:
            self.deck_listbox.insert(tk.END, deck)

def run_flashcard_app(file_name, decks_folder):
    flashcards = load_flashcards(os.path.join(decks_folder, file_name))

    if not flashcards:
        messagebox.showerror("Error", "Failed to load flash cards. Exiting program.")
        return

    root = tk.Tk()
    root.title("Flash Card Game")
    app = FlashcardApp(root, flashcards)
    root.mainloop()

def main():
    welcome_root = tk.Tk()
    decks_folder = "decks/"
    welcome_screen = WelcomeScreen(welcome_root, decks_folder)

    welcome_root.mainloop()

if __name__ == "__main__":
    main()
