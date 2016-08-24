f = CurrentFont()

for g in f:
    # print g.name, g.unicode, g.width
    # g.width = g.width + 50
    g.leftMargin += 50  # shortcut for: g.leftMargin = g.leftMargin + 50
    g.rightMargin += 50
    # g.rotate(-15)

