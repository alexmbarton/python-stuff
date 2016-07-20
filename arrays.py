import sys

n = int(raw_input().strip())

arr = map(int,raw_input().strip().split(' '))


while (n > 0):
	print(arr[n - 1 ]),
	n = n - 1

