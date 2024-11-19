import random

def print_hangman(tries):
    stages = [
        """
        _______
        |       |
        |       O
        |      /|\\
        |      / \\
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      / 
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|
        |      
        |
        """,
        """
        _______
        |       |
        |       O
        |       
        |      
        |
        """,
        """
        _______
        |       |
        |       
        |       
        |      
        |
        """,
    ]
    return stages[6 - tries]

def hangman():
    word_list = ['banana', 'cherry', 'date', 'elderberry',"baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
    chosen_word = random.choice(word_list)
    display = ["_"] * len(chosen_word)
    tries = 6
    guessed = []

    print("🎉 Welcome to Hangman! 🎉")
    print(f"The word has {len(chosen_word)} letters: {' '.join(display)}")
    
    while tries > 0 and "_" in display:
        print(print_hangman(tries))
        print(f"Guessed letters: {', '.join(guessed) if guessed else 'None yet'}")
        print(f"Word: {' '.join(display)}")
        print(f"Tries left: {tries}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
        elif guess in guessed:
            print("⚠ You already guessed that letter.")
        elif guess in chosen_word:
            print("✅ Correct guess!")
            guessed.append(guess)
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display[i] = guess
        else:
            print("❌ Wrong guess!")
            guessed.append(guess)
            tries -= 1
    
    print(print_hangman(tries))
    if "_" not in display:
        print(f"🎉 Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"💔 Out of tries! The word was: {chosen_word}")

if __name__ == "__main__":
    hangman()