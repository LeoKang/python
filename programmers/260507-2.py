#프로그래머스-코딩테스트 연습-코딩테스트 입문 - 문자열 정렬하기(1)

function solution(my_string) {
    return my_string.match(/\d/g).map(Number).sort((a, b) => a - b);
}

# 2. ---------------------------------

def solution(my_string):
    numbers = []
    for char in my_string:
        if '0' <= char <= '9':  
            numbers.append(int(char))
    
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# 1. -------------------------------

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))

    answer.sort()
    return answer

my_string1 = "hi12392"
my_string2 = "p2o4i8gj2"

print(solution(my_string1))
print(solution(my_string2))