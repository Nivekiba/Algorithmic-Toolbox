# Uses python3
import sys

def binary_search(a, x):
	left, right = 0, len(a)
	# write your code here

def linear_search(a, x):
	return linear_search_rec(a, 0, len(a)-1, x)
	
def linear_search_rec(a, ind, fin, x):
	if fin <= ind:
		if a[fin] != x: return -1
		else: return fin
	mid = (ind+fin+1)//2
	if a[mid] < x: return linear_search_rec(a, mid+1, fin, x)
	elif a[mid] > x: return linear_search_rec(a, ind, mid-1, x)
	else: return mid

if __name__ == '__main__':
	a = list(map(int, input().split()))
	a = a[1:]
	b = list(map(int, input().split()))
	b = b[1:]
	for x in b:
		# replace with the call to binary_search when implemented
		print(linear_search(a, x), end = ' ')
