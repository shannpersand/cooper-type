translate(width() / 2, height() / 2)

save()

numberOfThings = 200
for i in range(numberOfThings):
    # t = i / (numberOfThings - 1)
    # fill(t, 0.5, 1 - t)
    rect(310, 0, 100, 40)
    rotate(17.28)
    scale(0.996)

restore()

fill(1, 0, 0)
rect(0, 0, 50, 50)
