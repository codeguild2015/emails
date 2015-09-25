def main():
    """Takes a text file and returns """
    file = open_file()
    output1 = line_scan(file)
    output2 = counted_hours(output1)
        
def open_file():
    """Opens a text file"""
    filename = input("Input filename. > ")
    file = open(filename, 'r')
    return file
    
def line_scan(file):    
    hour_lst = []
    for line in file:
        if "From" in line:
            #print(line)
            if len(line.split()) > 2:
                split_line = line.split()
                b = split_line[5]
                hour_lst.append(b[:2])
            #print(split_line)
    return hour_lst

def counted_hours(hour_lst):
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
def line_scan_test():
    assert split_line == ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
    assert len(split_line) > 2 == True
    
#def counted_hour_test():
   # assert fin_count_hour(hour_lst) ==  

#print("Passed unit tests.")
