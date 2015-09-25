def main():
    file = open_file()
    output1 = line_scan(file)
    output2 = counted_emails(output1)
    file.close()
    
def open_file():
    filename = input("Input filename. > ")
    file = open(filename, 'r')
    print("Opened " + filename )
    return file
    
def line_scan(file):
    line_lst = []
    for line in file:
        if "From" in line:
            if len(line.split()) > 2:
                a = line.split()
                line_lst.append(a[1])
    return line_lst 
    
def counted_emails(line_lst): # A list of lines that meet our search criteria
    tot_emails = []
    for item in line_lst:
        email = item
        commit = line_lst.count(item)
        num = commit, email
        tot_emails.append(num)
    tot_emails.sort(reverse=True)
        
    print(tot_emails[0])
       
    
#Unit Tests"""
#assert commit_address() == (100, 'email@email.net')
#print('Passed unit test.')    

main()

