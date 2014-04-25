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