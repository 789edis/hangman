import random

word_bank= ['blaze', 'crane', 'mirth', 'plumb', 'slick','frost','tango','quirk','bound','haven']  #should feel free to add more words
word = random.choice(word_bank)  #chooses a random word from the word bank

guessedWord = ["_"] * len(word) 
attempts = 10
guessed_letters = []

print("Guess the word!") 

while attempts > 0:  
    print("\nWord: " + " ".join(guessedWord))  #unrelated bu hehe it says nword
    print(f"Remaining errors: {attempts}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1: #if wgong input
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:  #if letter was already guessed
        print(f"You already guessed this letter: {guess}")
        continue

    guessed_letters.append(guess)

    if guess in word:  #if correct guess
        print("Correct guess!")
        
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
    
    else:  #if wrong guess
        attempts -= 1
        print(f"Wrong guess! You have {attempts} left.")
        
    
    if "_" not in guessedWord:  #if end 
        print(f"Congratulations! You found the word: {word}")
        break

