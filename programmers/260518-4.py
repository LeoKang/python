def solution(before, after):
    unique_chars = set(before)

    for char in unique_chars:
        if before.count(char) != after.count(char):
            return 0

    return 1

# 3. -------------------------------

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0 

# 2. -------------------------------

def solution(before, after):
    return int(sorted(before) == sorted(after))

    # 1. ---------------------------

def solution(before, after):
    bsort = "".join(sorted(before))
    asort = "".join(sorted(after))

    if bsort == asort:
        answer = 1
    else:
        answer = 0
    
    return answer

before1 = "olleh"
after1 = "hello"

before2 = "allpe"
after2 = "apple"
print(solution(before1, after1))
print(solution(before2, after2))