import os
import customtkinter
from customtkinter import CTk, CTkButton, CTkRadioButton, CTkScrollableFrame
from PIL import Image

import subprocess
from tkinter import messagebox
from flashcard import load_flashcards
from gui import FlashcardApp

class ScrollableRadiobuttonFrame(CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def clear_options(self):
        for radiobutton in self.radiobutton_list:
            radiobutton.destroy()
        self.radiobutton_list = []

    def add_item(self, item):
        radiobutton = CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(sticky="w", pady=(0, 10))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()

class WelcomeScreen(CTk):
    def __init__(self, decks_folder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Welcome to Flash Card Game")

        self.decks_folder = decks_folder
        self.available_decks = self.get_available_decks()

        self.refresh_button = CTkButton(self, text="Refresh List", command=self.refresh_list)
        self.refresh_button.pack(pady=10)

        self.deck_frame = ScrollableRadiobuttonFrame(self, item_list=self.available_decks, command=self.on_radiobutton_change)
        self.deck_frame.pack(pady=10)

        self.load_decks_button = CTkButton(self, text="Load Flash Card Deck", command=self.load_deck)
        self.load_decks_button.pack(pady=10)

        self.open_folder_button = CTkButton(self, text="Open Decks Folder", command=self.open_decks_folder)
        self.open_folder_button.pack(pady=10)

    def get_available_decks(self):
        return [f for f in os.listdir(self.decks_folder) if f.endswith(".txt")]

    def load_deck(self):
        selected_deck = self.deck_frame.get_checked_item()

        if selected_deck:
            ''' ".after" used in scaling_tracker.py etc do no gracefull shutdown
             timer events, so destory() is messy. exit() can be used.
            '''
            # self.destroy()  # Close the welcome screen

            # Run the flashcard app
            run_flashcard_app(selected_deck, self.decks_folder)
        else:
            messagebox.showwarning("No Deck Selected", "Please select a flash card deck.")

    def open_decks_folder(self):
        subprocess.Popen(['explorer', os.path.abspath(self.decks_folder)])

    def refresh_list(self):
        self.available_decks = self.get_available_decks()
        self.deck_frame.clear_options()  # Clear existing options
        for deck in self.available_decks:
            self.deck_frame.add_item(deck)

    def on_radiobutton_change(self):
        # Add any custom behavior when a radiobutton is selected
        pass

def run_flashcard_app(file_name, decks_folder):
    flashcards = load_flashcards(os.path.join(decks_folder, file_name))

    if not flashcards:
        messagebox.showerror("Error", "Failed to load flash cards. Exiting program.")
        return

    root = CTk()
    root.title("Flash Card Game")
    app = FlashcardApp(root, flashcards)
    root.mainloop()

def main():
    decks_folder = "decks/"
    welcome_screen = WelcomeScreen(decks_folder)
    welcome_screen.mainloop()

if __name__ == "__main__":
    main()
