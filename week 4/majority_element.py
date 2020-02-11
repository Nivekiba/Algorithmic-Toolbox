# Uses python3
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	
	mid = (left + right)//2
	m1 = get_majority_element(a, left, mid)
	m2 = get_majority_element(a, mid, right)
	
	major_element = check_candidates(a, left, right, m1, m2)
	return major_element

def check_candidates(a, left, right, m1, m2):
	n_m1 = 0
	n_m2 = 0
	for i in range(left, right):
		if m1 != -1 and a[i] == m1: n_m1 += 1
		if m2 != -1 and a[i] == m2: n_m2 += 1
	n = right-left
	if n_m1 > n/2 and m1 != -1: return m1
	elif n_m2 > n/2 and m2 != -1: return m2
	else:
		return -1	
	
if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
