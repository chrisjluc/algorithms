"""This module contains the following convex hull algorithms:
    - Gift wrapping algorithm (Jarvis March) - O(n^2)

Given a list of points, the convex hull of a set of points S is the smallest
convex set that contains X. A convex hull can be visualized as the shape formed
when an elastic band is stretched around S.

References:
http://en.wikipedia.org/wiki/Convex_hull
http://en.wikipedia.org/wiki/Convex_hull_algorithms
"""


def gift_wrapping_2d(points):
    """Computes the convex hull of a list of tuples (points) in O(n^2). This is
    also called the Jarvis March and it is the simplest of the convex hull algorithms.

    @param points - List of tuples for the points in the set.
    @return hull - List of tuples for the points on the convex hull.
    """

    if not points:
        return []

    def _turn_direction(a, b, c):
        """Returns the turn direction of the joint a, b, c. This returns 1 if it's
        a right turn, 0 if it's a straight line, or -1 if it's a left turn.
        """

        turn_val = (b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0])*(b[1] - a[1])
        return -1 * cmp(turn_val, 0)

    def _dist(a, b):
        """Returns the square of the euclidean distance between points a and b.
        """
        return (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])

    hull = [min(points)]

    for pt in hull:
        # Find the next point in the hull (find the point that corresponds to the
        # largest turn angle (see http://tinyurl.com/qc4dnae).
        cur = pt
        for next_pt in points:
            turn = _turn_direction(pt, cur, next_pt)
            if turn == -1 or (turn == 0 and _dist(pt, next_pt) > _dist(pt, cur)):
                cur = next_pt

        if cur == hull[0]:
            break;
        hull.append(cur)

    return hull