import random

animals = ["dog", "cat", "eel", "zebra", "giraffe",
 "jackal", "alligator", "raccoon", "orangutan", "elk",
 "monkey","boar", "hamster", "ocelot", "otter",
 "yak", "woodchuck", "sheep","cheetah", "platypus"]

instruments = ["guitar", "bass", "drumset", "piano", "theremin"
 "violin", "cello", "vibraslap", "bongo", "trumpet",
 "trombone", "tuba", "clarinet", "flute", "xylophone",
 "accordion", "saxophone", "tambourine", "triangle", "harp"]

food = ["spaghetti", "chocolate", "hazelnut", "pineapple", "hamburger", 
 "apple", "bagel", "pizza", "cheese", "cake",
 "banana", "cantaloupe", "watermelon", "salami", "chicken",
 "salsa", "taco", "vegemite", "horseradish", "pistachio"]

def mask_word(word):
    anon_word = '*' * len(word)
    return anon_word

def uncover_word(word,anon_word,guess):
    i = 0
    anon = list(anon_word)
    for x in word:
        if guess.lower() == x:
            anon[i] = guess
        i += 1
    return "".join(anon)

def getWord(wordList):
    word = random.randint(0, len(wordList) - 1)
    return wordList[word]

def chooseList(num):
    if num == "1":
        return animals
    if num == "2":
        return instruments
    if num == "3":
        return food

def chooseDifficulty(num):
    if num == "1":
        return 10
    if num == "2":
        return 6
    if num == "3":
        return 3

####################MAIN##################### 

difficulty = 10
word_guessed = False
game_over = False
guessed_letters = ''   
intro = input('Welcome to Hangman, would you like to play? (Press any button to continue or "q" to quit)\n')
if intro.lower() == "q":
    quit()

chooseWords = input('''Please choose your word list:
1 = Animals
2 = Instruments
3 = Food\n''')

answer = getWord(chooseList(chooseWords))

chooseDiff = input('''Please choose your difficulty:
1 = Easy (10 wrong letters)
2 = Normal (6 wrong letters)
3 = Hard (3 wrong letters)\n''')

difficulty = chooseDifficulty(chooseDiff)

maskedWord = mask_word(answer)
print('The hidden word will be printed below.  You have',difficulty,'wrong guesses available.\n' + 
maskedWord)

while game_over == False:
    while word_guessed == False:
        print('Guessed Letters: ' + guessed_letters)
        print('Remaining Guesses: ', difficulty)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in guessed_letters:
            print('You have already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a single LETTER.')
        else:
            wordPart = uncover_word(answer, maskedWord, guess)
            if wordPart == maskedWord:
                guessed_letters += guess
                difficulty -= 1
                print('That letter was incorrect! Try again.\n' + wordPart)
            else:
                guessed_letters += guess
                maskedWord = wordPart
                print('That letter was correct!\n' + wordPart)
                if wordPart == answer:
                    word_guessed = True
                    over = input('Would you like to play again? (q to quit)')
                    if over == 'q':
                        game_over = True




