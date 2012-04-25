def smallest_divisible_number_20():
	num = 20
	temp = 20
	while True:
		if not is_all_divisible(temp):
			temp+=num
		else:
			return temp
	return temp

def is_all_divisible(num):
	i = 2
	while i<=20:
		if(num%i !=0):
			return False
		i+=1
	return True

print smallest_divisible_number_20()
