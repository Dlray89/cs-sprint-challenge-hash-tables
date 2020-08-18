
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #find sum of two items(i, x) = limit
    # return tuple
    # if no pair return none
    # Your code here
    item_dict = {}
    for i in range(length):
        if limit - weights[i] in item_dict:
            key = limit - weights[i]
            x = item_dict[key]
            print('i', i)
            print('x', x)
            return [i, x]
        item_dict[weights[i]] = i
        print('item_dict', item_dict)

    return None


weights = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights, 5, 21)