"""commit_address() prompts the user for a text file to scan.  \n
The program then scans the file for lines containing the world \n
the word \'From' and splits the line into a list. As we are only \n
concerned with lists containing more than two items, the program will \n
discard lines shorter than this, as they do not contain valid email \n
addresses.  \n\n

The program will then sort the email addresses and return the one with \n
the most number of commits, along with the total number of commits."""


def commit_address():
    filename = input("input filename ")
    file = open(filename, 'r')

    add_lst = []
    for line in file:
        if "From" in line:
            if len(line.split()) > 2:
                a = line.split()
                add_lst.append(a[1])
    
    num_lst = []
    for item in range(len(add_lst)):
        email = add_lst[item]
        commit = add_lst.count(add_lst[item])
        num = commit, email
        num_lst.append(num)
    num_lst.sort(reverse=True)

    print(num_lst[0])
    # print(num_lst)
    file.close()

# """Unit Tests"""
# assert commit_address() == type(int)
# assert commit_address() == ('email@email.net')
# assert commit_address(['stephen.marquard@uct.ac.za'])

# print('Passed unit test.')    
    
commit_address()
