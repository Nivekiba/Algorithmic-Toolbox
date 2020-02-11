#Uses python3

import sys

# Uses python3
def edit_distance_long_sub_seq(s, t, u):
	n, m = len(s), len(t)
	# table that containing the values of edit distance continously for the 2 sequences	
	d = []
	for i in range(len(s)+1):
		p = []
		for j in range(len(t)+1):
			p.append([0]*(len(u)+1))
		d.append(p)
		
	for i in range(1,len(s)+1):
		for j in range(1,len(t)+1):
			for k in range(1, len(u)+1):
				"""d[i][j][k] = max(
								d[i-1][j-1][k-1],
								max(
									d[i-1][j][k], 
									max(
										d[i][j-1][k],
										d[i][j][k-1]
									)
								)
							)"""
				d[i][j][k] = d[i-1][j-1][k-1]
				if s[i-1] == t[j-1] == u[k-1]:
					d[i][j][k]+=1
					#if (i>=2 and j>=2 and (s[i-2]==s[i-1] and t[j-2]==t[j-1]) or (s[i-2]!=s[i-1] and t[j-2]!=t[j-1]) ) or (i==1 or j==1):
					#	d[i][j] += 1
				else:
					d[i][j][k] = max(
								d[i-1][j-1][k-1],
								max(
									d[i-1][j][k], 
									max(
										d[i][j-1][k],
										d[i][j][k-1]
									)
								)
							)
				
				d[i][j][k] = min(i, min(j, min(k, d[i][j][k])))

	"""for i in range(0, len(s)+1):
		for j in range(0, len(t)+1):
			print(d[i][j], end="")
		print()"""
	return d[len(s)][len(t)][len(u)]

def lcs3(a, b, c):
	#write your code here
	return edit_distance_long_sub_seq(a, b, c)

if __name__ == '__main__':

	input()
	a = list(map(int, input().split()))
	input()
	b = list(map(int, input().split()))
	input()
	c = list(map(int, input().split()))

	print(lcs3(a, b, c))
