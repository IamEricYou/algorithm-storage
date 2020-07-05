from collections import ChainMap
from collections import Counter

baseline = {
    'music': 'bach',
    'art': 'rembrandt'
}

adjustment = {
    'art': 'van gogh',
    'opera': 'carmen'
}

# c = ChainMap(adjustment, baseline)
#
# d = c.new_child()
# e = c.new_child()
#
#
# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
#
# print(cnt)


def most_frequent_count(li):
    return max(set(li), key=li.count)


if __name__ == '__main__':
    temp = [10, 20, 10, 40, 40, 40, 50]
    print(most_frequent_count(temp))