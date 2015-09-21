
def count_by_name():
	filename = input("input filename ")
	file = open(filename, 'r')
	

	name_list = []
	for line in file:
		line.strip()
		words = line.split()
		if words and words[0] == 'From':
			name_list.append(words[1])
		else:
			continue
	result_list = []
	for item in name_list:
		result_list.append((name_list.count(item), item))

	result_list.sort(reverse=True)
	print(result_list)




count_by_name()
