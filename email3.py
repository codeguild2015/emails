def open_file():
	''' Opens file, returns contents'''
	filename = input("Please input file name: ")
	file = open(filename, 'r')
	return file

def file_to_list(doc):
	'''takes file, splits at "from", returns list of emails'''
	lst = []
	for line in doc:
		line_temp = line.replace("  ", " ").split(" ")
		if line_temp[0] == "From":
			lst.append(line_temp)
	return lst
	
def dict_times(lst):
	''' takes lst from file_to_list, seperates out times and puts into dict '''
	times = {} 
	for item in lst:
		if item[5] in times:
			times[item[5]]+=1
		times.update({item[5] : 1})
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
		lst.append([count,name])
	lst.sort(reverse = True)
	return lst
	
def main():
	doc = open_file()
	lst = file_to_list(doc)
	times = dict_times(lst)
	names = dict_names(lst)
	final_email = combine_emails(names)
	final_times = combine_times(times)
	for item in final_email:
		print(item)
	for item in final_times:
		print(item)

main()