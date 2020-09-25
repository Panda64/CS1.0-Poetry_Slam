# Name - Jaylen Schelb
# Program - Poetry Slam

def get_file_lines(filename):
    infile = open(filename, "r")
    data = infile.readlines()
    
    return data

def lines_printed_backwards(lines_list):
    lines_list.reverse()
    line_num = len(lines_list)

    for i in lines_list:
        print(f"{line_num} {i}")
        line_num -= 1
        
data = get_file_lines("poem.txt")
lines_printed_backwards(data)



