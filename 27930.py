S = str(input())
Slist = list(S)


K = ['K','O','R','E','A']
Y = ['Y','O','N','S','E','I']

for idx, val in enumerate(Slist):
    if val in K:
        K.remove(val)
        if len(K) == 0:
            print("KOREA")
            break
    if val in Y:
        Y.remove(val)
        if len(Y) == 0:
            print("YONSEI")
            break




