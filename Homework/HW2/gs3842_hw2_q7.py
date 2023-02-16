def findChange(lst01):
    left = 0
    right = len(lst01) - 1

    while left < right:
        midpoint = (left + right) // 2

        if lst01[midpoint - 1] == 0 and lst01[midpoint] == 1:
            return midpoint
        elif lst01[midpoint] == 0 and lst01[midpoint + 1] == 1:
            return midpoint + 1
        elif lst01[midpoint] == 0:
            left = midpoint + 1
        elif lst01[midpoint - 1] == 1:
            right = midpoint - 1
