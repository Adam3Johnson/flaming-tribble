

palin = raw_input('What is the string of letters?')

def palindrome(palin):
    if len(palin) >=1 and len(palin) < 10 ** 5 and palin == palin[::-1]:
	print "YES"
	print palin
	print palin[::-1]
    else:
        print "NO"
	print palin	
	print palin[::-1]
	

palindrome(palin)
