# Enter your code here. Read input from STDIN. Print output to STDOUT


# k, m = [int(x) for x in input().split()]

# table = []
# for i in range(k):
#     table.append([int(x) for x in input().split()])

# print(table)
# print(table**2)

# list = []
# i=0, j=1

# for a in range(k):
#     sum += (table[i][j])**2
#     i += 1
#     when i == k:
#         list.append(sum % m)
#         sum == 0

import itertools

k, m = [int(x) for x in input().split()]
table = []
for i in range(k):
    array = input().split()
    table.append([int(x)**2 for x in array[1:]])

print([x for x in itertools.product(*table)])
print(max(sum(x)%m for x in itertools.product(*table)))