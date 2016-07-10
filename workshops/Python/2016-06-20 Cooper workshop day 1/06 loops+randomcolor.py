# size(1500, 1500)  # the size of the canvas
# size("A4") # some presets available, see sizes()

# print range(2, 12, 3)

numberOfSquares = 8
squareSize = 94
gutter = 21
margin = 60
# doRectangle = False


for j in range(numberOfSquares):
    y = j * (squareSize + gutter) + margin
    for i in range(numberOfSquares):
        # print i, j
        x = i * (squareSize + gutter) + margin
        fill(random(), random(), random())
        if random() > 0.5:
            rect(x, y, squareSize, squareSize)
        else:
            oval(x, y, squareSize, squareSize)


# saveImage("mygridimage.png")
