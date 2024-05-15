import os

# ASCII art for Hangman
HANGMAN_ASCII_ART = """
Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/"""

# ASCII art for winning
WON_ASCII = r"""
 __     ______  _    _  __          ______  _   _ 
 \ \   / / __ \| |  | | \ \        / / __ \| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` |
    | | | |__| | |__| |    \  /\  / | |__| | |\  |
    |_|  \____/ \____/      \/  \/   \____/|_| \_|
"""

# ASCII art for loosing
LOST_ASCII = r"""
 __     ______  _    _   _      ____   _____ _______ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|__   __|
  \ \_/ / |  | | |  | | | |   | |  | | (___    | |   
   \   /| |  | | |  | | | |   | |  | |\___ \   | |   
    | | | |__| | |__| | | |___| |__| |____) |  | |   
    |_|  \____/ \____/  |______\____/|_____/   |_|   
"""

# Maximum tries allowed
MAX_TRIES = 6

# photos of the hangman
# added tabs so the first picture will be in line with other pictures
HANGMAN_PHOTOS = {1: "                      x-------x",

                  2:
                      """
                      x-------x
                      |
                      |
                      |
                      |
                      |""",

                  3:
                      """
                      x-------x
                      |       |
                      |       0
                      |
                      |
                      |""",

                  4:
                      """
                      x-------x
                      |       |
                      |       0
                      |       |
                      |
                      |""",

                  5:
                      """
                      x-------x
                      |       |
                      |       0
                      |      /|\\
                      |
                      |""",

                  6:
                      """
                      x-------x
                      |       |
                      |       0
                      |      /|\\
                      |      /
                      |
                  """,
                  7:
                      """
                      x-------x
                      |       |
                      |       0
                      |      /|\\
                      |      / \\
                      |"""
                  }


def print_start_game():
    """Print the starting game message and the maximum number of tries allowed"""
    print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the letter guessed is valid and not already guessed.
    Param: letter_guessed - the letter that the user guessed
    Param: old_letters_guessed - the letters that the user already guessed
    Return: True if the input is valid (a single letter, alphabetic, and not guessed before); False otherwise
    """
    # check if the letter is in the list of guessed letters
    is_letter_in_array = letter_guessed in old_letters_guessed
    # check if the letter is not a single letter or not alphabetic or already guessed
    if (len(letter_guessed) != 1) or (not letter_guessed.isalpha() or is_letter_in_array):
        return False
    return True



def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Attempts to update the list of guessed letters with the new guess.
    Param: letter_guessed - The letter that the user guessed
    Param: old_letters_guessed - The list of letters that have already been guessed
    Return: True if the letter was successfully added, False otherwise
    """
    
    # Check if letter is valid and not already guessed
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    # Print 'X' and the sorted list of guessed letters with '->' between them
    print('X')
    # sort the list of guessed letters
    old_letters_guessed.sort()
    # join the list of guessed letters with '->' between them
    sort_with_arrows = ' -> '.join(old_letters_guessed)
    print(sort_with_arrows)
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Displays the secret word with guessed letters revealed and underscores for unguessed letters.
    Param: secret_word - The word the player is trying to guess
    Param: old_letters_guessed - The list of letters that have already been guessed
    Return: A string representing the partially guessed word
    """
    displayed_word = ""
    # for each letter in the secret word
    for letter in secret_word:
        # if the letter is in the list of guessed letters
        if letter in old_letters_guessed:
            # add the letter to the displayed word
            displayed_word += letter + ' '
        else:
            # add an underscore to the displayed word
            displayed_word += '_ '
    return displayed_word


def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has successfully guessed all letters in the secret word.
    Param: secret_word - The word the player is trying to guess
    Param: old_letters_guessed - The list of letters that have already been guessed
    Return: True if the player has won (all letters guessed), False otherwise
    """
    displayed_word = show_hidden_word(secret_word, old_letters_guessed)
    if '_' in displayed_word: # if there are still hidden letters
        return False
    return True


def print_hangman(num_of_tries):
    """
    Prints the current stage of the hangman drawing based on the number of incorrect tries.
    Param: num_of_tries - The current number of incorrect guesses
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """
    Selects a word from a file at a given index, wrapping around if the index exceeds the file length.
    Param: file_path - Path to the file containing possible secret words
    Param: index - The index to pick the word from
    Return: The chosen word from the file
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
    # return the word in the index
    return words[(index - 1) % len(words)]


def hangman():
    """Main function to start and manage the game of Hangman."""
    # print the starting game message and art
    print_start_game()
    # get the path of the file with the words
    path = input("Please enter the path of the file: ")

    does_exists = os.path.exists(path)  # check if the file exists
    # if the file does not exist
    while not does_exists:
        print("The file does not exist")
        # get the path of the file with the words
        path = input("Please enter the path of the file: ")
        does_exists = os.path.exists(path)

    # get the index of the word to guess
    index = input("Please enter a random number: ")
    # get the word from the file in the index
    secret_word = choose_word(path, int(index))

    # Initialize the list of guessed letters
    old_letters_guessed = []

    print_hangman(1)  # print the starting point of the hangman

    num_of_tries = 0  # initialize loop counter to 0

    # Print the hidden word with '_' and the letters already guessed
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < MAX_TRIES: # loop until player wins or loses

        # get the letter guessed and put in lower case (if not letter won't do anything)
        letter_guessed = input("Guess a letter: ")
        print(letter_guessed)  # print the input

        os.system("cls") # clear terminal

        # update letter guessed and check if valid and already guessed
        check_valid = try_update_letter_guessed(letter_guessed.lower(), old_letters_guessed)

        #  if input not valid or already guessed go to next iteration
        if not check_valid:
            # continue to the next iteration
            continue

        #  if letter not in the word to guess
        if letter_guessed not in secret_word:
            print("):")
            # add one to loop counter (adds one to disqualification)
            num_of_tries += 1
            print_hangman(num_of_tries + 1)
        
        # Print the hidden word with '_' and the letters already guessed
        print(show_hidden_word(secret_word, old_letters_guessed))

        # checks if player won and if did end the loop
        if check_win(secret_word, old_letters_guessed):
            print(WON_ASCII)
            # end the loop
            break

    # if player lost
    if num_of_tries == MAX_TRIES:
        print(LOST_ASCII)
        print(f"The word was: {secret_word}")


# Main function to start the game
def main():
    hangman()


# Entry point of the program
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
