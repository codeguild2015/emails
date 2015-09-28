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
    """Return a dictionary where keys = hour and values = count of commits for that hour.

    Parameters
    ----------
    Input:
    lst: list
    A list of lists where each internal list contains a line split at " "

    Output:
    count_dict: dictionary
    A dictionary where keys = hour and values = count of commits for that hour.
    """

    count_dict = {}
    for item in lst:
        count_dict[item[5][:2]] = count_dict.get(item[5][:2], 0) + 1
    return count_dict


def format_output(dict1):
    """Presents output data in user friendly columns

    Parameters
    ----------
    Input:
    dict1: Dictionary
    A dictionary where keys = hour and values = count of commits for that hour.

    Output:
    """
    
    print("Hour - Commits")
    for item in sorted(dict1):
        print("{} - {}".format(item, dict1[item]))


def main():
    """Takes a text file and evaluates it to extract and present contents.

    Takes in a text file (desigend for list of commits to git) and pulls
    all lines beginning with "From".  From those lines it extracts and 
    counts hours and commits for those hours.

    Ex.
    ---
    "From", "stephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"]]) == {"09" : 1}

    Parameters
    ----------
    Input:

    Output:
    """
    iter1 = open_file()
    lst = from_line_split(iter1)
    hours_count = build_count_dict(lst)
    format_output(hours_count)


if __name__ == '__main__':
    main()