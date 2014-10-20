

palin = raw_input('What is the string of letters?')

def palindrome(palin):
    if len(palin) >=1 and len(palin) < 10 ** 5 and palin == palin[::-1]:
	 sys.stdout.write("YES")
    else:
         sys.stdout.write("NO")
palindrome(palin)
