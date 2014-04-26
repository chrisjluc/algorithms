"""This module contains the following string searching algorithms. These are algorithms that 
find all occurences of a pattern in a body of text.
    - Naive search - O(n*m), with n as the length of the text and m is the length of the pattern.
    - Rabin-Karp - O(n+m) average, O(n*m) worst case
    - Knuth-Morris-Pratt - O(n)

References:
http://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=stringSearching
http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
"""

# Do all hashing in mod 1000000007 to avoid large numbers.
PRIME_MOD = 1000000007

def naive_search (text, pattern):
    """The naive string search algorithm, which is generally usable in most cases. For
    large inputs, the other algorithms are much more performant.

    @param text - The text to search in.
    @param pattern - The pattern to search for in the text.
    @return indices - An array of indices in the text where the pattern begins.
    """
    n, m = len(text), len(pattern)
    indices = []
    for i in range(n - m + 1):
        if pattern == text[i:i+m]:
            indices.append(i)
            
    return indices

def rabin_karp (text, pattern, base=256):
    """The Rabin-Karp algorithm for string searching. Uses a 'rolling hash' to search for
    the pattern. This algorithm works well for most input cases, with an average running time
    of O(n+m), however the worst case is O(n*m).

    @param text - The text to search in.
    @param pattern - The pattern to search for in the text.
    @param base - The base to use for hashing (defaults to 256).
    @return indices - An array of indices in the text where the pattern begins.
    """
    n, m = len(text), len(pattern)
    indices = []
    ht, hp = _hash_base(text[:m], base), _hash_base(pattern, base)

    for i in range(n-m+1):
        if ht == hp:
            if text[i:i+m] == pattern:
                indices.append(i)

        # Subtract out the hash contribution from the first character, and add the next one on.
        # This computes the substring hashes by "rolling" through.
        if i < n - m:
            ht = (base * (ht - (ord(text[i]) * (base ** (m-1)))))
            if ht > PRIME_MOD:
                ht %= PRIME_MOD

            ht += ord(text[i+m])
            if ht > PRIME_MOD:
                ht %= PRIME_MOD

    return indices

def knuth_morris_pratt (text, pattern):
    """Implementation of the Knuth-Morris-Pratt algorithm for string searching. This involves
    observing that the pattern has enough information in itself to determine where the next match
    could possibly begin, allowing us to skip some characters. See the wiki page for more info.

    @param text - The text to search in.
    @param pattern - The pattern to search for in the text.
    @return indices - An array of indices in the text where the pattern begins.
    """
    n, m = len(text), len(pattern)
    indices = []

    LPS = _compute_LPS_array(pattern)
    i, j = 0, 0
    while i < n:
        if pattern[j] == text[i]:
            j += 1
            i += 1

        if j == m:
            indices.append(i-j)
            j = LPS[j-1]
        elif pattern[j] != text[i]:
            if j != 0:
                j = LPS[j-1]
            else:
                i += 1

    return indices

def _compute_LPS_array (pattern):
    """Computes an array such that for each pattern[0:i], LPS[i] is the length of the longest
    proper prefix which is also a suffix of the string.

    @param pattern - Input string.
    @return LPS[] - The LPS array of the string.
    """
    L = len(pattern)
    LPS = [0]*L

    # Prev is the previous longest prefix suffix.
    i, prev = 1, 0

    while i < L:
        if pattern[i] == pattern[prev]:
            prev += 1
            LPS[i] = prev
            i += 1
        else:
            if prev != 0:
                prev = LPS[prev-1]
            else:
                LPS[i] = 0
                i += 1

    return LPS

def _hash_base (text, base):
    """Hash function for a string using a given base.

    @param text - The text to hash.
    @param base - The base to hash the text with.
    @return ret - The hash value.
    """
    ret = 0
    L = len(text)
    power = L - 1

    for i in range(L):
        ret += (ord(text[i]) * (base ** power))
        if ret > PRIME_MOD:
            ret %= PRIME_MOD
        power -= 1

    return ret % PRIME_MOD if ret > PRIME_MOD else ret