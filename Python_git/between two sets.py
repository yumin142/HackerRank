def getTotalX(a, b):
    # Write your code here
    aa = [i for i in range(max(a), min(b)+1) if all([(i % x) == 0 for x in a])]
    bb = [i for i in aa if all([(y % i) == 0 for y in b])]
    return len(bb)