# Authored by Jaydn C and Connor M
# Written 9/24/15
# References: Google, StackOverFlow
# Program to read in a file, pull lines out based on string keyword
# converts lines into a dictionary to be sorted and returned as sorted list to print. 

def open_file():
	""" Prompting user for file name, opens corresponding file, returns contents.
	
	Paramaters
	-----
	Input:
	None
	
	Output:
	file: lst
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
	if doc:
		lst = []
		for line in doc:
			line_temp = line.replace("  ", " ").split(" ") # single double space throws error, replaced with single space
			if line_temp[0] == split_word:# allows split word to be replaced 
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
		if item[5][0:2] in times: # Pulls out time 
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
		if item[1] in emails: # checks for email, then creates dict of emails
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
	test_file_to_list()
	test_dict_times()
	test_dict_names()
	test_combine_times()
	test_combine_emails()
	doc = open_file()
	lst = file_to_list(doc)
	times = dict_times(lst)
	names = dict_names(lst)
	final_email = combine_emails(names)
	final_times = combine_times(times)
	print("Commits: ",final_email[0][0], "Email: ", final_email[0][1])# list in list needs double indexes to print properly.
	print()	
	for item in final_times:
		print("Hour:", item[0], "Commits:", item[1])

def test_file_to_list():
	assert file_to_list(None) == None
	assert file_to_list(['From test list of words']) == [['From','test','list','of','words']]
	assert file_to_list(['line without capital from']) == []
def test_dict_times():
	a = [['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
	b = [['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']]
	c = a + a + b
	assert dict_times(a) == {'09': 1}
	assert dict_times(c) == {'09': 2, '18': 1}
	assert dict_times([]) == {}
def test_dict_names():
	a = [['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']]
	b = [['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']]
	c = a + a + b
	assert dict_names(a) == {'stephen.marquard@uct.ac.za': 1}
	assert dict_names(c) == {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 1}
	assert dict_names([]) == {}
	

def test_combine_emails():
	assert combine_emails({'stephen.marquard@uct.ac.za': 1}) == [[1, 'stephen.marquard@uct.ac.za']]
	assert combine_emails({'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 1}) == [[2, 'stephen.marquard@uct.ac.za'], [1, 'louis@media.berkeley.edu']]
	assert combine_emails({}) == []

def test_combine_times():
    assert combine_times({'09': 1}) == [['09', 1]]
    assert combine_times({'09': 2, '18': 1}) == [['09', 2], ['18', 1]]
    assert combine_times({}) == []

main()