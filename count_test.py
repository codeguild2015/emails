#unique = ['jessie', 'sally', 'raphael']
#lst = [['sally', '1', '2'], ['sally', '1', '2'], ['raphael', '1', '2'], ['sally', '1', '2']]

t = list() #list variable for storing a list of tuples
for name in unique:
	count = 0 #re-init the counter to 0 for each element of the unique list
	for index, elem in enumerate(lst):
		#print("name in inner for is:", name)
		print(index, elem)
		if name == elem[0]:
			#print("elem[0] is:  ", elem[0])
			count += 1
			#print("name is:  ", name)
			#print("count is:  ", count)
		#print("the value of t before appending is:  ", t)
		#print( "the type of t is:  ", type(t) )
	t.append((name, count))
		#t = name, count
		#print("t is type: ", type(t))
print("t contains:  ", t)
#print(sorted(t, key=lambda commits: commits[1]) )