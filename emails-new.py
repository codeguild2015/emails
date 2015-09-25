# Authored by Jaydn C and Connor M
# Written 9/24/15
# Program to read in a file, pull lines out based on string keyword
# converts lines into a dictionary to be sorted and returned as sorted list to print. 

def open_file():
    """ Opens file, returns contents
    Paramaters
    -----
    Input:
    
    
    Output:
    list 
    file turned into string and assigned to variable for input on other functions"""
    filename = input("Please input file name: ")
    file = open(filename, 'r')
    return file

def file_to_list(doc, split_word="From"):
    '''takes doc, adds line into a list based on specific key word search
    Parameters
    ---------
    Input:
    doc: file
    split_word: string
    
    Output:
    lst: list
    list of lines extracted from doc'''
    
    lst = []
    for line in doc:
        line_temp = line.replace("  ", " ").split(" ")
        if line_temp[0] == split_word:
            lst.append(line_temp)
    return lst
    
def dict_times(lst):
    ''' takes lst, creates dict, updates indexed items to dict, otherwise, creates item in dict. 
    Parameters
    ----------
    Input:
    lst: list
    
    Output:
    times: dictionary'''

    times = {} 
    for item in lst:
        if item[5][:2] in times:
            times[item[5][:2]] += 1
        else:
            times.update({item[5][:2] : 1})
    return times

def dict_names(lst):
    ''' takes lst, creates dict, updates indexed items to dict, otherwise, creates item in dict. 
    Parameters
    ----------
    Input:
    lst: list
    
    Output:
    times: dictionary'''
    
    emails = {}
    for item in lst:
        if item[1] in emails:
            emails[item[1]] +=1
        else:
            emails.update({item[1]: 1})
    return emails   
    
def combine_emails(names):
    """ Takes dictonary in, converts item pairs in dict to a list
    Parameters
    ----------
    Input:
    dict1: dictionary
    
    Output:
    lst: list
    sorted list """
    
    lst = [] 
    for name, count in names.items():
        lst.append([count, name])
    lst.sort(reverse = True)
    return lst
    
def combine_times(times):
    """ Takes dictonary in, converts item pairs in dict to a list
    Parameters
    ----------
    Input:
    dict1: dictionary
    
    Output:
    lst: list
    sorted list """
    
    lst = []
    for name, count in times.items():
        lst.append([name , count])
    lst.sort()
    return lst

def file_to_list_test():
    assert file_to_list(['From in my test string']) == [['From', 'in', 'my', 'test', 'string']]
    assert file_to_list(['in my test string']) == []

def dict_names_and_times_test():
    a = [['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
    b = [['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']]
    c = a + a + b
    assert dict_times(a) == {'09': 1}
    assert dict_times(c) == {'09': 2, '18': 1}
    assert dict_times([]) == {}
    assert dict_names(a) == {'stephen.marquard@uct.ac.za': 1}
    assert dict_names(c) == {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 1}
    assert dict_names([]) == {}

def combine_emails_test():
    assert combine_emails({'stephen.marquard@uct.ac.za': 1}) == [[1, 'stephen.marquard@uct.ac.za']]
    assert combine_emails({'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 1}) == [[2, 'stephen.marquard@uct.ac.za'], 
            [1, 'louis@media.berkeley.edu']]
    assert combine_emails({}) == []

def combine_times_test():
    
    
def test():
    file_to_list_test()
    dict_names_and_times_test()
    combine_emails_test()
    combine_times_test()

def main():
    """ Calls each funtion in order, assigns input variables for each subsequent function
    Parameters
    ----------
    Inputs:
    
    Outputs:
    doc: string
    lst: list
    times: dict
    names: dict
    final_email: list
    final_times: list"""
    doc = open_file()
    lst = file_to_list(doc)
    times = dict_times(lst)
    names = dict_names(lst)
    final_email = combine_emails(names)
    final_times = combine_times(times)
    print(final_email[0])
    print() 
    for item in final_times:
        print("Hour:", item[0], "Commits:", item[1])
    test()

main()

