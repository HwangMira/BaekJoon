A, B, C, M = map(int, input().split())
P = 0
W = 0

for i in range(24):
    if P+A <= M :
        P += A
        W += B
    else :
        P -= C
        if P < 0:
            P = 0
print(W)