txt = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum.

Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum."""


fontList = installedFonts()

# print len(fontList)
margin = 80
gutter = 10
numColumns = 2

for fontName in fontList[400:420]:
    newPage("A4")
    font(fontName)
    fontSize(20)
    text(fontName, (margin, height() - margin))
    fontSize(14)
    hyphenation(True)
    
    columnWidth = (width() - 2 * margin - gutter * (numColumns - 1)) / numColumns
    columnHeight = height() - 300

    copy = txt
    for i in range(numColumns):
        x = margin + i * (columnWidth + gutter)
        y = margin
        fill(0.9)
        rect(x, y, columnWidth, columnHeight)
        fill(0)
        copy = copy.lstrip("\n") # strip any leading blank lines
        copy = textBox(copy, (x, y, columnWidth, columnHeight))

    font("Curlz MT")
    fontSize(14)
    text(str(pageCount()), (margin, margin/2))
