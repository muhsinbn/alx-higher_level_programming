#!/usr/bin/python3
def weight_average(my_list=[]):

    """
    Returns the weighted average of all integers tuple (<score>, <weight>)
    ...

    Parameters
    ----------
    my_list : list
        list of tuples

    Return:
        the average
    """
    if my_list and len(my_list):
        num = 0
        dem = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            dem += tup[1]
        return (num / dem)
    return 0
