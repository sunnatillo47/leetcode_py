a = int(input('a: '))
b = int(input('b: '))

def func(a, b):
	arr = []
	for n in range(a, 0, -1):
		if b % n == 0 and a % n == 0:
			arr.append(n)

	print(arr[0])

func(a, b)