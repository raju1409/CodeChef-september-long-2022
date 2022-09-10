# cook your dish here
from collections import Counter
for i in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    counts = Counter(arr1)
    arr = [id for id in arr1 if counts[id] > 1]
    sets = list(set(arr))
    count = 0
    for i in sets:
        if arr.count(i)>1:
            val = arr.count(i)
            count += (val * (val - 1)) // 2
    print(count)
