def tuple_full():
    count_dict = {}
    final_lst = []
    filename = input("input filename "  )
    file = open(filename, 'r')

    for line in file:
        lst = line.split(" ")
        if lst[0] == "From":
            

            if lst[1] in count_dict:
                count_dict[lst[1]] += 1
            else:
    	        count_dict.update({lst[1]: 1})
    
    for name, count in count_dict.items():
        final_lst.append([count,name])
    final_lst.sort(reverse=True)
    print(final_lst)
        

tuple_full()
