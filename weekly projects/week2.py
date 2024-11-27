import random

# List of words for the game
words = ["oxygen","frazzled","frizzled","fuchsia","funny", "galaxy", "abyss",]

# Pick a random word
word = random.choice(words)
hidden_word = "_" * len(word)
attempts = 6
guessed_letters = [] #keeps track of guessed letters

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters: {hidden_word}") #shows the length of the word to be guessed

while attempts > 0:
    print(f"Attempts left: {attempts}") #prints attempts left
    print("Guessed letters:", " ".join(guessed_letters)) #prints numbers guessed
    print("Word:", " ".join(hidden_word)) #prints hidden word
    
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        new_hidden_word = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_hidden_word += guess
            else:
                new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts -= 1

    if "_" not in hidden_word:
        print("\nCongratulations! You guessed the word:", word)
        break
else:
    print("\nYou ran out of attempts! The word was:", word)
