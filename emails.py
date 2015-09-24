# Authored by Jaydn C and Connor M
# Written 9/24/15
# Program to read in a file, pull lines out based on user inputed string keyword

def open_file():
	""" Opens file, returns contents
	Paramaters
	-----
	Input:
	file
	text doc
	
	Output:
	string 
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
	
	Output:
	lst: list
	list of lines extracted from doc'''
	
	lst = []
	for line in doc:
		line_temp = line.replace("  ", " ").split(" ")
		#if line_temp[0] == "From":
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
	times: dictionary
	'''
	
	times = {} 
	for item in lst:
		if item[5][0:2] in times:
			times[item[5][0:2]] += 1
		else:
			times.update({item[5][0:2] : 1})
	return times

def dict_names(lst):
	""" takes list of emails and puts them into a dictonary"""
	emails = {}
	for item in lst:
		if item[1] in emails:
			emails[item[1]] +=1
		else:
			emails.update({item[1]: 1})
	return emails	
	
def combine_emails(names):
	""" Turns dictonary into a sortable list"""
	lst = [] 
	for name, count in names.items():
		lst.append([count, name])
	lst.sort(reverse = True)
	return lst
	
def combine_times(times):
	''' Turns time dictonary into sortable list''' 
	lst = []
	for name, count in times.items():
		lst.append([count, name])
	lst.sort()
	return lst
	
def main():
""" Calls each funtion in order, assigns input variables for each subsequent function"""
	doc = open_file()
	lst = file_to_list(doc)
	times = dict_times(lst)
	names = dict_names(lst)
	final_email = combine_emails(names)
	final_times = combine_times(times)
	print(final_email[0])
	print()	
	for item in final_times:
		print("Commits for the hour: ",item)

main()