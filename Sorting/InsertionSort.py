n = int(input('Enter the number of elements: '))

arr = []

for i  in xrange(1,n+1):
	arr.append(int(input('Enter the value: ')))

def InsertionSort(data):
	for j in range(1,n):
		key = data[j]
		i = j - 1
		while data[i] > key and i >= 0:
			data[i+1] = data[i]
			i = i-1

		data[i+1] = key
	return data

print(InsertionSort(arr))