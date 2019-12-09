# Uses python3
import sys

def gcd(a, b):
	if a == 0: return b
	if b == 0: return a
	if a>b: return gcd(b, a%b)
	return gcd(a, b%a)

if __name__ == "__main__":
	inpt = input()
	a, b = map(int, inpt.split())
	print((a*b)//gcd(a, b))
