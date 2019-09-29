def count_positives_sum_negatives(arr):
    if not arr: return []
    p=0
    n=0
    for x in arr:
        if x>0:
            p+=1
        if x<0:
            n+=x
    return [p, n]