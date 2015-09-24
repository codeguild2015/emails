"""put in header with authors and how it works and stuff

check google style guide"""

def open_file():
    """Open file and return text as a variable"""
    filename = input("\nInput filename "  )
    file1 = open(filename, 'r')
    return file1


def list_split(iter1):
    """Parses the .txt file, extracts all lines starting with "From" and appends them to a list."""
    lst = []
    for line in iter1:
        line_temp = line.replace("  ", " ").split(" ")
        if line_temp[0] == "From":
            lst.append(line_temp)
    return lst


def build_count_dict(lst):
    """Return a dictionary of lists with each containing count of commits and author"""
    count_dict = {}
    for item in lst:
        count_dict[item[1]] = count_dict.get(item[1], 0) + 1
    return count_dict


def main():
    iter1 = open_file()
    lst = list_split(iter1)
    name_count = build_count_dict(lst)
    head, *tail = sorted(name_count.items(), key=lambda x:x[1], reverse=True)
    print("Most commits: {} - {}\n".format(head[0], head[1]))
    

main()
 