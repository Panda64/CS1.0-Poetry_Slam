# Name - Jaylen Schelb
# Program - Poetry Slam

from random import choice

def get_file_lines(filename):
    infile = open(filename, "r")
    data = infile.readlines()
    
    return data

data = get_file_lines("poem.txt")


def lines_printed_backwards(lines_list):
    lines_list.reverse()
    line_num = len(lines_list)

    for i in lines_list:
        print(f"{line_num} {i}")
        line_num -= 1
        
# lines_printed_backwards(data)

def lines_printed_random(lines_list):
    for i in lines_list:
        print(choice(lines_list))

# lines_printed_random(data)

def lines_printed_custom(lines_list):
    # Code goes here....