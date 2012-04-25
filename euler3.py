def largest_primeFactor():
	max_factor = 0
	num = 600851475143
	j =2;
		
	while j<num:
		while(num%j==0):
			num=num/j
		j+=1
	print num
	
largest_primeFactor()
