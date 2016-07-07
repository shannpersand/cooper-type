f = CurrentFont()




for g in f:
    g.prepareUndo("add width")
    # print g.name, g.unicode, g.width
    # g.width = g.width + 50
    # g.rotate(15)
    # g.leftMargin = g.leftMargin + 50
    # g.rightMargin = g.rightMargin + 50
    g.leftMargin +=10
    g.rightMargin += 10
    
#     g = CurrentGlyph()

# print g.width
# print g.leftMargin
# print g.rightMargin

# angledRightMargin (italic)

g.performUndo()