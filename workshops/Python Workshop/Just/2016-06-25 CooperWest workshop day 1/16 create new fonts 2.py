for styleName in ["Light", "Regular", "Bold", "Black"]:
    f = NewFont()
    f.info.familyName = "MyNewGreatFontFamily"
    f.info.styleName = styleName



print AllFonts()
