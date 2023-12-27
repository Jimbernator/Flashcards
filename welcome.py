import tkinter as tk
import os
from tkinter import messagebox, filedialog
from flashcard import load_flashcards
from gui import FlashcardApp

class WelcomeScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to Flash Card Game")

        self.deck_listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.deck_listbox.pack(pady=10)

        self.load_decks_button = tk.Button(master, text="Load Flash Card Deck", command=self.load_deck)
        self.load_decks_button.pack(pady=10)

    def load_deck(self):
        selected_index = self.deck_listbox.curselection()
        if selected_index:
            selected_deck = self.deck_listbox.get(selected_index)
            self.master.destroy()  # Close the welcome screen
            run_flashcard_app(selected_deck)
        else:
            messagebox.showwarning("No Deck Selected", "Please select a flash card deck.")

def run_flashcard_app(file_path):
    flashcards = load_flashcards("decks/"+file_path)

    print(file_path)

    if not flashcards:
        messagebox.showerror("Error", "Failed to load flash cards. Exiting program.")
        return

    root = tk.Tk()
    root.title("Flash Card Game")
    app = FlashcardApp(root, flashcards)
    root.mainloop()

def main():
    welcome_root = tk.Tk()
    welcome_screen = WelcomeScreen(welcome_root)

    decks_folder = "decks/"
    available_decks = [f for f in os.listdir(decks_folder) if f.endswith(".txt")]

    if not available_decks:
        messagebox.showerror("Error", "No flash card decks found in the 'decks/' folder. Exiting program.")
        welcome_root.destroy()  # Close the welcome screen
        return

    welcome_screen.deck_listbox.delete(0, tk.END)  # Clear the listbox
    for deck in available_decks:
        welcome_screen.deck_listbox.insert(tk.END, deck)

    welcome_root.mainloop()

if __name__ == "__main__":
    main()
