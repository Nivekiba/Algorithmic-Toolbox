#Uses python3

import sys
import functools
import random
import itertools

def cmp_digits_str(a, b):
	f = int(a+b)
	g = int(b+a)
	if f > g: return -1
	elif f < g: return 1
	else: return 0
		

def largest_number(a):
	a = list(map(str, a))
	cmpd = functools.cmp_to_key(cmp_digits_str)
	a.sort(key=cmpd)
	return int("".join(a))
	
def largest_number_naive(a):
	maxi = -1
	for e in itertools.permutations(a):
		maxi = max(int("".join(map(str,e))), maxi)
	return maxi

if __name__ == '__main__':
	input()
	a = list(map(int, input().split()))
	print(largest_number(a))
	
	#### Stress test ####
	"""
	n_m = 2
	a_m = 1000
	
	while True:
		n = random.randint(2, 1+n_m)
		a = []
		for i in range(n): a.append(random.randint(0,a_m))
		ln = largest_number(a)
		lnn = largest_number_naive(a)
		print(a)
		if ln != lnn:
			print(a)
			print(ln, lnn)
			break """
		
		
