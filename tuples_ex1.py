filename = input('mbox-short.txt ' )
file = open(filename, 'r')

for line in file:
	if "From" in line:
		a = line.split()
		if len(a) > 2:
			print(a)
	