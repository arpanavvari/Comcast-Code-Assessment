def isCovered(ranges, left, right):
    for i in range(left, right + 1):
        covered = False
        for start, end in ranges:
            if start <= i <= end:
                covered = True
                break
        if not covered:
            return False
    return True

# Example 1
ranges_1 = [[1, 2], [3, 4], [5, 6]]
left_1 = 2
right_1 = 5
output_1 = isCovered(ranges_1, left_1, right_1)

# Example 2
ranges_2 = [[1, 10], [10, 20]]
left_2 = 22
right_2 = 22
output_2 = isCovered(ranges_2, left_2, right_2)

print(output_1, output_2)

