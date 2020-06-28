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

c = ChainMap(adjustment, baseline)

d = c.new_child()
e = c.new_child()


cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)