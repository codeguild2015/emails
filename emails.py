# Authored by Jaydn C and Connor M
# Written 9/24/15
# Program to read in a file, pull lines out based on string keyword
# converts lines into a dictionary to be sorted and returned as sorted list to print. 

def open_file():
	""" Prompting user for file name, opens corresponding file, returns contents.
	
	Paramaters
	-----
	Input:
	None
	
	Output:
	file: string
	file turned into string and assigned to variable for input on other functions"""
	
	filename = input("Please input file name: ")
	file = open(filename, 'r')
	return file

def file_to_list(doc, split_word="From"):
	'''takes doc, adds line into a list based on specific key word search
	Parameters
	---------
	Input:
	doc: string
	split_word: defaults to "From". 
	Skips lines not starting with split_word.
	
	Output:
	lst: list
	list of lines extracted from doc'''
	
	lst = []
	for line in doc:
		line_temp = line.replace("  ", " ").split(" ")
		if line_temp[0] == split_word:
			lst.append(line_temp)
	return lst
	
def dict_times(lst):
	''' takes lst, creates dict, updates indexed items to dict, otherwise, creates item in dict. 
	Parameters
	----------
	Input:
	lst: list
	
	Output:
	times: dictionary'''

	times = {} 
	for item in lst:
		if item[5][0:2] in times:
			times[item[5][0:2]] += 1
		else:
			times.update({item[5][0:2] : 1})
	return times

def dict_names(lst):
	''' takes lst containing emails and returns dict of emails and occurences.
	
	Parameters
	----------
	Input:
	lst: list
	
	Output:
	times: dictionary'''
	
	emails = {}
	for item in lst:
		if item[1] in emails:
			emails[item[1]] +=1
		else:
			emails.update({item[1]: 1})
	return emails	
	
def combine_emails(names):
	""" Takes dictonary in, converts item pairs in dict to a list
	Parameters
	----------
	Input:
	dict1: dictionary
	
	Output:
	lst: list
	sorted list """
	
	lst = [] 
	for name, count in names.items():
		lst.append([count, name])
	lst.sort(reverse = True)
	return lst
	
def combine_times(times):
	""" Takes dictonary in, converts item pairs in dict to a list
	Parameters
	----------
	Input:
	dict1: dictionary
	
	Output:
	lst: list
	sorted list """
	
	lst = []
	for name, count in times.items():
		lst.append([name , count])
	lst.sort()
	return lst
	
def main():
	""" Calls each funtion in order, assigns input variables for each subsequent function
	Parameters
	----------
	Inputs:
	
	Outputs:
	doc: string
	lst: list
	times: dict
	names: dict
	final_email: list
	final_times: list"""
	#test_file_to_list()
	doc = open_file()
	lst = file_to_list(doc)
	times = dict_times(lst)
	names = dict_names(lst)
	final_email = combine_emails(names)
	final_times = combine_times(times)
	#print(final_email[0])
	for item in final_email:
		print(item)
	print()	
	for item in final_times:
		print("Hour:", item[0], "Commits:", item[1])

#def test_file_to_list():

#def test_dict_times():

#def test_dict_names():

#def test_combine_emails():

#def test_combine_times():

main()
