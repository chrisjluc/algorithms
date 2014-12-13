from heapq import *

def heap_sort_lazy(a):
	"""
	Create a min heap using heapq library 
	and popping the elements using list comprehension.

	@return sorted_list 
	"""
	h = []
	for value in a:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

def merge_sort_recursive(a):
	"""
	Recursively divide the unsorted lists into sublists each containing 1 element
	and repeatedly merge sublists to produce new sublists.

	@return sorted_list 
	"""
	length = len(a)
	if length == 1:
		return a
	left = merge_sort_recursive(a[0:length/2])
	right = merge_sort_recursive(a[length/2:length])
	for i in xrange(0, length):
		if len(left) == 0:
			a[i] = right[0]
			right = right[1:len(right)]
		elif len(right) == 0:
			a[i] = left[0]
			left = left[1:len(left)]
		elif left[0] < right[0]:
			a[i] = left[0]
			left = left[1:len(left)]
		else:
			a[i] = right[0]
			right = right[1:len(right)]
	return a

def merge_sort_iterative(a):
	"""
	Divide the unsorted lists into sublists each containing 1 element
	and repeatedly merge sublists to produce new sublists.

	@return sorted_list 
	"""
	length = len(a)
	i = 1
	while i <= length:
		for j in xrange(i, length, 2 * i):
			a = merge(a, j - i, j, min(j + i, length))
		i *= 2
	return a

def merge(a, start, middle, end):
	"""
	Merges 2 sublists

	@return sorted_sublist
	"""
	l = r = 0
	merged = []
	while l < middle - start and r < end - middle:
		if a[start + l] < a[middle + r]:
			merged.append(a[start + l])
			l+=1
		else:
			merged.append(a[middle + r])
			r += 1
	while l < middle - start:
		merged.append(a[start + l])
		l += 1
	while r < end - middle:
		merged.append(a[middle + r])
		r += 1
	return a[0:start] + merged + a[end:len(a)]

def quick_sort(a, low, high):
	"""
	Pick an element, called a pivot.
	Reorder the array so that all elements with 
	values less than the pivot come before the pivot,
	while all elements with values greater than the pivot come after it.
	After this partitioning, the pivot is in its final position.
	Recursively apply the above steps to the sub-array of elements with smaller 
	values and separately to the sub-array of elements with greater values.

	@return sorted_list
	"""
 	if low < high:
 		pivot = partition(a, low, high)
 		quick_sort(a, low, pivot - 1)
 		quick_sort(a, pivot + 1, high)
 	return a

def partition(a, low, high):
	"""
	pVal = pivot value
	pIndex keeps of track of where the pivot has to be placed.
	Make sure all the elements < pVal are place left of pIndex and elements > pVal are right of it

	Choose the half way point as the pivot and move it to the last position.
	Iterate through each element and keep track of the number of elements < pivot value

	@return pivot_index
	"""
	pIndex = (low + high)/2
	pVal = a[pIndex]
	swap(a, pIndex, high)
	pIndex = low
	for i in xrange(low, high):
		if a[i] < pVal:
			swap(a, i, pIndex)
			pIndex += 1
	swap(a, pIndex, high)
	return pIndex

def swap(a, i, j):
	"""
	swap elements at index i and j of array a
	"""
	if i == j:
		return
	temp = a[i]
	a[i] = a[j]
	a[j] = temp