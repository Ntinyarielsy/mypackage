def top_n(items, n):
    """ returns top n items in a descending order

    :param items:list or array like-object
    :param n: (int) the number of items to be returned
    :return:(array) to n items in descending order
    e.g: top_n([6,5,10,62,19],3)
              [62,19,10]
    """

    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    top_n = items[-n:]

    return top_n[::-1]


