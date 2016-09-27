# f = OpenFont("DemoFonts/SourceSansPro_0_subset.ufo")

# for styleName in ["light","regular","bold"]


for i in range(2)
    f = NewFont()
    f.info.familyName = "New Family Name"
    f.info.styleName = "Style" + str(i)
    
    f.save("My new familt" + str(i) + ".ufo")
    f.close()

print AllFonts()


a = hi
b = there

for i in range(3):
    print a + " " + b + str(i)