from collections import Counter


def sherlockAndAnagrams(s):
    buckets = {}
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            print(len(s) - i + 1)
            print(i, j, i+j)
            key = frozenset(Counter(s[i:i+j]).items())
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:

        count += buckets[key] * (buckets[key]-1) // 2
    return count


print(sherlockAndAnagrams('Madam'))
