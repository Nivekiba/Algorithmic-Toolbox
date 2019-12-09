# Uses python3
def calc_fib(n):
	n = n % 60
	if (n <= 1):
		return n
	a,b =0,1
	for i in range(n-1):
		a,b=b,a+b
	return (b*(a+b))%10


n = int(input())
print(calc_fib(n))
