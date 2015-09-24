def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
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

def build_dict_names(lst):
    """Returns a dictionary of lists with each containing count of commits and author"""
    count_dict = {}
    for item in lst:
        count_dict[item[1]] = count_dict.get(item[1], 0) + 1
    return count_dict

def build_dict_hours(lst):
    hours_dict = {}
    for item in lst:
        hours_dict[item[5][:2]] = hours_dict.get(item[5][:2], 0) + 1
    return hours_dict

def final(dict):
    """Takes dictionary and returns sorted list"""
    final_list = []
    for name, count in dict.items():
        final_list.append([count,name])
    final_list.sort(reverse=True)
    return final_list


def main():
    iter1 = open_file()
    lst = list_split(iter1)
    name_count = build_dict_names(lst)
    final_list = final(name_count)
    hours_count = build_dict_hours(lst)
    

    print("Most commits = " + str(final_list[0][0]) + " - " + final_list[0][1])
    for item in sorted(hours_count):
        print("Hour: {}, Commits: {}".format(item, hours_count[item]))



main()
 