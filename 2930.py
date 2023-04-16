from collections import Counter

R = int(input())
S_List = str(input())
N = int(input())
F_List = []

val_1 = 0
val_2 = 0

FT_List = []
New_S_List = []

def now_score(A, B):
    score = 0
    if A == "S":
        if B == "P":
            score = 2
        elif B == "S":
            score = 1
        else:
            score = 0
    if A == "P":
        if B == "R":
            score = 2
        elif B == "P":
            score = 1
        else:
            score = 0
    if A == "R":
        if B == "P":
            score = 0
        elif B == "R":
            score = 1
        else:
            score = 2
    return score

for i in range(N):
    tmp = []
    strr = str(input())
    for j in range(R):
        tmp.append(strr[j])
    F_List.append(tmp)

def win(val):
    if val == "S":
        return "R"
    elif val == "P":
        return "S"
    elif val == "R":
        return "P"


# 친구들의 라운드별로 모아놓는 이중리스트

for j in range(R):
    tmp_list = []
    for i in range(N):
        tmp_list.append(F_List[i][j])
    FT_List.append(tmp_list)

# 상근이가 뭘 내야할지 알려주는 리스트


# 출력 1
for i in range(N):
    for j in range(R):
        val_1 += now_score(S_List[j], F_List[i][j])

print(val_1)