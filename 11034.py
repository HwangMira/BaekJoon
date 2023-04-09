i = 1
while True:
    try:
        A,B,C = map(int, input().split())
        # if B-A < C-B:
        #     result = C-B-1
        # else:
        #     result = B-A-1
        result = max(B-A, C-B) - 1
        print(result)
    except:
        break