import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string
    letters_guessed: list
    returns: boolean
    '''
    flag = True
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            flag = False
    return flag
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string
    letters_guessed: list
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = ["_ "]*len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word[i] = secret_word[i]
    return word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    x = string.ascii_lowercase
    q = ''
    for i in x:
        if i in letters_guessed:
            continue
        else:
            q += i
    return q

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, prints avalible words.

    '''
    x = []
    for ele in wordlist:
        Flag = True
        if len(ele) == len(my_word):
            for i in range(len(my_word)):
                if my_word[i] !=  '_':
                    if my_word[i] != ele[i]:
                        Flag = False
                        break
            if Flag:
                x.append(ele)
    for ele in x:
        print(ele,end=" ")
        print()
    return None

def hangman_with_hints(secret_word):
    guesses = 6
    warnings = 3
    hint = 1
    letters_guessed = []
    print(secret_word)
    while True:
        print(secret_word)
        print("Length of secret word is:",len(secret_word))
        print("guesses remaning:",guesses)
        if hint == 1:
            print("Type '*' to get all avalible words with matching guessed words!")
        print(get_guessed_word(secret_word, letters_guessed))
        print(get_available_letters(letters_guessed))
        while True:
            char_guessed = input("Enter a character: ")
            if char_guessed == "*":
                if hint == 1:
                    t = get_guessed_word(secret_word, letters_guessed)[:]
                    my_word = ''.join(t)
                    my_word = my_word.replace(" ",'')
                    show_possible_matches(my_word)
                    hint=0
                else:
                    guesses -=1
                    print("You have already used your abality! guesses remaning: ",guesses)
            elif char_guessed.isalpha() and char_guessed not in letters_guessed:
                break
            elif char_guessed in letters_guessed:
                if warnings==0:
                    guesses-=1
                    if guesses == 0:
                        break
                    print(print("Enter a new character!\n\nYou have",guesses,"remaning guesses"))
                else:
                    warnings-=1
                    print("Enter a new character!\n\nYou have",warnings,"remaning warnings")
            else:
                if char_guessed in "aeiou" and warnings>0:
                    warnings-=1
                elif warnings <= 0:
                    guesses-=1
                else:
                    if char_guessed in "aeiou":
                        guesses-=2
                    else:
                        guesses-=1
                    if guesses <= 0:
                        break
                print("Enter a character or a new character!\nYou have",warnings,"remaning warnings")
        letters_guessed += char_guessed
        if char_guessed not in secret_word:
            guesses-=1
            if guesses <= 0:
                    break
        print("---------------")
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations you Won!")
            break
        elif guesses<=0:
            print("You lost")
            break
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)