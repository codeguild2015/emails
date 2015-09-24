#put in header with authors and how it works and stuff
#
#check google style guide

def open_file():
    """Opens file and saves text as a variable"""
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
    """ put comment here please"""
    count_dict = {}
    for item in lst:
        count_dict[item[5][:2]] = count_dict.get(item[5][:2], 0) + 1
    return count_dict

def prep_out_list(dict1):
    """please add header here"""
    print("Hour - Commits")
    for item in sorted(dict1):
        print("{} - {}".format(item, dict1[item]))


def main():
    """ put comment here please"""
    iter1 = open_file()
    lst = list_split(iter1)
    hours_count = build_count_dict(lst)
    prep_out_list(hours_count)

main()
