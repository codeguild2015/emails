def parse_file(filename):
	'''Input - filename of helper files
	Output - Some sort of data structure with all 'From' lines with leading from removed'''
	file = open(filename, r)
	for line in file:
		print(line)
	# return lst

def count_user_commits():
	'''Input - Data structure with all the lines of username data
	Output - Tuple with username and number of commits ordered from least to most commits'''
	pass



parse_file("mail_short.txt")

#txt = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
 # sets words to a list of each word from string txt
#print(words)
#print(words[1])
#addresses = () # create an empty tuple
#addresses =+ word[1]

#t = list()  # instantiate and empty list.
#print("The value of list is: ", list)
#for word in words:
#  t.append((len(word), word)) # - Gives us a tuple with the lenght of the word and the word.

#t.sort(reverse=True) # returns the sort in reverse order

#res = list()
#for length, word in t:
#    res.append(word)

#print(res)