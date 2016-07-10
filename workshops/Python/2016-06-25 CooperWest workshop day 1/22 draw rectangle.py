def drawRectangle(pen, xMin, yMin, xMax, yMax):
    pen.moveTo((xMin, yMin))
    pen.lineTo((xMin, yMax))
    pen.lineTo((xMax, yMax))
    pen.lineTo((xMax, yMin))
    pen.closePath()


g = CurrentGlyph()

pen = g.getPen()
drawRectangle(pen, 100, 100, 500, 600)
drawRectangle(pen, 200, 700, 400, 900)
