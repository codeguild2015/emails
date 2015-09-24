def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file1 = open(filename, 'r')
    return file1

def list_split(iter1):
    """Parses the .txt file, extracts all lines starting with "From" and appends them to a list."""
    lst = []
    for line in iter1:
	#In order to split the lines into a list so that they can be indexed, occasional 
	#instances of two spaces related to Date input (e.g. Jan 21 vs Jan  1) 
	#needed to be reduced to one space to avoid incorrect indexing
        line_temp = line.replace("  ", " ").split(" ")  
        if line_temp[0] == "From":
            lst.append(line_temp)
    return lst

def build_dict_names(lst):
    count_dict = {}
    """Returns a dictionary of lists with each containing count of commits and author"""
    for item in lst:
        if item[1] in count_dict:
            count_dict[item[1]] += 1
        else:
            count_dict.update({item[1]: 1})
    return count_dict

def build_dict_hours(lst):
    hours_dict = {}
    for item in lst:
        if int(item[5][:2]) in hours_dict:
            hours_dict[int(item[5][:2])] += 1
        else:
            hours_dict.update({int(item[5][:2]): 1})
    return hours_dict

def final(dict):
    """Takes dictionary and returns sorted list"""
    final_list = []   #empty list for storing dictionary elements in
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
    for item in hours_count:
        print("Hour: {}, Commits: {}".format(item, hours_count[item]))
    print("Total Commits = {}".format(len(lst)))


main()


assert(main('This should not return anything') == None

#assert(main('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008') == 