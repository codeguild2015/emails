"""commit_hour() prompts the user for a text file to scan.  \n
The program then scans the file for lines containing the word \n
the word \'From' and splits the line into a list. As we are only \n
concerned with lists containing more than two items, the program will \n
discard lines shorter than this, as they do not contain valid timestamps. \n\n

The program will then sort the timestamps and return one per line with \n
the most number of commits, along with the total number of commits."""

def commit_hour():
    filename = input("input filename ")
    file = open(filename, 'r')
    hour_lst = []

    for line in file:
        if "From" in line:
            if len(line.split()) > 2:
                a = line.split()
                b = a[5]
                hour_lst.append(b[:2])


    fin_count_hour = [] 
    for item in range(len(hour_lst)):
        commit_count = hour_lst.count(hour_lst[item])
        commit_time = hour_lst[item]
        commit_tuple = commit_count, commit_time
        fin_count_hour.append(commit_tuple)
        fin_count_hour.sort(reverse=True)
    
    for item in range(len(fin_count_hour)):
        if fin_count_hour[item] != fin_count_hour[item - 1]:
            print(fin_count_hour[item])
    file.close()
  
# """Unit Tests"""
# assert commit_hour() == (100, '10')
# print('Passed unit test.')

commit_hour()


                               
