def sum_pairs(lst, tgt):
    i = 0
    while i < len(lst) - 1:
        j = i + 1
        while j < len(lst):
            res = lst[i] + lst[j]
            if res == tgt:
                return [lst[i], lst[j]]
            j += 1
        i += 1
    return []


assert sum_pairs([4,2,10,5,1], 6) == [4,2]
assert sum_pairs([11,20,4,2,1,5], 100) == []

print('All tests OK')
