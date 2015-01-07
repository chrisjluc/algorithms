"""
This module contains the following dp algorithms associated with sequences of elements:
    - Longest Common Substring - O(mn)
    - Longest Common Subsequences - O(mn)
    - Levenshtein distance - O(mn)

References:
http://en.wikipedia.org/wiki/Longest_common_substring_problem
http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://en.wikipedia.org/wiki/Levenshtein_distance
"""

def longest_common_substring(a, b):
    """
        Returns set of longest common substrings
        which is a sequence of common elements that occupy consecutive positions.
        Iterate through the strings and
        assigns the length of current LC substring if the current letters match.
        Look back a diagonal to check if the letters before it matched

        c is a 2d array that holds the length of a LC substring up to that point
        z holds the longest length for the LC substring
    """
    ret = set()
    z = 0
    # Init with zeros
    c = [[0 for x in range(len(b))] for x in range(len(a))]
    for i in xrange(0, len(a)):
        for j in xrange(0, len(b)):
            if a[i] is b[j]:
                if i > 0 and j > 0:
                    # Extend current sequence
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    #First row or first column means this is the first match
                    c[i][j] = 1

            if c[i][j] > z:
                # Create a new set because a new longest substring is found
                ret = set()
                ret.add((i, j))
                z = c[i][j]
            elif c[i][j] is z:
                # Append to set because this is also a longest common substring
                ret.add((i, j))

    # Use the ending location to build the substrings in reverse
    substrings = set()
    for location in ret:
        substring = ''
        for i in xrange(0, z):
            substring += a[location[0] + 1 + i - z]
        substrings.add(substring)
    return substrings


def longest_common_subsequence(a, b):
    """
        Returns set of longest common subsequences.
        Subsequences are not required to occupy consecutive positions.
        When iterating, if elements are equal, the sequence is extended by that element
        If they're not equal the sequence is the same as previously found sequences

        c is a 2d array that holds the length of a LC subsequence up to that point of string a and b
        z holds the longest length for the LC subsequence
    """
    if len(a) <= 0 or len(b) <= 0:
        return set()
    z = 0
    c = [[0 for x in range(len(b))] for x in range(len(a))]
    for i in xrange(0, len(a)):
        for j in xrange(0, len(b)):
            if a[i] is b[j]:
                if i > 0 and j > 0:
                    c[i][j] = c[i - 1][j - 1] + 1
                else:
                    c[i][j] = 1
            else:
                # Find the previous longest subsequence
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

            if c[i][j] > z:
                z = c[i][j]
    return backtrack(a, b, c, len(a) - 1, len(b) - 1)

def backtrack(a, b, c, i, j):
    """
        Starts at the last index in the matrix and recursively builds a set of
        longest common subsequences
    """
    if i is 0 or j is 0:
        if a[i] is b[j]:
            # This is the first matching element in the sequence
            return set([a[i]])
        elif c[i][j] is 0:
            # No matching elements before this
            return set([''])
        elif j > 0:
            # Find the first matching element
            return backtrack(a, b, c, i, j - 1)
        else:
            return backtrack(a, b, c, i - 1, j)
    elif a[i] is b[j]:
        # Append the matching element to the LC Subsequences
        return set([z + a[i] for z in backtrack(a, b, c, i - 1, j - 1)])
    else:
        # Find the previously LC Subsequences
        r = set()
        if c[i][j - 1] >= c[i - 1][j]:
            r = backtrack(a, b, c, i, j - 1)
        if c[i - 1][j] >= c[i][j - 1]:
            r = r | backtrack(a, b, c, i -1, j)
        return r

def levenshtein_distance(a, b):
    """Calculates the edit distance between two strings a and b. The edit distance is defined
    as the minimum cost required to transform string a into string b. Operations permitted are
    deletion, addition, and replacing of characters.
    """
    # If either string is empty, we must delete all characters from the other one.
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    # Create the matrix where dp[i][j] represents the levenshtein distance of the string
    # prefixes a[0..(i-1)] and b[0..(j-1)].
    dp = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]

    # You can create the empty string by deleting all characters.
    for i in xrange(1, len(a) + 1):
        dp[i][0] = i
    for j in xrange(1, len(b) + 1):
        dp[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            dp[i][j] = min (
                # Consider replacement of a character.
                dp[i - 1][j - 1] + (a[i - 1] != b[j - 1]),

                # Consider insertions and deletions.
                min (
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1
                )
            )

    return dp[len(a)][len(b)]
