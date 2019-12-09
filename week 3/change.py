# Uses python3
import sys

def get_change(m):
	n = 0
	t = [10, 5, 1]
	for piece in t:
		tmp_n = m // piece
		m -= tmp_n * piece
		n += tmp_n
	return n

if __name__ == '__main__':
	m = int(input())
	print(get_change(m))
