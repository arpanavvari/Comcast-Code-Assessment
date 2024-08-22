def fullycovered(ranges, left, right):
    """
    Given a 2D Array ranges, determine if all integers within the interval [left, right] 
    are covered by at least one of the intervals in the list of ranges.

    Args:
        ranges (list of lists): A list of intervals [start, end].
        left (int): The left boundary of the target interval.
        right (int): The right boundary of the target interval.

    Returns:
        bool: True if every integer from left to right is covered by at least one range, False otherwise.
    """

    try:
        # Iterate over each integer in the interval [left, right]
        for i in range(left, right + 1):
            covered = False

            # Check if the integer i is covered by any of the ranges
            for start, end in ranges:
                if start <= i <= end:
                    covered = True
                    break

            # If any integer in the interval [left, right] is not covered, return False
            if not covered:
                return False

        # If all integers are covered, return True
        return True

    except TypeError as e:
        print(f"TypeError encountered: {e}")
        return False  # Return False or Can add a friendly message

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False  # Return False or add to a error logger


# Example 1
ranges_1 = [[1, 2], [3, 4], [5, 6]]
left_1 = 2
right_1 = 5
output_1 = fullycovered(ranges_1, left_1, right_1)

# Example 2
ranges_2 = [[1, 10], [10, 20]]
left_2 = 21
right_2 = 21
output_2 = fullycovered(ranges_2, left_2, right_2)

print(output_1, output_2)
