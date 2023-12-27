import os
import time

def load_flashcards(file_path):
    """Load flash cards from a text file."""
    if not os.path.isfile(file_path):
        print(f"Error: File not found - {file_path}")
        return []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    flashcards = [(lines[i].strip(), lines[i + 1].strip()) for i in range(0, len(lines), 2)]
    return flashcards

def flashcard_game(flashcards):
    """Flash card game loop."""
    for front, back in flashcards:
        print("Front of the card:")
        print(front)
        input("Press Enter to reveal the back of the card...")
        print("Back of the card:")
        print(back)
        input("Press Enter for the next card...")

def main():
    # file_path = input("Enter the path of the flash card deck file: ")
    file_path = "decks/demo.txt"
    flashcards = load_flashcards(file_path)

    if not flashcards:
        print("Exiting program.")
        return

    print("Welcome to the Flash Card Game!")
    input("Press Enter to start the game...")

    flashcard_game(flashcards)

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
