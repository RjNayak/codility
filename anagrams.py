
from collections import Counter


def count_anagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items())
            # print(key)
            # print(buckets.get(key, 0) + 1)
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    print(buckets)
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count


if __name__ == '__main__':
    print(count_anagrams('abba'))
