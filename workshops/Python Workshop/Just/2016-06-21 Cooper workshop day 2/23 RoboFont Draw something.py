f = CurrentFont()

# for g in f:
#     print g

g = f.newGlyph("b")

pen = g.getPen()

pen.moveTo((100, 100))
pen.lineTo((40, 600))
pen.lineTo((700, 700))
pen.lineTo((726, 154))
pen.closePath()

# the counter shape needs to go in the
# opposite direction to become a hole.
pen.moveTo((200, 200))
pen.lineTo((560, 200))
pen.lineTo((618, 578))
pen.lineTo((194, 532))
pen.closePath()

g.update()
