import math
def find_nth_prime_number(num):
	prime_count = 0;
	i = 2
	while prime_count <num:
		if is_prime(i):
			prime_count+=1
		i+=1
	print i-1
	
	

def is_prime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num%i == 0:
			return False
	return True

find_nth_prime_number(10001)
