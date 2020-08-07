count = {}
matches = []
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    for lsts in arrays:
        for values in lsts:
            if values not in count:
                count[values] = 1
            else:
                count[values] += 1
        for value in count:
            if count[value] == len(arrays):
                matches.append(value)
    return matches

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
