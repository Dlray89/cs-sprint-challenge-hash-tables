def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    values = {}
    result = []

    for i in a:
        if abs(i) in values:
            values[abs(i)] += 1
            if values[abs(i)] > 1 and abs(i) not in result:
                result.append(abs(i))
            else:
                values[abs(i)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
