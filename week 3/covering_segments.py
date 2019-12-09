# Uses python3
import sys
import functools
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def seg_cmp(a, b):
	if a.start < b.start: return -1
	elif a.start > b.start: return 1
	else:
		if a.end < b.end: return -1
		elif a.end > b.end: return 1
		else: return 0
		
def optimal_points(segments):
	points = []
	#print("missing segment ?", segments[57], segments[56])
	cmpd = functools.cmp_to_key(seg_cmp)
	segments.sort(key=cmpd)
	if len(segments) == 0: return []
	
	seg1 = segments[0]
	for i in range(len(segments)-1):
		seg2 = segments[i+1]
		if seg1.end >= seg2.start:
	#		print("next for", seg2)
			seg1 = Segment(seg2.start, min(seg1.end, seg2.end))
		else:
			points.append(min(seg1.end, seg1.start))
	#		print("point", seg1.start, seg1.end)
	#		print("next for", seg2)
			seg1 = seg2
	
	points.append(min(seg1.end, seg1.start))
	
	return points

if __name__ == '__main__':
	n = int(input())
	segments = []
	for i in range(n):
		t=input().split()
		segments.append(Segment(int(t[0]), int(t[1])))
	points = optimal_points(segments)
	print(len(points))
	print(*points)
