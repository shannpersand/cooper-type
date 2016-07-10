f = CurrentFont()

g = f.newGlyph("a")

pen = g.getPen()

pen.moveTo((100, 100))
pen.lineTo((100, 600))
pen.lineTo((600, 500))
pen.curveTo((600, 200), (400, 100), (200, 100))
pen.closePath()

g.update()
