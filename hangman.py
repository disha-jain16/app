import random  
  
def hangman():  
    words = ["python", "hangman", "programming", "developer", "keyboard"]  
    word = random.choice(words)  
    guessed = set()  
    attempts = 6  
  
    print("Welcome to Hangman!")  
      
    while attempts > 0:  
        display_word = "".join([letter if letter in guessed else "_" for letter in word])  
        print(f"Word: {display_word}")  
        print(f"Attempts left: {attempts}")  
  
        guess = input("Guess a letter: ").lower()  
          
        if guess in guessed:  
            print("You already guessed that letter.")  
        elif guess in word:  
            guessed.add(guess)  
            print("Correct guess!")  
        else:  
            guessed.add(guess)  
            attempts -= 1  
            print("Wrong guess!")  
  
        if set(word).issubset(guessed):  
            print(f"Congratulations! You guessed the word: {word}")  
            break  
    else:  
        print(f"Game over! The word was: {word}")  
  
hangman()  
