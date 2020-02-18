# Uses python3
import sys
import math

def optimal_weight(W, w):
	value = []
	n = len(w)
	for i in range(W+1):
		value.append([0]*(n+1))
	gcd = w[0]
	if len(w)>1:
		for e in w: 
			gcd = math.gcd(gcd, e)
			
	for wi in range(1, W+1):
		for i in range(1, n+1):
			value[wi][i] = value[wi][i-1]
			if w[i-1] <= wi:
				value[wi][i] = max(value[wi][i], value[wi-w[i-1]][i-1] + w[i-1])
	return value[W][n]

if __name__ == '__main__':
	W, n = list(map(int, input().split()))
	w = list(map(int, input().split()))
	print(optimal_weight(W, w))
