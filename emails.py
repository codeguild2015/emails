def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file = open(filename, 'r')
    return file

def list_split(file):
    """Parses the .txt file, extracts all lines starting with "From" and appends them to a list."""
    lst = []
    for line in file:
        if line.split(" ")[0] == "From":
            lst.append(line.split(" "))
    return lst

def build_dict(lst):
    count_dict = {}
    """Returns a dictionary of lists with each containing count of commits and author"""
    for item in lst:
        if item[1] in count_dict:
            count_dict[item[1]] += 1
        else:
            count_dict.update({item[1]: 1})
    return count_dict

def final(dict):
    """Takes dictionary and returns sorted list"""
    final_list = []
    for name, count in dict.items():
        final_list.append([count,name])
    final_list.sort(reverse=True)
    return final_list


def main():
    file = open_file()
    lst = list_split(file)
    count = build_dict(lst)
    final_list = final(count)
    print(str(final_list[0][0]) + " - " + final_list[0][1])

main()