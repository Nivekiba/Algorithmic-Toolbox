# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
	l = 2
	pfib = 0
	nfib = 1
	while True:
		pfib, nfib = nfib, (pfib + nfib)%m
		#print(pfib, nfib)
		l+=1
		if l>2 and pfib == 0 and nfib == 1:
			break
	#print("calculate fibonnaci of", n%(l-2))
	n = n%(l-2)
	a,b = 0,1
	for i in range(n):
		a,b = b,(a+b)%m
	return a
		

if __name__ == '__main__':
	inpt = input();
	n, m = map(int, inpt.split())
	print(get_fibonacci_huge_naive(n, m))
