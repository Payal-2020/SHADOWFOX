import random 
WORDS=["ALGORITHM","SOFTWARE","INTERNET","HARDWARE","DATABASE","FRAMEWORK","FUNCTION","VARIABLE","TERMINAL","COMPILER","DEBUG","OPERATING","SECURITY","CLOUD","GALAXY","MOUNTAIN","TELEVISION","KEYBOARD"]


HANGMAN_ART = [
    """
      +---+
      |   |
          |
          |
          |
        ===
    """,
    """
      +---+
      |   |
      O   |
          |
          |
        ===
    """, 
    """
      +---+
      |   |
      O   |
      |   |
          |
        ===
    """, 
    """
      +---+
      |   |
      O   |
     /|   |
          |
        ===
    """, 
    """
      +---+
      |   |
      O   |
     /|\  |
          |
        ===
    """, 
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
        ===
    """, 
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
        ===
    """ 
]

def choose_word(word_list):
    
    return random.choice(word_list)

def display_game_state(word, guessed, incorrect, max_attempts):
    display_word = "".join([letter + " " if letter in guessed else "_ " for letter in word ])
    print("\n" + "="*40)
    print(f"WORD: {display_word}")
    
    print(HANGMAN_ART[incorrect])
    print(f"Incorrect guesses left: {max_attempts - incorrect}")
    print(f"Guessed letters: {', '.join(sorted(list(guessed)))}")
    print("="*40)


def get_player_guess(guessed_set):
    """Prompts player for input and ensures it is a valid, un-guessed letter."""
    while True:
        guess = input("Enter your guess (a single letter): ").upper()
        if len(guess) != 1 or not 'A' <= guess <= 'Z':
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_set:
            print("You already guessed that letter. Try again.")
        else:
            return guess


def game_loop(word, max_attempts):
    guessed_letters = set()
    incorrect_guesses = 0
    
    while incorrect_guesses < max_attempts:
        display_game_state(word, guessed_letters, incorrect_guesses, max_attempts)
        
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: {word}!")
            return 
            
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
    
    display_game_state(word, guessed_letters, incorrect_guesses, max_attempts) 
    print(f"\n😭 GAME OVER! The word was: {word}")


def main():
    MAX_ATTEMPTS = 6 
    print("WELCOME TO THE HANGMAN GAME!")
    
    while True:
        chosen_word = choose_word(WORDS)
        print("\n--- Starting New Game ---")
        
        game_loop(chosen_word, MAX_ATTEMPTS)

        play_again = input("\nDo you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()