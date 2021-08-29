def groupAnagrams(strs):
    hp = {}
    res = []
    c = 0
    for i, s in enumerate(strs):
        ind = tuple(sorted(s))
        if ind not in hp:
            hp[ind] = c
            c += 1
            res.append([s])
        else:
            res[hp[ind]].append(s)
    return res
strs=list(input().split(","))
print(groupAnagrams(strs))