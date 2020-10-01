# Name - Jaylen Schelb
# Program - Poetry Slam

# Importing choice from random for the lines_printed_random() functionality
from random import choice

# Newline to make everything look cleaner
print("")

# Opening a file and returning its lines in a list
def get_file_lines(filename):
    infile = open(filename, "r")
    raw_data = infile.readlines()
    infile.close()
    
    final_data = [i.rstrip("\n") for i in raw_data]
    
    return final_data

data = get_file_lines("poem.txt")

# Printing the lines of the peom backwards
def lines_printed_backwards(lines_list):
    lines_list.reverse()

    # The variable no_count is so that the line numbers don't count empty lines (In conjuction with the following if statement)
    no_count = lines_list.count("")
    raw_line_num = len(lines_list)
    line_num = raw_line_num - no_count

    for i in lines_list: 
        if i == "":
            print(i)
        else:
            print(f"{line_num} {i}")
            line_num -= 1
        

# Printing the lines of the poem in random order
def lines_printed_random(lines_list):
    for i in lines_list:
        print(choice(lines_list))


# My custom poem function. Refer to the print statement on line x and y for an explanation of what it does
def lines_printed_custom(lines_list):
    for i in lines_list:
        # Splitting each line into a list of individual words
        i = i.split()
        # Getting the length of the list and then dividing it by 2. This will determine how many words will be in each half of
        # the line (floor division is used here because we do not want decimals)
        i_length = len(i)
        half_i_length = i_length // 2

        # Actually declaring what words will be in the first and second half of the list
        first_half_list = i[0:half_i_length]
        second_half_list = i[half_i_length:i_length]

        # Joining the list so each half is one big string instead of a list of words
        first_half = " ".join(first_half_list)
        second_half = " ".join(second_half_list)

        # Printing the second half of the line in front of the first half
        print(second_half + " " + first_half)

# Printing the lines of the peom in normal order
def lines_printed_normal(lines_list):
    for i in lines_list:
        print(i)

# Introduction message
print("Welcome to Poetry Slam! The poem that we will be working with today is called Monosyllabics by Laura E. Richards. \n\
There are a few things you can do with this peoem. Below are the options. Type the number corresponding to which \n\
version of the poem you would like to see printed below. Feel free to select any as many times as you would like. \n\
When you are done with this program, simply type 'stop'. Enjoy! :)")

restart = True

# Menu for the user to select what version of the poem they want to see printed to terminal. This is in a while loop, so it 
# will repeat until the user types 'stop' or 'Stop'
while restart:
    print("\n\
1. The poem will be printed normally \n\
2. The peom will be printed in reverse (line wise) \n\
3. The peom will be printed randomlly (line wise) \n\
4. The two halves of each line will be swapped in position \n\
   (Example: 'Hey how are you' will become 'are you? Hey how')")

    user_input = ""

    # This while statement is here to ensure the user only types in an integer between 1 and 4. If not, the program will keep
    # promting the user to enter a valid number or type 'stop' (with the help of the if statement below)
    while True:
        user_input = input()
        print("")
    
        if user_input == "1":
            lines_printed_normal(data)
            break
        elif user_input == "2":
            lines_printed_backwards(data)
            break
        elif user_input == "3":
            lines_printed_random(data)
            break
        elif user_input == "4":
            lines_printed_custom(data)
            break
        elif user_input == "stop" or user_input == "Stop":
            restart = False
            break
        else:
            print("You must enter an integer between 1 and 4! Try again.")
            