def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file = open(filename, 'r')
    return file
	
def count_dict(thing):
    k = 'zxcvbnmpoiuytrewqasdfghjkl'
    dict = {}
    for line in thing:
        lower = line.lower()
        for elem in lower:
            if elem in k:
                if elem in dict:
                    dict[elem] += 1
                else:
                    dict.update({elem : 1})
    return dict
	
def listify(dict1):
    final_list = []
    for letter, count in dict1.items():
        final_list.append([count, letter])
    final_list.sort()
    return final_list
	
def main():
    iter1 = open_file()
    final_dict = count_dict(iter1)
    print_list = listify(final_dict)
    for elem in print_list:
        print(elem)
	
main()