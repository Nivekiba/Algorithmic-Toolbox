#Uses python3

import sys

# Uses python3
def edit_distance_long_sub_seq(s, t):
	n, m = len(s), len(t)
	# table that containing the values of edit distance continously for the 2 sequences	
	d = []
	for i in range(len(s)+1):
		d.append([0]*(len(t)+1))
		
	for i in range(1,len(s)+1):
		for j in range(1,len(t)+1):
			d[i][j] = max(
						d[i-1][j-1],
						max(d[i-1][j], d[i][j-1])
					)
			d[i][j] = d[i-1][j-1]
			if s[i-1] == t[j-1]:
				d[i][j]+=1
				#if (i>=2 and j>=2 and (s[i-2]==s[i-1] and t[j-2]==t[j-1]) or (s[i-2]!=s[i-1] and t[j-2]!=t[j-1]) ) or (i==1 or j==1):
				#	d[i][j] += 1
			else:
				d[i][j] = max(
						d[i-1][j-1],
						max(d[i-1][j], d[i][j-1])
					)
			
			d[i][j] = min(i, min(j, d[i][j]))

	"""for i in range(0, len(s)+1):
		for j in range(0, len(t)+1):
			print(d[i][j], end="")
		print()"""
	return d[len(s)][len(t)]

def lcs2(a, b):
	#write your code here
	return edit_distance_long_sub_seq(a, b)

if __name__ == '__main__':

	input()
	a = list(map(int, input().split()))
	input()
	b = list(map(int, input().split()))

	print(lcs2(a, b))
