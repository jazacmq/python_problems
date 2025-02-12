def findMinDifference(timePoints):
    # Convert time to minutes
    minutes = sorted(int(tp[:2]) * 60 + int(tp[3:]) for tp in timePoints)

    min_diff = float("inf")

    # Compare adjacent times
    for i in range(len(minutes) - 1):
        min_diff = min(min_diff, minutes[i + 1] - minutes[i])

    # Compare last and first considering circular time
    min_diff = min(min_diff, (minutes[0] + 1440) - minutes[-1])

    return min_diff

# Example usage:
timePoints = ["23:59", "02:10", "12:30", "10:35","13:00"]
print(findMinDifference(timePoints))  # Output: 1
