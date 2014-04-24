# Computes the longest increasing subsequence of an array of numbers.
# Does this recursively and with DP.
#
# The longest increasing subsequence problem is to find the longest
# subsequence of a given sequence (not necessarily contiguous), such that
# all the elements of the subsequence are in increasing order.
#
# For example, the length of the LIS of [10, 22, 9, 33, 21, 50, 41, 60, 80] is 
# 6, and the subsequence is [10, 22, 33, 50, 60, 80].

# Recursively computes the length of the LIS.
# Note that the LIS of arr[0..n] is the longer of:
#     - the LIS of arr[1..n]
#     - arr[0] followed by the LIS of arr[1..n], with elements greater than arr[0]
# This recursion follows that rule.
#
# This runs in O(2^n).
def lis(prev, arr):
	L = len(arr)
	if L == 0:
		return 0
	else:
		m = lis(prev, arr[1:])
		if arr[0] > prev:
			m = max(m, 1 + lis(arr[0], arr[1:]))

		return m

# Uses DP.
# Let L[i] be the longest increasing subsequence ending at arr[i].
# For all j such that j < i and arr[j] < arr[i], find the largest L[j] and set L[i] to one plus it.
#
# This runs in O(n^2) and uses O(n) additional space.
def lisdp(arr):
	n = len(arr)
	L = [1]*n

	for i in range(n):
		for j in range(i):
			if (arr[j] < arr[i] and L[i] <= L[j]):
				L[i] = L[j] + 1

	return max(L)

"""
print "LIS of [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]:"
print "Recursion (2^n):" + repr(lis(-1000000, [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print "DP (n^2): " + repr(lisdp([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print "DP (nlogn): "
"""