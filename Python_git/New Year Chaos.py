q = [1,2,5,3,7,8,6,4]
# q = [2,1,5,3,4]

### ONEE
# for i in range(1,len(q)+1):
#     print(q.index(i)+1)
# d = {}
# for i in q:
#     d[i] = q.index(i)+1
    
# print(d)

# b = 0

# for i in d:
#     if d[i] < i:
#         b = max(b, i-d[i])
        
# print(b)


### TWOOO
    # total = 0
    # for i in range(len(q)):
        # c = 0
        # for j in q[i+1:]:
            # if j < q[i]:
                # c += 1
        # if c > 2:
            # print("Too chaotic")
            # return
        # else:
            # total += c
    # print(total)


### THREEE
# total = 0
# for i in range(len(q)):
#     c = sum([1 for x in q[i+1:] if x < q[i]])
#     q.pop(q.index(i))
#     if c > 2:
#         print("Too chaotic")
#     total += c
# print(total)


### FOURR
# total = 0
# for i in range(len(q),0,-1):
#     c = sum([1 for x in q[q.index(i)+1:] if x < i])
#     q.pop(q.index(i))
#     if c > 2:
#         print("Too chaotic")
#         return
#     total += c
# print(total)


### FIVEEE
# total = 0
# m=q.index(1)
# for i in range(2,len(q)+1):
#     print("i=",i)
#     if q.index(i) < m:
#         c = sum([1 for x in q[q.index(i)+1:] if x < i])
#         print("c=",c)
#         if c > 2:
#             print("Too chaotic")
#         total += c
#         print("total=",total)
#     else:
#         m = max(m,q.index(i))
# print(total)


### POIM1
total = 0
for i in range(len(q)):
    c = sum(k < q[i] for k in q[i+1:])
    if c > 2:
        print("Too chaotic")
        break
    total += c
print(total)


### SIXXXX
# total = 0
# for i in range(len(q)-1,0,-1):
#     print("i=",i)
#     if q[i-1] > q[i]:
#         c = sum([1 for x in q[i:] if x < q[i-1]])
#         print("c=",c)
#         if c > 2:
#             print("Too chaotic")
#         total += c
#         print("total=",total)
# print(total)
        
    

                