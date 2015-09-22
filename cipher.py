def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file = open(filename, 'r')
    return file
	
def count_dict(thing):
    k = 'zxcvbnmpoiuytrewqasdfghjkl'
    dict = {}
    #thing.lower()
    for elem in thing:
        if elem in k:
            if elem in dict:
                dict[elem] += 1
            else:
                dict.update({elem:1})
    return dict
	
def listify(dict):
    final_list = []
    for letter, count in dict:
        final_list.append([letter, count])
    final_list.sort()
    return final_list
	
def main():
    file = open_file()
    final_dict = count_dict(file)
    print(final_dict)
    print_list = listify(final_dict)
    for elem in print_list:
        print(elem)
	
main()