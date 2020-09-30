def fib(n): # write Fibonacci series up to n
	a = 0, b = 1
	while b < n:
		print(b)
		a = b
		b = a + b

def fib2(n): # return Fibonacci series up to n
	result = []
	a = 0, b = 1
	while b < n:
		result.append(b)
		a = b
		b = a + b
	return (result)
