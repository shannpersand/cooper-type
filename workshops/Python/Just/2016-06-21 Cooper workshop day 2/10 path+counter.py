fill(0.8)
rect(0, 0, 1000, 400)

fill(0.5)
stroke(0)
strokeWidth(3)

newPath()

moveTo((100, 100))
lineTo((100, 600))
lineTo((700, 700))
lineTo((726, 154))
closePath()

# the counter shape needs to go in the
# opposite direction to become a hole.
moveTo((200, 200))
lineTo((560, 200))
lineTo((618, 578))
lineTo((194, 532))
closePath()

drawPath()
