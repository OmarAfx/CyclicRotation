def solution(A, K):
    N = len(A)

    # An empty list has nothing to rotate, and A[N - 1] below would crash
    if N == 0:
        return A

    # One rotation moves everything right by one, so repeat it K times
    for step in range(K):
        # Save the last element first, because the shifting below overwrites it
        last = A[N - 1]

        # Shift every element one spot to the right.
        # Go from the END backwards so each value is copied before it gets overwritten.
        i = N - 1
        while i > 0:
            A[i] = A[i - 1]
            i = i - 1

        # The old last element wraps around to the front
        A[0] = last

    return A