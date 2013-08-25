def factorial_iterative(n):
	factorial = 1
	for i in range(2,n+1):
		factorial *= i
	return factorial

def factorial_recursive(n):
	return 1 if n==1 or n==0 else n * factorial_recursive(n-1)

assert factorial_iterative(0) == 1
assert factorial_iterative(1) == 1
assert factorial_iterative(5) == 120

#verifies that factorial_iterative and factorial_recursive return the same result
for i in range(0, 10):
	assert factorial_iterative(i) == factorial_recursive(i)
