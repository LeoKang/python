output = set()

for x in range(10):
    inp = int(input())
    # print(inp)

    output.add(inp % 42)

print(len(output))