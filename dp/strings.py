def longest_common_substring(a, b):
    """
        Returns length of longest common substring
    """
    length = 0
    c = [[0 for x in range(len(b))] for x in range(len(a))] 
    for i in xrange(0, len(a)):
        for j in xrange(0, len(b)):
            if a[i] is b[j]:
                if i > 0 and j > 0:
                    c[i][j] = c[i - 1][j - 1] + 1
                    length = c[i][j] if c[i][j] > length else length
                else:
                    c[i][j] = 1
            else:
                c[i][j] = 0
    return length
    
def longest_common_subsequence(a, b):
    """
        Returns length of longest common subsequence
    """
    length = 0
    c = [[0 for x in range(len(b))] for x in range(len(a))] 
    for i in xrange(0, len(a)):
        for j in xrange(0, len(b)):
            if a[i] is b[j]:
                if i > 0 and j > 0:
                    c[i][j] = c[i - 1][j - 1] + 1
                    length = c[i][j] if c[i][j] > length else length
                else:
                    c[i][j] = 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return length


