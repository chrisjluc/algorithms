"""This module contains the closest pair of points algorithm - O(nlogn)
        References:
        http://en.wikipedia.org/wiki/Closest_pair_of_points_problem
"""


from heapq import heappush, heappop

def closest_pair_of_points(P):
    """
        P - set of points (x, y)
        Returns: set of closest pair of points
    """
    if len(P) < 2:
        raise ValueError('Must be at least 2 points')
    h = []
    for point in P:
        heappush(h, point)
    # Order by x-values
    P = [heappop(h) for i in range(len(h))]
    return closest_pair_in_subset(P)

def closest_pair_in_subset(P):
    """
        Divide and conquer, find the left-side and right-side min distance
        Find min distance among set of pairs of points which one point
        lies on the left and the other on the right.
        The minimum is between d_l, d_r, d_lr
    """
    if len(P) == 2:
        return P
    mid = len(P) / 2
    # Slice into even subsets
    left = P[:mid + len(P) % 2]
    right = P[mid:]
    # Divide and conquer
    p_l = closest_pair_in_subset(left)
    p_r = closest_pair_in_subset(right)
    # Min dist of both sides - p_min is the set of points with min distance
    d_min, p_min = (dist_pair(p_l), p_l) if dist_pair(p_l) < dist_pair(p_r) else (dist_pair(p_r), p_r)
    # Find candidate points with x < d_min from x_mid
    x_mid = P[mid]
    cand_left = [p for p in left if x_mid[0] - p[0] < d_min]
    # If odd, slice the last point in cand_left, it will be included in the right
    if len(P) % 2 == 1:
        cand_left = cand_left[:-1]
    # Compare min distances with those to the right
    for l in cand_left:
        for r in right:
            if r[0] - l[0] >= d_min:
                break
            if abs(r[1] - l[1]) >= d_min:
                continue
            d = dist(l, r)
            if d < d_min:
                d_min = d
                p_min = [l, r]
    return p_min

def dist(a, b):
    """
        Calculates Euclidean distance between points a and b
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def dist_pair(p):
    if len(p) is not 2:
        raise ValueError('Needs exactly 2 points')
    return dist(p[0], p[1])
