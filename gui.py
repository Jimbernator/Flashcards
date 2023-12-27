import tkinter as tk
from tkinter import messagebox
# import flashcard
from flashcard import load_flashcards

class FlashcardApp:
    def __init__(self, master, flashcards):
        self.master = master
        self.flashcards = flashcards
        self.current_card_index = 0

        self.front_label = tk.Label(master, text="")
        self.front_label.pack()

        self.show_front()

        next_button = tk.Button(master, text="Next Card", command=self.show_front)
        next_button.pack()

    def show_front(self):
        if self.current_card_index < len(self.flashcards):
            front_text = self.flashcards[self.current_card_index][0]
            self.front_label.config(text=front_text)
            self.current_card_index += 1
        else:
            messagebox.showinfo("Game Over", "No more cards!")

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
