#filename = input('input filename '  )
#file = open(filename, 'r')


def parsefile(filename):
    file = open(filename, 'r')
    res = []
    for line in file:
        lst1 = line.split()
        for words in lst1:
            if lst1[0] == "From":
                return lst1([res])
				
            
							
def create_unique_address(lst):
    '''inputs - list of lists from read_file()
    outputs - list of unique address'''
    for words in res: 
	    res.append(lst1[1:])
            return 

				
	## put code here
	#"print(line)
	
#def count_user_commits:

print(parsefile('mbox-short.txt'))
