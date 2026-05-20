def solution(keyinput, board):
    x = 0
    y = 0
    maxx = board[0]//2
    maxy = board[1]//2
    minx = -maxx
    miny = -maxy

    for dir in keyinput:
        if dir=="left":
            if x > minx:
                x-=1
        elif dir=="right":
            if x < maxx:
                x+=1
        elif dir=="down":
            if y > miny:
                y-=1
        elif dir=="up":
            if y < maxy:
                y+=1

    for dir in keyinput:
        # print(dir)
        # match dir:
        #     case "left":
        #         if x > minx:
        #             x-=1
        #     case "right":
        #         if x < maxx:
        #             x+=1
        #     case "down":
        #         if y > miny:
        #             y-=1
        #     case "up":
        #         if y < maxy:
        #             y+=1

    return x, y

keyinput1 = ["left", "right", "up", "right", "right"]
board1 = [11, 11]
keyinput2 = ["down", "down", "down", "down", "down"]
board2 = [7, 9]
print(solution(keyinput1, board1))