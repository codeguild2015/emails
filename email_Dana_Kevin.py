# hour_Dana_Kevin.py
# Authors = Dana and Kevin
# Usage: import in python interpreter.
def main():
    """Takes a text file and returns the email address of the person
    with the total number of commits.
    """
    file = open_file()
    output1 = line_scan(file)
    output2 = counted_emails(output1)
    file.close()
    
def open_file():
    """Opens a text file indicated by the user."""
    filename = input("Input filename. > ")
    file = open(filename, 'r')
    print("Opened " + filename )
    return file
    
def line_scan(file):
    """Inputs the text file and outputs a list of email addresses"""
    line_lst = []
    for line in file:
        if "From" in line: # The From line contains the relevant email addresses
                           # and commit hours. 
            if len(line.split()) > 2: # We are only interested in lines
                                      # that contain more than two objects,
                                      # as they have the time stamps
                                      # associated with valid commits.
                a = line.split()
                line_lst.append(a[1])
    return line_lst 
    
def counted_emails(line_lst): 
    """Inputs a list of email addresses, counts and sorts the list, and outputs 
    the final counts, sorted by the greatest number of commits. 
    """
    tot_emails = []
    for item in line_lst:
        email = item
        commit = line_lst.count(item)
        num = commit, email
        tot_emails.append(num)
    tot_emails.sort(reverse=True)
        
    print(tot_emails[0])
       

"""Unit Tests
def line_scan_test():
    assert line_scan("From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008") == ['stephen.marquard@uct.ac.za']

def counted_emails_test("")
"""   
main()
#line_scan_test()
