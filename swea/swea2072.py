N=int(input())
p=1
for _ in range(N):
    Y=list(map(int, input().split()))
    J=0
    for i in Y:
        if i%2!=0:
            J+=i
    print(f"#{p} {J}")
    p+=1
    
# 1. -------------------------

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lst = input().split()
    # print(lst)
    
    sum = 0
    for i in lst:
        # print(i, end=' ')
        if int(i)%2!=0:
            sum += int(i)

    print(f"#{test_case} {sum}")
    # ///////////////////////////////////////////////////////////////////////////////////