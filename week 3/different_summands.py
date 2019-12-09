# Uses python3
import sys
import math
import random

def optimal_summands(n):
	if n == 1: return [1]
	summands = []
	maxi = math.ceil( ((1+8*n)**0.5-1)/2 )
	nb = math.floor( ((1+8*n)**0.5-1)/2 )
	summands = list(range(1,maxi+1))
	to_remove = (maxi*(maxi+1))//2-n
	if to_remove > 0:
		summands.remove( (maxi*(maxi+1))//2-n )
	return summands

def partiesliste(seq):
	p = []
	i, imax = 0, 2**len(seq)-1
	while i <= imax:
		s = []
		j, jmax = 0, len(seq)-1
		while j <= jmax:
			if (i>>j)&1 == 1:
				s.append(seq[j])
			j += 1
		p.append(s)
		i += 1 
	return p

def optimal_summands_naive(n):
	if n==1: return [1]
	k = 0
	liste = []
	for l in partiesliste(range(1,n+1)):
		if sum(l) == n and len(l) > k:
			k = len(l)
			liste = l
	return liste

if __name__ == '__main__':
	n = int(input())
	summands = optimal_summands(n)
	print(len(summands))
	print(*summands)
	
	### Stressed test
	"""while True:
		n = random.randint(1, 20)
		print(n)
		l_naives = optimal_summands_naive(n)
		l_opt = optimal_summands(n)
		if set(l_opt) != set(l_naives):
			print(l_opt, l_naives)
			break"""
