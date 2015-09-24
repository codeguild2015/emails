def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file = open(filename, 'r')
    return file
	
def count_dict(thing):
    """Loops through all the characters in the file, 
    checks if a character is in the alphabet (and lowercase), 
    then its frequency is counted and added to a dictionary"""
    k = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    for line in thing:
        lower = line.lower()
        for elem in lower:
            if elem in k:
                if elem in dict:
                    dict[elem] += 1
                else:
                    dict.update({elem:1})
    return dict
	
def listify(dict):
    """Loops through the dictionary of characters and their 
    counts and appends them as nested lists to a new list 
    e.g. {a:2}, {b:3} --> [[a,2],[b,3]]"""
    final_list = []
    for letter, count in dict.items():
        final_list.append([count, letter])
    final_list.sort()
    return final_list
	
def main():
	
    file = open_file()
    final_dict = count_dict(file)
    print_list = listify(final_dict)
    for elem in print_list:
        print(elem)
main()