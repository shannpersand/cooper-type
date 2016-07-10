# size(1500, 1500)  # the size of the canvas
# size("A4") # some presets available, see sizes()

# print range(2, 12, 3)

numberOfSquares = 5
squareSize = 94
gutter = 21
margin = 110

for j in range(numberOfSquares):
    y = j * (squareSize + gutter) + margin
    for i in range(numberOfSquares):
        print i, j
        x = i * (squareSize + gutter) + margin
        oval(x, y, squareSize, squareSize)
        #print "hello"

saveImage("mygridimage.png")