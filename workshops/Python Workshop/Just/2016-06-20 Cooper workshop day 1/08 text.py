for fontName in installedFonts():
    if fontName.startswith("Hoef"):
        print fontName

font("HoeflerText-BlackItalic")
fontSize(100)
lineHeight(90)
text("Typographic\nsssssssss", (100, 96))

# fill(0.8)
# rect(10, 200, 800, 500)
fill(0)
font("HoeflerText-Regular")
# openTypeFeatures()
print listOpenTypeFeatures()
openTypeFeatures(lnum=False, pnum=True, smcp=True)
fontSize(60)
lineHeight(60)
textBox("0123456789 ABCabc " * 12, (92, 270, 806, 646))
