# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	
	d = dict()
	for i in range(len(weights)):
		d[i] = values[i]/weights[i]
		
	d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for e in d_sorted:
		ind, value_per_weight = e
		if weights[ind] <= capacity:
			value += weights[ind]*value_per_weight
			capacity -= weights[ind]
		else:
			value += capacity*value_per_weight
			break
	
	return value


if __name__ == "__main__":
	n, capacity = list(map(int, input().split()))
	values = []
	weights = []
	for i in range(n):
		v,w = list(map(int, input().split()))
		values.append(v)
		weights.append(w)
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))
