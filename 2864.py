# 문제
# 상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.
# 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())

A_list = list(map(str,str(A)))
B_list = list(map(str,str(B)))

a_answer = ""
b_answer = ""

X = 0

def change(list, before, after) :
    answer = ""
    for idx, val in enumerate(list) :
        if val == before :
            list[idx] = after
        answer += list[idx]
    return int(answer)

print(change(A_list,"6","5") + change(B_list,"6","5"), change(A_list,"5","6") + change(B_list,"5","6"))



# for idx, val in enumerate(A_list) :
#     if val == "6" :
#         A_list[idx] = "5"
#     a_answer += A_list[idx]
# a_answer = int(a_answer)
#
# for idx, val in enumerate(B_list) :
#     if val == "6" :
#         B_list[idx] = "5"
#     b_answer += B_list[idx]
# b_answer = int(b_answer)
#
# X = a_answer + b_answer
#
# a_answer = ""
# b_answer = ""
#
# for idx, val in enumerate(A_list) :
#     if val == "5" :
#         A_list[idx] = "6"
#     a_answer += A_list[idx]
# a_answer = int(a_answer)
#
# for idx, val in enumerate(B_list) :
#     if val == "5" :
#         B_list[idx] = "6"
#     b_answer += B_list[idx]
# b_answer = int(b_answer)
#
# Y = a_answer + b_answer
#
# print(X, Y)