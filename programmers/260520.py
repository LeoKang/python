def solution(numbers):
    def get_sum(arr):
        if not arr:
            return 0
        return arr[0] + get_sum(arr[1:])

    total_sum = get_sum(numbers)
    return total_sum / len(numbers)

# 1. --------------------------------

def solution(numbers):
    answer = 0

    for i in numbers:
        answer += i

    return answer / len(numbers)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(solution(numbers1))