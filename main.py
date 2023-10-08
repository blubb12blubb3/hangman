import random
import requests

#get Word List
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

word = random.choice(WORDS)
word = str(word)
word = word[1:]
word = word.replace("'", "")

#Initialise game
solvedWord = word

#solvedWord = Hangman
#capsSolution = ['H', 'a', 'n', 'g', 'm', 'a', 'n']
capsSolution = solvedWord
capsSolution = list(capsSolution)

#solution = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
solution = solvedWord
solution = solution.lower()
solution = list(solution)

#guessLine = ['_', '_', '_', '_', '_', '_', '_']
length = len(solution)
guessLine = []
while length > 0:
    guessLine.append("_")
    length = length - 1

#init var
allGuesses = []
wrongGuesses = []
mistakes = 0
gameActive = True

def printCleanList(arr):
    arr = str(arr)
    arr = arr.replace("'", "").replace(",", "")
    #arr = arr.replace("[", "").replace("]", "")
    print(arr)
def printHangman(miss):
    match miss:
        case 0:
            print(" ---------------- ")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print(" ---------------- ")
        case 1:
            print(" ---------------- ")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|                |")
            print("|   _____        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 2:
            print(" ---------------- ")
            print("|                |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 3:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 4:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/         |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 5:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |          |")
            print("|     |          |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 6:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |          |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 7:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |      |   |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 8:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |     /|   |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 9:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |     /|\x5c  |")
            print("|     |          |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 10:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |     /|\x5c  |")
            print("|     |     /    |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
        case 11:
            print(" ---------------- ")
            print("|     ________   |")
            print("|     |/     |   |")
            print("|     |      O   |")
            print("|     |     /|\x5c  |")
            print("|     |     / \x5c  |")
            print("|   __|__        |")
            print("| /       \x5c      |")
            print(" ---------------- ")
def updateGuessLine(miss):
    if activeGuess in allGuesses:
        print()
        print()
        print("____________________________________")
        print("You already guessed that. Try again.")
    elif activeGuess in solution:
        print()
        print()
        print("____________________________________")
        print("That was a good guess :)")
        for i in range(0, len(solution)):
            if solution[i] == activeGuess:
                guessLine[i] = capsSolution[i]
    else:
        if activeGuess not in wrongGuesses:
            print()
            print()
            print("____________________________________")
            print("That was a wrong guess :(")
            miss = miss + 1
            wrongGuesses.append(activeGuess)
        else:
            print()
            print()
            print("____________________________________")
            print("You already guessed that. Try again.")
    allGuesses.append(activeGuess)
    allGuesses.append(activeGuess.upper())
    return miss
def enterGuess():
    aG = input("Enter your guess: ")
    if len(aG) != 1:
        aG = input("Please only enter one character: ")
    aG = aG.lower()
    print()
    print()
    return aG
def checkWin():
    if guessLine == capsSolution:
        printCleanList(guessLine)
        print("  --------------------------------  ")
        print("/                                  \x5c")
        print(f" You won! The solution was {solvedWord}!")
        print("\x5c                                  /")
        print("  --------------------------------- ")
        return False
    elif mistakes >= 11:
        printHangman(mistakes)
        printCleanList(guessLine)
        print("  --------------------------------  ")
        print("/                                  \x5c")
        print(f"You lost :( The solution was {solvedWord}!")
        print("\x5c                                  /")
        print("  --------------------------------  ")
        return False
    else:
        return True

#design
print("____________________________________")
print()

#GAME LOOP
while gameActive:
    cleanWrongGuesses = str(wrongGuesses).replace("[", "").replace("]", "")
    cleanWrongGuesses = cleanWrongGuesses.replace("'", "")
    print(f"Wrong guesses: {cleanWrongGuesses}")
    printHangman(mistakes)
    print("Progress: ")
    printCleanList(guessLine)
    activeGuess = enterGuess()
    mistakes = updateGuessLine(mistakes)
    gameActive = checkWin()

"""
def printEmptyLines(amount):
    while amount > 0:
        print()
        amount = amount - 1
"""