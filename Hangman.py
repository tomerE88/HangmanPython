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


# Function to check if the guessed letter is valid
def is_valid_input(letter_guessed):
    # if it's not one letter in english will return false
    if (len(letter_guessed) != 1) or (not letter_guessed.isalpha()):
        return False
    return True


# Function to try updating the guessed letter
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # Check if letter is already guessed
    is_letter_in_array = letter_guessed in old_letters_guessed
    # Check if letter is valid and not already guessed
    if is_valid_input(letter_guessed) and (not is_letter_in_array):
        old_letters_guessed.append(letter_guessed)
        return True

    # Print 'X' and the sorted list of guessed letters with '->' between them
    print('X')
    old_letters_guessed.sort()
    sort_with_arrows = ' -> '.join(old_letters_guessed)
    print(sort_with_arrows)
    return False


# Function to show the hidden word with guessed letters revealed
def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word


# check if plater won (guessed all characters of the word to guess)
def check_win(secret_word, old_letters_guessed):
    displayed_word = show_hidden_word(secret_word, old_letters_guessed)
    if '_' in displayed_word:
        return False
    return True


# print the current hangman photo
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


# Main game function
def hangman():
    print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)
    secret_word = input("Please enter a word: ")

    # Initialize the list of guessed letters
    old_letters_guessed = []

    print_hangman(1)  # print the starting point of the hangman

    i = 0  # initialize loop counter to 0

    while i < MAX_TRIES:
        # Print the hidden word with '_' and the letters already guessed
        print(show_hidden_word(secret_word, old_letters_guessed))
        # get the letter guessed and put in lower case (if not letter won't do anything)
        letter_guessed = input("Guess a letter: ")
        print(letter_guessed)  # print the input
        # update letter guessed and check if valid and already guessed
        check_valid = try_update_letter_guessed(letter_guessed.lower(), old_letters_guessed)
        #  if input not valid or already guessed letter
        if not check_valid:
            continue
        #  if letter not in the word to guess
        if letter_guessed not in secret_word:
            # add one to loop counter (adds one to disqualification)
            i += 1
            print_hangman(i + 1)

        # checks if player won and if did end the loop
        if check_win(secret_word, old_letters_guessed):
            print(WON_ASCII)
            break

    if i == MAX_TRIES:
        print(LOST_ASCII)


# Main function to start the game
def main():
    hangman()


# Entry point of the program
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
