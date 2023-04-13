N, M = map(int, input().split())

PointList = []

for i in range(M):
    A, B = map(int, input().split())
    PointList.append([A, B])

for i in range(M):
    if PointList > N:

