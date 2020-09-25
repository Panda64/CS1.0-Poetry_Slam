# Name - Jaylen Schelb
# Program - Poetry Slam

def get_file_lines(filename):
    infile = open(filename, "r")
    data = infile.readlines()
    
    return data

test = get_file_lines('poem.txt')
print(test)
