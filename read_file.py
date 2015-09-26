def read_file(filename):
    '''inputs - file to read
    outputs - a list of lists containing all the from lines from the file'''
    file = open(filename, 'r')
    lst2 = []

    for line in file:
        #print("value of line before split is:  ", line)
        lst1 = line.split()
        if lst1 == []:
            #print("got a blank line")
            continue
        else:    
            #for words in lst1:
            if lst1[0] == "From":
                lst2.append(lst1[1:]) 
                #print(lst2)
    #remove_unique_address(lst2)
    #print("lst2 is:  ", lst2)
    return lst2

    #Test files for assertions
file1 = 'one_good_line.txt'
file2 = 'two_good_line.txt'
file3 = 'two_good_one_bad.txt'
file4 = 'bogus_file.txt'
file5 = 'mbox-short.txt'
file6 = 'mbox-short1.txt'

''' read_file() assertions '''

print(read_file(file5))