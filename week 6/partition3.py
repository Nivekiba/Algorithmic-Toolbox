# Uses python3
import sys

dictio = {}

def recur_partition3(S, n, a, b, c):
	
	key = str(n)+"|"+str(a)+"|"+str(b)+"|"+str(c)
	
	if key in dictio.keys():
		return dictio[key]
	
	if a==b==c==0: return True
	if n < 0: return False
	
	A = False
	if a-S[n] >= 0:
		A = recur_partition3(S, n-1, a-S[n], b, c)
	
	B = False
	if b-S[n] >= 0:
		B = not(A) and recur_partition3(S, n-1, a, b-S[n], c)
	
	C = False
	if c-S[n] >= 0:
		C = not(A or B) and recur_partition3(S, n-1, a, b, c-S[n])
	
	dictio[key] = A or B or C
	return dictio[key]

def partition3(S):
	return not(sum(S)%3) and recur_partition3(S, n-1, sum(S)//3, sum(S)//3, sum(S)//3)

if __name__ == '__main__':
	n = int(input())
	A = list(map(int, input().split()))
	print( int(partition3(A)) )

