"""
Name: (Gabbie Chinnis)
Peers: (N/A)
References: (Notes/Lecture)
"""

def get_letter():
    """ Ask the user for a single uppercase letter A, B, or C. """
    while True:
        letter = input("Give a single uppercase letter: ")

        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue

        if letter not in ["A", "B", "C"]:
            print("Error: You provided the wrong character.")
            continue

        return letter

def get_digit():
     """ Ask the user for a single digit between 1 and 3. """
     while True:
        digit = input("Give an single number character: ")

        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue

        if digit not in ["1", "2", "3"]:
            print("Error: a single digit needs to be in [1,3].")
            continue

        return digit


def check_pattern(letter, digit, lst):
    """ Print words containing the letter followed by the digit. """
    
    print("Strings with the pattern: ")

    for word in lst:
        letter_position = word.find(letter)

        if letter_position != -1:
            if digit in word[letter_position + 1:]:
                print(word, end=" ")

    print()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    while True:
        letter = get_letter()
        digit = get_digit()

        check_pattern(letter, digit, st_list)

        answer = input("Try Again? (y/n): ")

        if answer != "y":
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
