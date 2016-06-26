def thisFunction(string):
    print string + " " + "hello function"
    
thisFunction('thing')

g = CurrentGlyph()
useThisPen = g.getPen()


def drawRectangle(pen, xMin, yMin, xMax, yMax):
    pen.moveTo((xMin, yMin))
    pen.lineTo((xMin, yMax))
    pen.lineTo((xMax, yMax))
    pen.lineTo((xMax, yMin))
    pen.closePath()

drawRectangle(useThiesPen, 100, 100, 500, 600)

