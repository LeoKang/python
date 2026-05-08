def solution(dots):
    
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])  
    
    A, B, C, D = dots
    
    if get_slope(A, B) == get_slope(C, D): return 1
    if get_slope(A, C) == get_slope(B, D): return 1
    if get_slope(A, D) == get_slope(B, C): return 1
    
    return 0

# 2. ----------------------------------------

def solution(dots):
    [a, b, c, d] = dots
    
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    if get_slope(a, b) == get_slope(c, d): return 1
    if get_slope(a, c) == get_slope(b, d): return 1
    if get_slope(a, d) == get_slope(b, c): return 1
    
    return 0



# 1. ------------------------------------------

# dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
def solution(dots):
    answer = 0

    mat = dots

    for a in range(len(mat)):
        for b in range(len(mat)):
            for c in range(len(mat)):
                for d in range(len(mat)):
                    if a != b and b != c and c != d and d!=a and a!=c and b!=d:
                        # print(a, b, c, d)
                        print((mat[b][0]- mat[a][0])**2 + (mat[b][1]- mat[a][1])**2)
                        print((mat[d][0]- mat[c][0])**2 + (mat[d][1]- mat[c][1])**2)

                        # if (((mat[b][0]- mat[a][0])**2 - (mat[b][1]- mat[a][1])**2) == ((mat[d][0]- mat[c][0])**2 - (mat[d][1]- mat[c][1])**2)):
                        #     print(f"[{a}, {b}, {c}, {d}]")
        print()

    return answer

solution(dots)