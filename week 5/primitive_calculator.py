# Uses python3
import sys
import random

def naive_sequence(n):
	sequence = []
	while n >= 1:
		sequence.append(n)
		if n % 3 == 0:
			n = n // 3
		elif n % 2 == 0:
			n = n // 2
		else:
			n = n - 1
	return sequence[::-1]

def optimal_sequence(n):
	child = [0]*(n+1)
	num = [10**15]*(n+1)
	num[1] = 0
	for i in range(1, n+1):
		# ai + 1 // finding fast ancestor
		if i+1 < n+1 and num[i]+1 < num[i+1]:
			num[i+1] = num[i]+1
			child[i+1] = i
		# ai * 2 // finding fast ancestor
		if i*2 < n+1 and num[i]+1 < num[i*2]:
			num[i*2] = num[i]+1
			child[i*2] = i
		# ai * 3 // finding fast ancestor
		if i*3 < n+1 and num[i]+1 < num[i*3]:
			num[i*3] = num[i]+1
			child[i*3] = i
	seq = [n]
	t = child[n]
	while True:
		if t == 0: break
		seq.append(t)
		t = child[t]
	return seq[::-1]

n=int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
print(*sequence)
