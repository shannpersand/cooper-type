f = CurrentFont()

g = f.newGlyph("a")

pen = g.getPen()

# moves pen to initial position
pen.moveTo((100, 100))

# draws to position
pen.lineTo((100, 600))
pen.lineTo((600, 500))

# draws curve (handle) (handle) (endpoint)
pen.curveTo((600, 200), (400, 100), (200, 100))

# closes path
pen.closePath()

g.update()