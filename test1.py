from collections import defaultdict
from random import random
from heapq import nlargest
from collections import Counter, OrderedDict


def word_count(str):
    count = dict()
    word_list = str.split()

    for word in word_list:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print('Input paragraph:')
paragraph = input()

word_dict = word_count(paragraph)
c = Counter(word_dict)
r = OrderedDict(sorted(c.items(), key=lambda x: (-x[1], x[0])))
d = Counter(r)
for key, value in d.most_common(5):
    print(str(key) + " - " + str(value))

