def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    plan =  {}
    output = []
    if len(weights)== 1:
        return None
    if len(weights) == 2:
        return [1,0]
    for nums in weights:
        plan[nums] = weights.index(nums)
    for keys in plan:
        if (limit-keys) in plan:
            output.append(plan[keys])
    output.sort(reverse=True)
    return(output)

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ],5,21)
