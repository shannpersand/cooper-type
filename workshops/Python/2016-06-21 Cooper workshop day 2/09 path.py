stroke(1, 0, 0)
strokeWidth(40)

# lineJoin("round")
lineCap("round")

lineDash(0, 70)

# start a new path object
newPath()

# add stuff to the path object
moveTo((100, 100))
lineTo((100, 600))
lineTo((600, 600))
curveTo((644, 202), (432, 132), (220, 100))

# closePath()

# now draw the path
drawPath()
