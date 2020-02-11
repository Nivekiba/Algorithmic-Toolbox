#Uses python3
import sys
import math
import functools
import random

def seg_cmp(a, b):
	if a[0] < b[0]: return -1
	elif a[0] > b[0]: return 1
	else:
		if a[1] < b[1]: return -1
		elif a[1] > b[1]: return 1
		else: return 0
		
def seg_cmp_by_y(a, b):
	if a[1] < b[1]: return -1
	elif a[1] > b[1]: return 1
	else:
		if a[0] < b[0]: return -1
		elif a[0] > b[0]: return 1
		else: return 0
		
def minimum_distance_naive(x, y):
	d_area = 10**18
	#seg = (10**18,10**18)
	#seg2 = (0, 0)
	for i in range(len(x)):
		for j in range(i+1, len(x)):
			#if d_area > (x[i]-x[j])**2 + (y[i]-y[j])**2:
			#	seg = x[i], y[i]
			#	seg2 = x[j], y[j]
			d_area = min(
					d_area,
					(x[i]-x[j])**2 + (y[i]-y[j])**2,
				)
	# print("the result is for",seg, seg2)
	return d_area

def minimum_distance(x, y):
	
	# base case.. we only have 2 or 3 points
	## 2 points
	if len(x) == 2:
		return (x[0]-x[1])**2 + (y[0]-y[1])**2
	## 3 points
	elif len(x) == 3:
		return min(
			(x[0]-x[1])**2 + (y[0]-y[1])**2,
			min(
				(x[0]-x[2])**2 + (y[0]-y[2])**2,
				(x[2]-x[1])**2 + (y[2]-y[1])**2
			)
		)
	
	points = [(x[i], y[i]) for i in range(len(x))]
	left_points = points[: len(x)//2]
	right_points = points[len(x)//2 :]
	
	middle_line = (left_points[-1][0] + right_points[0][0])/2
	
	# recursive call after separating the points into 2 partitions
	d1 = minimum_distance([p[0] for p in left_points], [p[1] for p in left_points])
	d2 = minimum_distance([p[0] for p in right_points], [p[1] for p in right_points])
	d = min(d1, d2)
	d_sq = d**0.5
	# we have to check now the distance between points in the area close to the middle x-line
	close_middle_points = []
	for i in range(len(points)):
		if abs(points[i][0] - middle_line) <= d_sq:
			close_middle_points.append(points[i])
	
	left_close_points = []
	for i in range(len(left_points)):
		if abs(left_points[i][0] - middle_line) <= d_sq:
			left_close_points.append(left_points[i])
	
		
	right_close_points = []
	for i in range(len(right_points)):
		if abs(right_points[i][0] - middle_line) <= d_sq:
			right_close_points.append(right_points[i])
	
	# sort the points in this area		
	#if len(close_middle_points) <= int(len(points)**0.5):
	cmpd = functools.cmp_to_key(seg_cmp_by_y)
	close_middle_points.sort(key=cmpd)
	#left_close_points.sort(key=cmpd)
	#right_close_points.sort(key=cmpd)
	
	d_area = 10**18
	for i in range(len(close_middle_points)):
		for j in range(i+1, min(8+i, len(close_middle_points))):
			#print("between",close_middle_points[i], "and", close_middle_points[j], (close_middle_points[i][0]-close_middle_points[j][0])**2 + (close_middle_points[i][1]-close_middle_points[j][1])**2)
			d_area = min(
					d_area,
					(close_middle_points[i][0]-close_middle_points[j][0])**2 + (close_middle_points[i][1]-close_middle_points[j][1])**2,
				)
	"""for i in range(len(left_close_points)):
		for j in range(min(8, len(right_close_points))):
			d_area = min(
					d_area,
					(left_close_points[i][0]-right_close_points[j][0])**2 + (left_close_points[i][1]-right_close_points[j][1])**2,
				)
				"""
	#print("\n intermediate areas", d1, d2)
	#print("\n close points to middle", close_middle_points)
	#print("\n d for middle area", d_area)
	return min(d, d_area)

if __name__ == '__main__':
	
	## Start stress test
	"""
	while True:
		n = 10000
		x = []
		y = []
		for i in range(n):
			a = random.randint(0, 3)
			b = random.randint(-10**9, 10**9)
			x.append(3)
			y.append(b)
		
		### sort points before applying algorithms
		points = [(x[i], y[i]) for i in range(len(x))]
		cmpd = functools.cmp_to_key(seg_cmp)
		points.sort(key=cmpd)

		x = [p[0] for p in points]
		y = [p[1] for p in points]
		### end sorting
		print("\t\t\tTest started")
		d_naive = minimum_distance_naive(x, y)
		d_min = minimum_distance(x, y)
		if d_naive != d_min :
			print(n)
			for i in range(n): print(x[i], y[i])
			print("fast =", d_min)
			print("naive =", d_naive)
			break
		else:
			print("Ok result", d_min)
		print("\n")
	"""
	# End stress test
	n = int(input())
	x = []
	y = []
	for i in range(n):
		a,b = map(int, input().split())
		x.append(a)
		y.append(b)
	points = [(x[i], y[i]) for i in range(len(x))]
	cmpd = functools.cmp_to_key(seg_cmp)
	points.sort(key=cmpd)

	x = [p[0] for p in points]
	y = [p[1] for p in points]
	print("{0:.15f}".format(minimum_distance(x, y)**0.5))
