# 타로는 자주 JOI잡화점에서 물건을 산다.
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
# 타로가 JOI 잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
# 입력 : 입력은 한 줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져 있다.
# 출력 : 제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.

n = int(input())
result = 0
jandon = 0
n = 1000-n

list = [500,100,50,10,5,1]

for i in list :
    if n > 0:
        result += n // i
        n = n % i
    else :
        break
print(result)


# if n > 0:
#     result = n // 500
#     jandon = n % 500
#     print(result, jandon)
#     if jandon > 0:
#         print(result, jandon)
#         result += jandon // 100
#         jandon = n % 100
#         print(result)
#         if jandon > 0:
#             result += jandon // 50
#             jandon = jandon % 50
#             print(result)
#             if jandon > 0:
#                 result += jandon // 10
#                 jandon = jandon % 10
#                 print(result)
#                 if jandon > 0:
#                     result += jandon // 5
#                     jandon = jandon % 5
#                     print(result)
#                     if jandon > 0:
#                         result += jandon
#                         print(result)