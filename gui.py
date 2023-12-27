import tkinter as tk
from tkinter import messagebox
# import flashcard
from flashcard import load_flashcards

class FlashcardApp:
    def __init__(self, master, flashcards):
        self.master = master
        self.flashcards = flashcards
        self.current_card_index = 0
        self.showing_front = True

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.show_button = tk.Button(master, text="Show Back", command=self.toggle_card)
        self.show_button.pack()

        self.next_button = tk.Button(master, text="Next Card", command=self.next_card)
        self.next_button.pack()

        self.show_card()

    def toggle_card(self):
        self.showing_front = not self.showing_front
        self.show_card()

    def next_card(self):
        self.current_card_index += 1
        self.showing_front = True
        self.show_card()

    def show_card(self):
        if self.current_card_index < len(self.flashcards):
            if self.showing_front:
                card_text = self.flashcards[self.current_card_index][0]
                self.show_button.config(text="Show Back")
            else:
                card_text = self.flashcards[self.current_card_index][1]
                self.show_button.config(text="Show Front")

            self.label.config(text=card_text)
        else:
            self.current_card_index -= 1
            messagebox.showinfo("Game Over", "No more cards!")

            # If you want to reset the game after reaching the end of the cards,
            # uncomment the following lines:
            # self.current_card_index = 0
            # self.showing_front = True
            # self.show_card()

def main():
    # file_path = input("Enter the path of the flash card deck file: ")
    file_path = "decks/demo.txt"
    flashcards = load_flashcards(file_path)

    if not flashcards:
        print("Exiting program.")
        return

    root = tk.Tk()
    root.title("Flash Card Game")
    app = FlashcardApp(root, flashcards)
    root.mainloop()

if __name__ == "__main__":
    main()
