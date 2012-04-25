def sumOf_mul_3_5():
	sumOf35 = 0;
	for i in range(1,1000):
		if i%3 == 0 or i%5 == 0:
			sumOf35+=i;
	print sumOf35


sumOf_mul_3_5()
