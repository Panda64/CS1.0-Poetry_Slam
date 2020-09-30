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
        
# lines_printed_backwards(data)

def lines_printed_random(lines_list):
    for i in lines_list:
        print(choice(lines_list))

# lines_printed_random(data)

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

lines_printed_custom(data)

