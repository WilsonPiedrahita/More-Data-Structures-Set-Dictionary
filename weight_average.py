def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    weighted_sum = 0
    total_weight = 0

    for item in my_list:
        value, weight = item
        weighted_sum += value * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return weighted_sum / total_weight
