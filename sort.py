def most_common(lst):
    return max(set(lst), key=lst.count)

print(most_common([1,2,34,5,43,2,1]))
