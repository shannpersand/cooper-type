f = CurrentFont()

# http://unifiedfontobject.org/versions/ufo2/fontinfo.plist/

print f.info.unitsPerEm
print f.info.ascender
print f.info.descender
print f.info.xHeight
print f.info.capHeight

f.info.ascender = 750
print f.info.familyName
print f.info.styleName
print f.info.postscriptFullName
print f.info.openTypeNameLicenseURL

f.kerning["T", "A"] = -100

print f.kerning.keys()
