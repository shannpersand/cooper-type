newPage("Letter")
save()
fill(1, 0, 0)
rect(10, 20, 300, 400)

fill(0)

f = CurrentFont()
fontName = f.info.familyName

font(fontName)

# openTypeFeatures(smcp=True, c2sc=False)

fontSize(60)
translate(-50, 0)
text("Hello there!",(200, 600))

newPage("Letter")
restore()
fill(0, 1, 0)
rect(10, 20, 300, 400)

saveImage("test.pdf")