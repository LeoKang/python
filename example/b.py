lst = [2, 4, 7, 16, 22, 8, 9]

for x in range(1, len(lst), 2):
    if x< len(lst):
        print(lst[x-1], lst[x])
