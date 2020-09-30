# Name - Jaylen Schelb
# Program - Poetry Slam

from random import choice

print("")

def get_file_lines(filename):
    infile = open(filename, "r")
    raw_data = infile.readlines()
    
    final_data = [i.rstrip("\n") for i in raw_data]
    
    return final_data

data = get_file_lines("poem.txt")


def lines_printed_backwards(lines_list):
    lines_list.reverse()

    no_count = lines_list.count("")
    raw_line_num = len(lines_list)
    line_num = raw_line_num - no_count

    for i in lines_list: 
        if i == "":
            print(i)
        else:
            print(f"{line_num} {i}")
            line_num -= 1
        

def lines_printed_random(lines_list):
    for i in lines_list:
        print(choice(lines_list))


def lines_printed_custom(lines_list):
    for i in lines_list:
        i = i.split()
        i_length = len(i)
        half_i_length = i_length // 2

        first_half_list = i[0:half_i_length]
        second_half_list = i[half_i_length:i_length]

        first_half = " ".join(first_half_list)
        second_half = " ".join(second_half_list)

        print(second_half + " " + first_half)

def lines_printed_normal(lines_list):
    for i in lines_list:
        print(i)

print("Welcome to Poetry Slam! The poem that we will be working with today is called Monosyllabics by Laura E. Richards. \n\
There are a few things you can do with this peoem. Below are the options. Type the number corresponding to which \n\
version of the poem you would like to see printed below. Feel free to select any as many times as you would like. \n\
When you are done with this program, simply type 'stop'. Enjoy! :)")

restart = True

while restart:
    print("\n\
1. The poem will be printed normally \n\
2. The peom will be printed in reverse (line wise) \n\
3. The peom will be printed randomlly (line wise) \n\
4. The two halves of each line will be swapped in position \n\
   (Example: 'Hey how are you' will become 'are you? Hey how')")

    user_input = 0

    while True:
        user_input = input()
    
        if user_input == "1":
            lines_printed_normal(data)
            break
        elif user_input == "1":
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
            