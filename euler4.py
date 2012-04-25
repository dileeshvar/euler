def largest_palindrome():
	max_prod = 0
	for a in range(999,100,-1):
		for b in range(999,100,-1):
			prod = a*b
			if(max_prod<prod and is_palindrome(prod)):
				max_prod = prod
	return max_prod
	
	
def is_palindrome(num):
	s = str(num)
	rev = s[::-1]
	if s==rev:
		return True
	return False

print largest_palindrome()
