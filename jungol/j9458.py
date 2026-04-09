def check_number(n):
    mapping = {
        (n > 0): 'positive',
        (n < 0): 'negative',
        (n == 0): 'zero'
    }
    return mapping[True]

num = int(input())
# print(num)
print(check_number(num))
# 1.--------------------------
inp = int(input())
# print(inp)

def get_integer(p):
    ret = ""
    if p>0:
        ret = "positive"
    elif p<0:
        ret = "negative"
    else:
        ret = "zero"

    return ret

r = get_integer(inp)
print(r)