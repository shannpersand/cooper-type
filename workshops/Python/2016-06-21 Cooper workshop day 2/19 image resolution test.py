betterFactor = 3

canvasSize = 500
size(canvasSize*betterFactor, canvasSize*betterFactor)

scale(betterFactor)

oval(100, 100, 300, 300)

saveImage("resolutiontest.jpg")
