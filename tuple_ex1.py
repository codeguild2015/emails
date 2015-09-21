#filename = input('input filename '  )
#file = open(filename, 'r')


def parsefile(filename):
    file = open(filename, 'r')
    for line in file:
        lst1 = line.split()
        for words in lst1:
            if lst1[0] == "From":
                print(lst1)
				
	## put code here
	#"print(line)
	
#def count_user_commits:

parsefile('mbox.txt')