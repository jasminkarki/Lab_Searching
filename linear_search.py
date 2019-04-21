def linear_search(values, target):
	n=len(values)
	i=0
	for i in range(n):
		if values[i]==target:
			#print(values[i])
			return values[i]