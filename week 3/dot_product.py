#Uses python3

import sys

def max_dot_product(a, b):
	#write your code here
	res = 0
	for e,d in zip(sorted(a), sorted(b)):
		res += e*d
	return res

if __name__ == '__main__':
	n = input()
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(max_dot_product(a, b))
    
