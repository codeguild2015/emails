# Author:  Ransom V and Skip A
# Written 9/25/15
# References: Google, StackOverFlow
# Program to read in an email file and output the user with the most number of commits
# Program does not include commits per hour.


def get_filename():
    """
    Arguments - none 
    returns - pointer to a file
    """

    filename = input("Input filename:  ")
    f = open(filename, 'r')
    return f

def read_file(file_pointer):
    """
    Arguments - Address of a file to read
    Returns - a list of lists containing all the from lines from the file
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
    """
    Arguments - list of lists from read_file()
    Returns - list of unique address
    """

    addresses = []
    for x in range(len(lst)):
        if lst[x][0] in addresses:
            continue
        else:
            addresses.append(lst[x][0])

    return addresses 

def count_(lst, unique):
    """
    Arguments - 
    - list of lists.  Each list contains address as first element
    - list of unique names

    Returns - list of tuples with elements count and email address
    """

    commits_user = list() #list variable for storing a list of tuples
 
    for name in unique:
        count = 0 #re-init the counter to 0 for each element of the unique list
        for index, elem in enumerate(lst):
            if name == elem[0]:
                count += 1
        commits_user.append((count, name))
    return(commits_user)

def sort_reverse(lst_of_tups):
    """
    Arguments - list of tuples from count function
    
    Returns - sorted list  of tuples keying on the # of commits value
    list sorted from most to least commits 
    """

    reversed_tups = sorted(lst_of_tups, reverse=True)
    return reversed_tups

# End of non-main functions  
 
def main():
    # get_filename() assertions will go here
    f = get_filename()

    # read_file() 
    # Test files for assertions will go here
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
    raw_commits = read_file(f)

    # remove_unique_address() assertions will go here
    unique_list = remove_unique_address(raw_commits)
    #lst = [['sally', '1', '2'], ['sally', '1', '2'], ['raphael', '1', '2']]
    
    # commits_per_user assertions will go here
    commits_per_user = count_(raw_commits, unique_list)

    # sort_reverse() assertions will go here
    reversed = sort_reverse(commits_per_user)   
    print("Most commits is: {} - {} ".format(reversed[0][0], reversed[0][1]) )

main()

