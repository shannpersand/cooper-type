# store a snapshot of the "graphics state", which includes color settings
# as well as the coordinate system
save()

# move the origin of the canvas 200 to the right and 100 up
translate(200, 100)
scale(2)
rotate(15)
# skew(10, 0)

rect(0, 0, 200, 200)

# restore the coordinate system
restore()

fill(1, 0, 0)
rect(0, 0, 100, 100)
