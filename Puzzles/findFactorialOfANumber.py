########## Python Program to find the factorial of a given number########

def factOfANumber(x):
	if x == 0 :
		return 1	
	return x * factOfANumber(x-1)
	
##Take input of X###
x = int(input())
##print ('test' + ' 2')
str1 = "The factorial of the number "
str1 = str1 + str(x) + " is :"
strFactOut = str(factOfANumber(x))
print ( str1 + strFactOut)
input()