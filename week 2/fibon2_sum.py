# Uses python3
import sys

def fibonacci_sum_naive(m,n):
	n = n % 60
	previous = 0
	current  = 1
	sum      = 1

	for _ in range(n-1):
		previous, current = current, previous + current
		sum += current
	sumn = sum
	if n <= 1: sumn = n

	m = (m-1) % 60
	previous = 0
	current  = 1
	sum      = 1

	for _ in range(m-1):
		previous, current = current, previous + current
		sum += current
	summ = sum
	if m <= 1: summ = m

	return (sumn-summ)%10

if __name__ == '__main__':
	inpt = input()
	m,n = map(int,inpt.split())
	print(fibonacci_sum_naive(m,n))
