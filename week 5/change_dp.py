# Uses python3
import sys

def get_change(m):
	number_coins = [0]*(m+1)
	coins = [1, 3, 4]
	for i in range(1,m+1):
		curr_coins = 15**18
		for c in coins:
			if i >= c:
				curr_coins = min(number_coins[i-c]+1, curr_coins)
		number_coins[i] = curr_coins
	return number_coins[m]

if __name__ == '__main__':
	m = int(input())
	print(get_change(m))
