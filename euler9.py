def triplet_prod():
	product = 0;
	
	# both a and b cannot be greater than 500
	for a in range(1,500):
		for b in range(a,500):
			c=1000-a-b
			if(c>0 and c*c==a*a+b*b):
				product = a*b*c
	print product
	
triplet_prod()
				
