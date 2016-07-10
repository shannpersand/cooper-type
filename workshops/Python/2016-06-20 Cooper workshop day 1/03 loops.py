# size(1500, 1500)  # the size of the canvas
# size("A4") # some presets available, see sizes()

# print range(2, 12, 3)

numberOfSquares = 7
squareSize = 108
gutter = 14
margin = 52

# this is a "for loop"
for i in range(numberOfSquares):
    x = i * (squareSize + gutter) + margin
    print i, x
    rect(x, margin, squareSize, squareSize)
    #print "hello"

#print "it still exists:", the_loop_variable
