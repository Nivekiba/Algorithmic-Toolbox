# Uses python3
def edit_distance(s, t):
	# table that containing the values of edit distance continously for the 2 strings	
	d = []
	for i in range(len(s)+1):
		d.append([0]*(len(t)+1))
	
	for i in range(1,len(s)+1):
		d[i][0] = i
	for j in range(1,len(t)+1):
		d[0][j] = j
		
	for i in range(1,len(s)+1):
		for j in range(1,len(t)+1):
			if s[i-1] == t[j-1]:
				d[i][j] = min(
							d[i-1][j-1],
							min(d[i-1][j], d[i][j-1])+1
						)
			else:
				d[i][j] = min(
							d[i-1][j-1],
							min(d[i-1][j], d[i][j-1])
						)+1

	return d[len(s)][len(t)]

if __name__ == "__main__":
	print(edit_distance(input(), input()))
