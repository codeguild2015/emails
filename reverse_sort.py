def sort_reverse(lst_of_tups):
	'''input list of tuples from count function
	output sorted list keying on the # of commits value'''
	#pass
    #lst_of_tups.sort(reverse = True)
    #print("lst_of_tups contains:  ", lst_of_tups)
    #print(sorted(lst_of_tups, key=lambda commits: commits[1]) )
    #lst_of_tups( sorted(lst_of_tups, key=lambda commits: commits[1]) )
    #lst_of_tups(:-1)  
	print("lst_of_tups in sort_reverse before sort is:", lst_of_tups)
	for count, val in lst_of_tups.sort(reverse=True):
		print(count, val)


lst_tups=[('raphael', 1), ('jessie', 0), ('sally', 2)]
#print('Value of lst_tups is:  ', lst_tups)
sort_reverse(lst_tups)