def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    values = {}
    result = []
    for i in arrays:
        for j in i:
            if j in values:
                values[j] += 1
                if values[j] == len(arrays):
                    result.append(j)
            else:
                values[j] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
