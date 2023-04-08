T = int(input())
list1 = [25,10,5,1]
list2 = []

for i in range(T) :
    list2.append(int(input()))

for i in list2:
    for a in list1:
        result = i // a
        i = i % a
        print(result, end =" ")
    print()
