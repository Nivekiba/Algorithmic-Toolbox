# Uses python3
import sys

def get_number_of_inversions(a, left, right):
	number_of_inversions = 0
	if right - left <= 1:
		return a[left:right], number_of_inversions
	ave = (left + right) // 2
	
	A1, n1 = get_number_of_inversions(a, left, ave)
	A2, n2 = get_number_of_inversions(a, ave, right)
	M1, nm = merge(A1, A2)
	# print(A1, "+", A2, "=", M1)
	return M1, n1+n2+nm
    
def merge(B, C):
	A = []
	n_inv = 0
	ib, ic = 0, 0
	while ib<len(B) and ic<len(C):
		if B[ib] > C[ic]:
			A.append(C[ic]) 
			n_inv += len(B)-ib
			ic += 1
		else:
			A.append(B[ib])
			ib += 1
			
	if ic < len(C):
		while ic < len(C):
			A.append(C[ic])
			ic += 1
	if ib < len(B):
		while ib < len(B):
			A.append(B[ib])
			ib += 1
	return A, n_inv
    	

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_number_of_inversions(a, 0, len(a))[1])
