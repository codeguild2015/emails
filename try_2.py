

def read_file(filename):
    '''inputs - file to readfile
    outputs - a list of lists containing all the from lines from the file'''
    file = open(filename, 'r')
    for line in file:
        lst1 = line.split()
        for words in lst1:
            if lst1[0] == "From":
                print(lst1)
				
	## put code here
	#"print(line)
	
#def count_user_commits:

#read_file('mbox-short.txt')

def remove_unique_address(lst):
    '''inputs - list of lists from read_file()
    outputs - list of unique address'''
	emails = lst[1]
	for words in lst1():
		lst2 = sort.words
    print(lst2)
    pass
def count(lst, unique_list):
    '''raw lst of names and unique list of names
    output - list of tuples with elements address, count'''
    pass

def sort_reverse(lst_of_tups):
    '''input list of tuples from count function
    output reverse sorted list from users with most to least commits'''
    pass

   
#file = 'mbox-short.txt'
#lst = readfile(file)
read_file('mbox-short.txt')



