# Uses python3
import sys
import functools
import random

def seg_cmp(a, b):
	if a[0] < b[0]: return -1
	elif a[0] > b[0]: return 1
	else:
		if a[1] < b[1]: return -1
		elif a[1] > b[1]: return 1
		else: return 0

def search(x, segments, left, right, count_seg):
	
	if right - left <= 1:
		if segments[left][0] <= x <= segments[left][1]:
			return count_seg[segments[left]]
		else: return 0
	mid = (left + right)//2
	
	seg_mid = segments[mid]
	if seg_mid[1] < x: 
		return search(x, segments, mid+1, right, count_seg)
	elif seg_mid[0] > x:
		return search(x, segments, left, mid, count_seg)
	elif seg_mid[0] <= x <= seg_mid[1]: 
		return count_seg[seg_mid] + search(x, segments, mid+1, right, count_seg) + search(x, segments, left, mid, count_seg)
	

def fast_count_segments(starts, ends, points):
	cnt = [0] * len(points)
	
	"""segments = [(starts[i], ends[i]) for i in range(len(starts))]
	
	segments = list(set(segments))
	
	cmpd = functools.cmp_to_key(seg_cmp)
	segments.sort(key=cmpd)
	
	count_seg = dict()
	for x in segments: count_seg[x] = 0
	
	for i in range(len(starts)):
			count_seg[(starts[i], ends[i])] += 1
	
	for i in range(len(points)):
		cnt[i] = search(points[i], segments, 0, len(segments)-1, count_seg)"""
	
	pts = []
	for s in starts: pts.append((s, "l"))
	for s in ends: pts.append((s, "r"))
	for s in points: pts.append((s, "p"))
	
	cmpd = functools.cmp_to_key(seg_cmp)
	pts.sort(key=cmpd)
	t = dict()
	for p in points: t[p] = 0
	n_s = 0
	
	for point in pts:
		if point[1] == "l": n_s += 1
		elif point[1] == "r": n_s -= 1
		elif point[1] == "p": t[point[0]] += max(n_s, 0)
	
	count_point = dict()
	for p in points: count_point[p] = 0
	for p in points: count_point[p] += 1
	
	for i in range(len(cnt)):
		cnt[i] = t[points[i]] // count_point[points[i]]
	return cnt

def naive_count_segments(starts, ends, points):
	cnt = [0] * len(points)
	for i in range(len(points)):
		for j in range(len(starts)):
			if starts[j] <= points[i] <= ends[j]:
				cnt[i] += 1
	return cnt

if __name__ == '__main__':
	"""
	while True:
		s = random.randint(1, 10)
		p = random.randint(1, 12)
		starts = []
		ends = []
		for i in range(s):
			st = random.randint(-200, 200)
			en = st + random.randint(0, 400)
			starts.append(st)
			ends.append(en)
		points = []
		while len(points) < p:
			t = random.randint(-200, 200)
			if points.count(t) == 0:
				points.append(t)
		fcs = fast_count_segments(starts, ends, points)
		ncs = naive_count_segments(starts, ends, points)
		if fcs != ncs :
			print(s, p)
			for i in range(s): print(starts[i], ends[i])
			print(*points)
			print("fast =", *fcs)
			print("naive =", *ncs)
			break
		print("\n")
	"""
	
	s, p = list(map(int, input().split()))
	starts = []
	ends = []
	for i in range(s):
		st, en = list(map(int, input().split()))
		starts.append(st)
		ends.append(en)
	points = list(map(int, input().split()))
	#use fast_count_segments
	cnt = fast_count_segments(starts, ends, points)
	print(*cnt)
