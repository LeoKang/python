def GetCategory(gender, age):
    table = [
        ['MAN', 'BOY'],  
        ['WOMAN', 'GIRL'] 
    ]
    
    g_idx = 0 if gender.upper() == 'M' else 1
    a_idx = 0 if age >= 20 else 1
    
    return table[g_idx][a_idx]

gen, age = input().split()
# print(gen, age)
print(GetCategory(gen, int(age)))
# 2. --------------------------------------
def info(gen,age):
    if (age >= 20) and gen in ["M" ,"m"]  :
        print("MAN")
    elif (age >= 20) and gen in ["F" ,"f"] :
        print("WOMAN")
    elif age <20 and gen in ["M" ,"m"]  :
        print("BOY")
    else:
        print("GIRL")

gen, age = input().split()

age=int(age)

info(gen, age)
# 1. -------------------------
def check_info(g, a):
    ret = ""
    if g.upper() == 'M':
        if a >= 20:
            ret = "MAN"
        else:
            ret = "BOY"
    else:
        if a >= 20:
            ret = "WOMAN"
        else:
            ret = "GIRL"
    return ret


gender, age = input().split()
print(gender, age)
print(check_info(gender, int(age)))