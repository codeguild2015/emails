def get_filename():
    """Arguments - none 
    returns - pointer to a file"""

    filename = input("Input filename:  ")
    file_pointer = open(filename, 'r')
    return file_pointer

def read_file(file_pointer):
    """inputs - file to read
    outputs - a list of lists containing all the from lines from the file"""
    
    lst2 = []

    for line in file_pointer:
        lst1 = line.split()
        # Don't get blank lines in the file.  This causes index out of range error.
        if lst1 == []:
            continue
        else:    
            #for words in lst1:
            if lst1[0] == "From":
                lst2.append(lst1[1:]) 
    #print("lst2 in read_file function is:  ", lst2)
    return lst2

def remove_unique_address(lst):
    '''inputs - list of lists from read_file()
    outputs - list of unique address'''

    addresses = []

    #print("lst in remove_unique_address is:  ", lst)
    #print("addresses[0] before entering for loop", addresses[0])
    # Remove everything but the address in the list of lists

def remove_unique_address1(lst):
    '''inputs - list of lists from read_file()
    outputs - list of unique address'''

    addresses = []
    # addresses.append('dummy')
    #print("lst in remove_unique_address is:  ", lst)
    #print("addresses[0] before entering for loop", addresses[0])
    # Remove everything but the address in the list of lists
    #print('length of lst before for is:  ', len(lst))
    #print('lenth of 0th list within lst bofore for is: ', len(lst[0] ))
    #for i in range(len(lst)):
    #for i in range(len(lst)):
        # #print("length of addresses in outer for:", len(addresses))
        # print("value of i in the outer for loop is: ", i)
        # #for x in range(len(addresses)):
    for x in range(len(lst)):
        if lst[x][0] in addresses:
            continue
        else:
                addresses.append(lst[x][0])
            #print("the value of x at inner for entry is: ", x)
            #print('the value of lst[i][0] is:  ', lst[i][0])
            #print('the value of address[x] is:  ', addresses[x])
            #print('addresses in inner for is: ', addresses)
            #if addresses[x] == 'dummy':
            #if not addresses: # empty list
             #   addresses[0] = (lst[i][0])
             #   print('At first if in inner for.  addresses[x] is: ', addresses[x])
             #   continue
            #elif addresses[x] == lst[i][0]: 
                # Do nothing for now.  good place to increment a counter.
             #   print("do nothing because addresses[x] {} and lst[i][0]{} are equal".format(addresses[x], lst[i][0]))
            #else:
            #    print("the value of i at else is:  ", i)
            #    #print("lst at else is: ", lst)
            #    print("The value of lst[i][0] is: ", lst[i][0])
            #    print("about to append addresses because current lst element isn't in addresses")
            #    addresses.append(lst[i][0]) 
            #    print("value of addresses[x] after the append is:", addresses[x])

    print("value of addresses is", addresses)
    print('')
            #print("value of lst is", lst)

                  

    #print("addresses in function after for loop: ", addresses)
    return addresses 


#Test files for assertions
file1 = 'one_good_line.txt'
file2 = 'two_good_line.txt'
file3 = 'two_good_one_bad.txt'
file4 = 'bogus_file.txt'
file_pointer = get_filename()
lst = read_file(file_pointer)
dodo = remove_unique_address1(lst)