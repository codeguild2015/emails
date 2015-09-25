# hour_Dana_Kevin.py
# Authors = Dana and Kevin
# Usage: import in python interpreter.

def main():
    """Takes a text file and returns the number of total commits per
    hour in the day."""
    file = open_file()
    output1 = line_scan(file)
    output2 = counted_hours(output1)
            
def open_file():
    """Opens a text file indicated by the user."""
    filename = input("Input filename. > ")
    file = open(filename, 'r')
    return file
    
def line_scan(file):
    """Inputs the text file and outputs a list of unsorted commit hours"""
    hour_lst = []
    for line in file:
        if "From" in line: # The From line contains the relevant email addresses
                           # and commit hours 
            #print(line)
            if len(line.split()) > 2: # We are only interested in lines
                                      # that contain more than two objects,
                                      # as they have the time stamps
                                      # associated with valid commits.
                
                split_line = line.split()
                b = split_line[5]
                hour_lst.append(b[:2])
            #print(split_line)
    print(hour_lst[0])
    return hour_lst

def counted_hours(hour_lst):
    """Inputs a list of commit hours, counts and sorts the list, and outputs 
    the final counts, sorted by hour of the day """
    fin_count_hour = [] 
    for item in hour_lst:
        commit_count = hour_lst.count(item)
        commit_time = item
        commit_tuple = commit_time, commit_count
        fin_count_hour.append(commit_tuple)
        fin_count_hour.sort()
    for item in range(len(fin_count_hour)): # Prints unique values by 
                                            # identifying unequal sequential 
                                            # values.
        if fin_count_hour[item] != fin_count_hour[item - 1]:
            hour, commit = fin_count_hour[item]
            print(hour, commit)
main()

"""Unit Tests"""
"""def line_scan_test():
    assert line == "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
    assert line_scan_test(split_line[0]) == ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
"""

#def line_scan_test(file):
#    assert file = 'mbox-short.txt'
#     assert line_scan_test(file) = 
    
#line_scan_test(file)
    
def counted_hour_test():
    assert line_scan(hour_lst[0]) == 5
counted_hour_test()

#print("Passed unit tests.")#
