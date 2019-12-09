# Uses python3
import sys

def fibonacci_sum_naive(n):
	n = n % 60
	if n <= 1:
		return n

	previous = 0
	current  = 1
	sum      = 1

	for _ in range(n-1):
		previous, current = current, (previous + current)%10
		sum += current

	return sum % 10

if __name__ == '__main__':
	inpt = input()
	n = int(inpt)
	print(fibonacci_sum_naive(n))
