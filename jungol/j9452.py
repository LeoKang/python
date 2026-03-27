# 2. ---------------------------------
def hello_k(count):
    if count > 0:
        print("Hello")
        hello_k(count - 1)

N, M = map(int, input().split())

hello_k(N)
print()
hello_k(M)

# 1. --------------------------------
def print_hello():
    print("Hello")

N, M = map(int, input().split())
# print(N, M)
for i in range(N):
    print_hello()
print()
for i in range(M):
    print_hello()