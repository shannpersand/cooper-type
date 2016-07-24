# adds spacing
f = CurrentFont()

for g in f:
    g.prepareUndo("add width")
    g.leftMargin += 5
    g.rightMargin += 5
    

g.performUndo()