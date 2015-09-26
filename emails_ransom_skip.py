def get_filename():
    """Arguments - none 
    returns - pointer to a file
    """

    filename = input("Input filename:  ")
    file_pointer = open(filename, 'r')
    return file_pointer

def read_file(file_pointer):
    """inputs - file to read
    outputs - a list of lists containing all the from lines from the file
    """
    
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
    # print("lst2 in read_file function is:  ", lst2)
    return lst2


def remove_unique_address(lst):
    """inputs - list of lists from read_file()
    outputs - list of unique address
    """
    # addresses = []
    # #print("lst in remove_unique_address is:  ", lst)

    # # Remove everything but the address in the list of lists
    # addresses = []
    # for x in range(0, len(lst)):
    #     #print("value of x is:  ", i)
    #     #print(lst[i][0])
    #     addresses.append  (lst[i][0])
    #     for i in range(0, len(addresses)):
    #         if addresses[i] == lst[x]:
    #             continue
    #         else:
    #             addresses[i] == lst[x]
    #     #addresses += (lst[0][i])
    # print("addresses: ", addresses)
    # print("addresses type: ", type(addresses))
    
    # #print("addresses: ", addresses)
    addresses = []
    for x in range(len(lst)):
        if lst[x][0] in addresses:
            continue
        else:
            addresses.append(lst[x][0])

    return addresses 

def count_(lst, unique):
    """inputs - list of lists.  Each list contains address as first element
              - a list of unique names

    output - list of tuples with elements address, count
    """

    commits_user = list() #list variable for storing a list of tuples
    print("Value of lst before for is: ", lst)
    for name in unique:
        count = 0 #re-init the counter to 0 for each element of the unique list
        for index, elem in enumerate(lst):
            print("name in inner for is: ", name)
            print("elem is ", elem)
            print("index is ", index)
            print("elem[0] is ", elem[0])
            if name == elem[0]:
                count += 1

        commits_user.append((count, name))
    return(commits_user)



def sort_reverse(lst_of_tups):
    """input list of tuples from count function
    output sorted list keying on the # of commits value 
    """
    #lst_of_tups.sort(reverse = True)
    #print("lst_of_tups contains:  ", lst_of_tups)
    reversed_tups = sorted(lst_of_tups,key=lambda x:(-x[1],x[0]))
    #print("reverse sorted list is: ", reversed_tups )
    return reversed_tups

# End of functions  
 
def main():
        #Test files for assertions

    file_pointer = get_filename()
    #print("file pointer is: ", file_pointer)



    # Test files for assertions
    file1 = 'one_good_line.txt'
    file2 = 'two_good_line.txt'
    file3 = 'two_good_one_bad.txt'
    file4 = 'bogus_file.txt'
    file5 = 'mbox-short.txt'
    file6 = 'mbox-short1.txt'
    file7 = 'mbox.txt'
    #assert read_file(file1) == [['stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']] 
    #assert read_file(file2) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
    #assert read_file(file3) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
    #assert read_file(file4) == [['fist_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008'], ['second_list.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
    #print("Assert tests passed")
    #print(read_file(file3))
    raw_commits = read_file(file_pointer)
    #print("Raw commits after running read_file on mbox-short.txt is:  ", raw_commits)


    # remove_unique_address() assertions will go here
    unique_list = remove_unique_address(raw_commits)
    print("Unique addresses after calling remove_unique_addresses are:  ", unique_list)


    # count_() assertions will go here
    # dummy lists to pass to count
    #unique = ['sally', 'jessie', 'raphael']
    #lst = [['sally', '1', '2'], ['sally', '1', '2'], ['raphael', '1', '2']]
    t = count_(raw_commits, unique_list)
    print("The returned value of t is:  ", t)
    #lst = read_file(file4)
    #lst = read_file(file) 
    #lst2 = count(lst, unique_list)
    #print("list in main is: ", lst)
    #result = count_(raw_commits, unique_list)
    #print("result after calling count_", result)


    # sort_reverse() assertions will go here
    #print( "the sorted list return value is:  ", sort_reverse(t) )
    #reversed = sort_reverse(result)
    #print(reversed)

main()

