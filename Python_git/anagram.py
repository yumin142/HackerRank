def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = s[:int(len(s)/2)]
        s2 = s[int(len(s)/2):]
    
    d1 = {i: s1.count(i) for i in s1}
    d2 = {i: s2.count(i) for i in s2}
    diff = 0
    for i in d1:
        if i in d1 and i in d2:
            diff += max(0, d1[i] - d2[i])
        else:
            diff += d1[i]
    
    return diff