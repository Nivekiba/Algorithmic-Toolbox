# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1, max2 = -1, -1
    tmp = -9999
    for i in range(n):
    	if tmp < numbers[i]:
    		max1 = i
    		tmp = numbers[i]
    tmp = -9999
    for i in range(n):
    	if i != max1 and tmp < numbers[i]:
    		max2 = i
    		tmp = numbers[i]

    return numbers[max1] * numbers[max2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
