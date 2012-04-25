def fibonacci():
	f1=0
	f2=0
	f3=1
	fib_sum=0
	while f3<4000000:
		if f3%2 == 0:
			fib_sum+=f3
		f1=f2
		f2=f3
		f3=f1+f2
	print fib_sum

fibonacci()
