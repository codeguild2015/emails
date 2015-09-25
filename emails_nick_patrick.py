#Authored by Patrick McNally and Nicholas Rivera
# Created on 09/25/15
#A program that reads a text file, pulls line based on criteria, 
#organizing them into a dictionary and returns a desired value.

def open_file():
    """Prompt user for a file name and return that file

    Parameters
    ----------
    Input:
    

    Output:
    file1: list
    A list with each line in the file being stored as a list element
    """

    filename = input("\nEnter a file name: "  )
    file1 = open(filename, 'r')
    return file1


def from_line_split(iter1):
    """Convert file to list of lists

    Parses original list, extracts all lines starting with "From" and 
    appends them as a list to the new list.

    Parameters
    ----------
    Input:
    iter1: list
    The file as a list

    Output:
    lst: list
    A list of lists where each internal list contains a line split at " "
    """

    lst = []
    for line in iter1:
        #Double spaces occur when single digit day is present. Replace resolves issue.
        line_temp = line.replace("  ", " ").split(" ") 
        if line_temp[0] == "From":
            lst.append(line_temp)
    return lst


def build_count_dict(lst):
    """Return a dictionary where keys = author and values = commits.

    Parameters
    ----------
    Input:
    lst: list
    A list of lists where each internal list contains a line split at " "

    Output:
    count_dict: dictionary
    A dictionary where keys = author and values = commits.
    """

    count_dict = {}
    for item in lst:
        count_dict[item[1]] = count_dict.get(item[1], 0) + 1
    return count_dict


def pull_head(dict1):
    """Pulls the key, value pair with the highest value

    Parameters
    ----------
    Input:
    count_dict: dictionary
    A dictionary where keys = author and values = commits.

    Output:
    head: tuple
    A tuple containing an email address and # of commits
    """

    head, *tail = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    return head


def main():
    """Takes a text file and evaluates it to extract and present contents.

    Takes in a text file (desigend for list of commits to git) and pulls
    all lines beginning with "From".  From those lines it extracts and 
    counts email addresses and the number of times they committed.

    Ex.
    ---
    "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008" = {"stephen.marquard@uct.ac.za" : 1}

    Parameters
    ----------
    Input:

    Output:
    """

    iter1 = open_file()
    lst = from_line_split(iter1)
    name_count = build_count_dict(lst)
    head = pull_head(name_count)
    print("Most commits: {} - {}\n".format(head[0], head[1]))


    
if __name__ == '__main__':
    main()


