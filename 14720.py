N = int(input())
store = list(map(int, input().split()))
result = 0

# for i in range(N):
#     if store[i] == 0:
#         result += 1
#         print(result, i)
#         if i+1 < N:
#             if store[i+1] == 1:
#                 result += 1
#                 print(result, i)
#                 if i+2 < N:
#                     if store[i+2] == 2:
#                         result += 1
# print(result)

flag = 0
def count_next(flag):
    if flag < 2:
        flag += 1
    else:
        flag = 0
    return flag

for i in store:
    if i == flag:
        result += 1
        flag = count_next(flag)
print(result)