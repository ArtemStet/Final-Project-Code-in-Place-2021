import random

WORDS = 'words.txt'

def main():
    """This is simple text version of the game Hangman. User needs to input difficulty
    and then try guess the word. The word is imported from the .txt file (could be any).
    Every time word is picked randomnly"""
    print("Welcome to the game Hangman!")
    print("You will need to guess a hidden word.\nIf you want to add new words, type 'add' in difficulty")
    answer = ""
    while answer != "n":
        lifes = difficulty()
        word_list = extract_words()
        random_word = pick_randowm_word(word_list)
        answer = hangman(lifes, random_word)
    print("Thanks for playing!\nHave a nice day!")

def difficulty():
    """Set the difficulty and allow to add new words in words.txt
    Input - diff; Output - return amount of attempts = lifes"""
    print("Choose your difficulty:")
    print("Easy - 15 attepmts\nMedium - 10 attempts\nHard - 5 attepmts")
    diff = input("Type your difficulty: ")
    while True:
        if diff == "easy" or diff =="Easy":
            lifes = 15
            break
        elif diff == "medium" or diff =="Medium":
            lifes = 10
            break
        elif diff == "hard" or diff == "Hard":
            lifes = 5
            break
        elif diff == "add":
            add_new_words()
            diff = input("Type your difficulty: ")
        else:
            print("Sorry invalid input!\nType again!")
            diff = input("Type your difficulty: ")
    print("You have", lifes, "attempts")
    return lifes

def extract_words():
    """Extract words from the .txt file. You can add more words in the .txt files"""
    f = open(WORDS)
    word_list = []
    for word in f:
        word = word.strip("\n")
        word_list.append(word)
    f.close()
    return word_list

def pick_randowm_word(word_list):
    """Generate random number from the range 0 to length of list of words - 1 and assign
    this number as index to the list and then return this word from the list"""
    random_num = random.randint(0, (len(word_list)-1))
    return word_list[random_num]

def hangman(lifes, random_word):
    """The main game process.
    It has two empty lists, where correct and wrong asnwers are appending.
    "while" loop is checking and controlling how many lifes/attempts are left.
    There is also check function that assemble letters into the string
    to compare if it is equal to random_word. If they are equal,
    "while" loop is breaked and it is the end of the game."""
    check = ""
    wrong_answers = []
    guess_word = []
    for i in range(len(random_word)):
        guess_word.append("_")
    print("\nThe word has", len(random_word), "letters.")
    print("The guess word is ", *guess_word, sep = "")
    letter = input("Type letter: ")
    print("")
    while lifes > 0:
        if letter in random_word:
            print("The letter", letter, "is in the word.")
            indices = assign_indices(random_word, letter)
            for index in indices:
                guess_word[index] = letter
            check = checking_guess_word(guess_word)
            if check == random_word:
                break
            print("The guess word is ",*guess_word, sep = "")
            print("Wrong letters:", *wrong_answers, sep =" ")
            letter = input("Type letter: ")
            print("")
        else:
            print("The letter", letter, "is not in the word.")
            wrong_answers.append(letter)
            lifes -= 1
            print("The guess word is ",*guess_word, sep = "")
            print("Wrong letters:", *wrong_answers, sep = " ")
            letter = input("Type letter: ")
            print("")
    if check == random_word:
        print("\nCongratulations!\nYou won!\nThe word was", random_word)
        answer = play_again()
        return answer
    else:
        print("You were close!\nThe word was", random_word)
        answer = play_again()
        return answer

def assign_indices(random_word, letter):
    """This function allows to collect indices of the letter that appears
    more than once in the word"""
    indices = []
    for i in range(len(random_word)):
        if random_word[i] == letter:
            indices.append(i)
    return indices

def checking_guess_word(guess_word):
    """Make quess_word one sting line to check if random_word == str(guess_word)"""
    check = ""
    for element in guess_word:
        check += element
    return check

def add_new_words():
    """If diff = "add", allow to add new words in words.txt"""
    print("Type the words you want to add.\nType 'q' to quit")
    word = input("Type the word: ")
    with open(WORDS, 'a+') as f:
        while word != 'q':
            f.write(word+"\n")
            word = input("Type the word: ")
    f.close()

def play_again():
    """Function to return answer to start new game or to stop"""
    print("")
    print("Do you want to play again?")
    answer = input("Type 'y' for yes and 'n' for no: ")
    return answer

if __name__ == '__main__':
    main()
