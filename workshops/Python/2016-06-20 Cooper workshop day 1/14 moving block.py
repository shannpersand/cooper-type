nFrames = 64
canvasSize = 500
squareSize = 166

def drawSquare(x):
    rect(x - squareSize/2, (canvasSize - squareSize)/2, squareSize, squareSize)

for frame in range(nFrames):
    phase = frame / nFrames
    # print phase
    newPage(canvasSize, canvasSize)
    frameDuration(1/20)
    # draw background
    fill(1)
    rect(0, 0, canvasSize, canvasSize)

    fill(0)
    # print degrees(phase * pi * 2), phase * 360
    s = sin(radians(phase * 360))
    drawSquare(canvasSize * (s + 1) / 2)

saveImage("movingblock-sin.gif")
