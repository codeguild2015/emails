
def read_file(filename):
    '''inputs - file to readfile
    outputs - a list of lists containing all the from lines from the file'''
    file = open(filename, 'r')
    lst2 = []

    for line in file:
        lst1 = line.split()
        #for words in lst1:
        if lst1[0] == "From":
            lst2.append(lst1[1:]) 
    #remove_unique_address(lst2)
    #print("lst2 is:  ", lst2)
    count(lst2)

def remove_unique_address(lst):
    '''inputs - list of lists from read_file()
    outputs - list of unique address'''
    pass

def count(lst, unique):
    '''inputs - list of lists.  Each list contains address as first element
              - a list of unique names

    output - list of tuples with elements address, count'''

    '''
    txt = 'but soft what light in yonder window breaks'
    words = txt.split() # sets words to a list of each word from string txt
    print(words)
    t = list()  # instantiate and empty list.
    print("The value of list is: ", list)
    *** Making a list of tuples ***
    for word in words:
       t.append((len(word), word)) # - Gives us a tuple with the length of the word and the word.
    '''


    t = list() #list variable for storing a list of tuples
    for name in unique:
        count = 0 #re-init the counter to 0 for each element of the unique list
        for index, elem in enumerate(lst):
            #print("name in inner for is:", name)
            if name == elem[0]:
                count += 1
                #print("name is:  ", name)
                #print("count is:  ", count)

        t.append((name, count))
    return(t)


def sort_reverse(lst_of_tups):
    '''input list of tuples from count function
	output sorted list keying on the # of commits value'''
    #lst_of_tups.sort(reverse = True)
    print("lst_of_tups contains:  ", lst_of_tups)
    #print(sorted(lst_of_tups, key=lambda commits: commits[1]) )
    lst_of_tups( sorted(lst_of_tups, key=lambda commits: commits[1]) )
    lst_of_tups(:-1)  
#Test files for assertions
file1 = 'one_good_line.txt'
file2 = 'two_good_line.txt'
file3 = 'two_good_line.txt'
file4 = 'bogus_file.txt'

#read_file assertions
#assert read_file(file1) == [['stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']] 
#assert read_file(file2) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
#assert read_file(file3) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
#assert read_file(file4) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
#print("Assert tests passed")

#count assertions
# dummy lists to pass to count
unique = ['sally', 'jessie', 'raphael']
#lst = [['sally', '1', '2'], ['sally', '1', '2']]
lst = [['sally', '1', '2'], ['sally', '1', '2'], ['raphael', '1', '2']]
t = count(lst, unique)
#print("The returned value of t is:  ", t)
#lst = read_file(file4)
#lst = read_file(file) 
#lst2 = count(lst, unique_list)
#print("list in main is: ", lst)

#sort_reverse assertions

print( "the sorted list return value is:  ", sort_reverse(t) )



