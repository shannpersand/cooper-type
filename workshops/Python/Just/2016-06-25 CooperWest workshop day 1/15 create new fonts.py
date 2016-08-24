for i in range(3):
    f = NewFont()
    f.info.familyName = "MyNewGreatFontFamily"
    f.info.styleName = "Style" + str(i)

    f.save("MyNewGreatFontFamily-Style" + str(i) + ".ufo")
    f.close()
