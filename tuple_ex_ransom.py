#filename = input('input filename '  )
#file = open(filename, 'r')


def parsefile(filename):
    '''Inputs file containing mbox file
    Outputs - list with elements containing addresses, and times stamps.'''

    file = open(filename, 'r')
    for line in file:
        lst1 = line.split()
        for words in lst1:
            if lst1[0] == "From":
                #print(lst1)
                lst2 = lst1.splice[1:]
                print(lst2)
				
	## put code here
	#"print(line)
	
#def count_user_commits():
#    '''Inputs - '''
#    pass


parsefile('mbox.txt')