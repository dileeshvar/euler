from math import sqrt
def sum_all_primes(num):
	i =2
	total = 0;
	while i<num:
		if is_prime(i):
			total += i
		i+=1
	return total

def is_prime(num):
	for i in range(2,int(sqrt(num))+1):
		if num%i == 0:
			return False
	return True

print sum_all_primes(2000000)
