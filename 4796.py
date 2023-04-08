# 문제
# 캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있다.
# 강산이는 이제 막 28일 휴가를 시작했다. 이번 휴가 기간동안 강산이는 캠핑장을 며칠동안 사용할 수 있을까?
# 연속하는 P일 중, L일 동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다.
# 강산이는 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)
# 입력
# L, P, V 순서대로 포함한다. 모든 입력 정수는 int 범위 마지막 줄에는 0이 3개 주어진다.
# 출력
# Case 1 : 14

list1 = []

while True :
    result = 0
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0 :
        break
    A = V // P
    result = A * L
    B = V % P
    if B <= L :
        result += B
    else :
        result += L
    # A = V // P
    # B = V % P
    #
    # result = A * L
    # if B <= L:
    #     result += B
    # else:
    #     result += L
    list1.append(str(result))
for idx, val in enumerate(list1) :
    print("Case " + str(idx+1) + ": " + str(val))