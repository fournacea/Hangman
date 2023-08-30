import random


word_list = ["aardvark", "baboon", "camel", "dingo", "elephant", "fox",]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#testing
print(chosen_word)

#Create empty list
display = []

#Set variable to length of chosen word
word_length = len(chosen_word)

#Set blanks in list to number of letters in randomly chosen word
for letter in chosen_word:
    display += "_"

print(display)

#End of game flag
end_of_game = False

#Loop through until user guesses all letters in randomly chosen word
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    # Check for guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == user_guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True

print("You won!")
