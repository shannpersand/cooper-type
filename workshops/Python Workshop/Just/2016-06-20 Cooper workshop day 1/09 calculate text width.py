targetWidth = 800

rect(100, 100, targetWidth, 800)

fill(1)
font("HoeflerText-BlackItalic")

word = "Typographics"

dummyDefaultSize = 100  # could be anything but 0
fontSize(dummyDefaultSize)
tw, th = textSize(word)  # get width and height of our text

# based on what we got, calculate what it really should be
print targetWidth / tw
calculatedFontSize = dummyDefaultSize * (targetWidth / tw)
print calculatedFontSize

fill(0.8)
fontSize(dummyDefaultSize)
text(word, (100, 576))

fill(1)
fontSize(calculatedFontSize)
text(word, (100, 366))
