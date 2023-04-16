N, M = map(int, input().split())

PointList = []
count = 0
result = 0

for i in range(M):
    A, B = map(int, input().split())
    PointList.append([A, B])

PointList.sort(key=lambda x: -x[0])

for i in range(M):
    if PointList[i][0] >= N:
        count += 1

del PointList[:count]

if count >= M-1:
    print(0)
else:
    for i in range(len(PointList)):
        result += PointList[i][1]-N
        count += 1
        if count >= M-1:
            print(result)
            break

