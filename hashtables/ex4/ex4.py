# Setup a dictionary where the pos number is the key then the value is negative key return the key

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    posititive_values = {}
    pairs = []
    for nums in a:
        if abs(nums) not in posititive_values:
            posititive_values[abs(nums)] = 1
        else:
            posititive_values[abs(nums)] += 1
    for values in posititive_values:
        if posititive_values[values] == 2:
            pairs.append(values)
    return pairs

if __name__ == "__main__":
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
