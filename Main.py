import random

playing = True
points = 0
playerX = 2
playerY = 2
coinX1 = 0
coinY1 = 2
coinX2 = 3
coinY2 = 4
gameMap = (
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        ["c", " ", "x", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "c", " "]
)

while playing == True:

    print(gameMap[0])
    print(gameMap[1])
    print(gameMap[2])
    print(gameMap[3])
    print(gameMap[4])
    playerInput = input("Points: " + str(points))

    gameMap[playerX][playerY] = "x"
    gameMap[coinX1][coinY1] = "c"
    gameMap[coinX2][coinY2] = "c"

    if playerInput == "w":
        gameMap[playerX][playerY] = " "
        playerX -= 1
        if playerX < 0:
            playerX += 1
    elif playerInput == "a":
        gameMap[playerX][playerY] = " "
        playerY -= 1
        if playerY < 0:
            playerY += 1
    elif playerInput == "s":
        gameMap[playerX][playerY] = " "
        playerX += 1
        if playerX > 4:
            playerX -= 1
    elif playerInput == "d":
        gameMap[playerX][playerY] = " "
        playerY += 1
        if playerY > 4:
            playerY -= 1
    elif playerInput == "q":
        playing = False
    else:
        print(gameMap[0])
        print(gameMap[1])
        print(gameMap[2])
        print(gameMap[3])
        print(gameMap[4])
        playerInput = input(points)
    points -= 5
    if playerX == coinX1 and playerY == coinY1:
        points += 20
        gameMap[coinX1][coinY1] = " "
        coinX1 = random.randint(0,4)
        coinY1 = random.randint(0,4)
        if (playerX == coinX1 and playerY == coinY1) or (coinX2 == coinX1 and coinY2 == coinY1):
            coinX1 = random.randint(0,4)
            coinY1 = random.randint(0,4)
        gameMap[coinX1][coinY1] = "c"
    if playerX == coinX2 and playerY == coinY2:
        points += 20
        gameMap[coinX2][coinY2] = " "
        coinX2 = random.randint(0,4)
        coinY2 = random.randint(0,4)
        if (playerX == coinX2 and playerY == coinY2) or (coinX2 == coinX1 and coinY2 == coinY1):
            coinX2 = random.randint(0,4)
            coinY2 = random.randint(0,4)
        gameMap[coinX2][coinY2] = "c"
    gameMap[playerX][playerY] = "x"


        



