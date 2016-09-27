nFrames = 10
canvasSize = 500
squareSize = 50

for frame in range(nFrames):
    newPage(canvasSize, canvasSize)
    frameDuration(1/20)
    fill(1)
    rect(0, 0, canvasSize, canvasSize)

    for i in range(10):
        # first square
        fill(0)
        x = randint(0, canvasSize - squareSize)
        y = randint(0, canvasSize - squareSize)
        rect(x, y, squareSize, squareSize)
        # second square
        fill(1, 0, 0)
        x = randint(0, canvasSize - squareSize)
        y = randint(0, canvasSize - squareSize)
        rect(x, y, squareSize, squareSize)

saveImage("simpleanimation.gif")
# saveImage("simpleanimation.mov")
