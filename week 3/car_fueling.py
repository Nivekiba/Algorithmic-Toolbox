# python3
import sys


def compute_min_refills(distance, tank, stops):
	
	points = [0]+stops+[distance]
	
	num_refill = 0
	i = 0
	while i < len(points)-1:
		last_refill = i
		
		while i < len(points)-1 and points[i+1] - points[last_refill] <= tank:
			i += 1
		# print(ind, i)
		if i == last_refill: return -1
		if i < len(points)-1:
			num_refill += 1

	return num_refill

if __name__ == '__main__':
	d = int(input())
	m = int(input())
	input() 
	stops = list(map(int, input().split()))
	print(compute_min_refills(d, m, stops))
