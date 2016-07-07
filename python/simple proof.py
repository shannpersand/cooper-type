newPage("Letter")

# TODO: get text only from the available letters?
# TODO: Auto proof for all open test installed fonts?

# you can change this text
txt = """Bade jut, babus hatreds res I, unhele us bolsheviks presumedly complimentation cowy, engarde boho, won he mesorhiny gummy bocal glycerose breathtakingly edit in evolving jimmy! Obligement mice mite net, am malignify an. Bebar, duluth attn in menu, troy wudge draw misalters tams riden fairest, despairingness nanga so adsmith dilacerating rogued\n
"""


ftxt = FormattedString()
ftxt.font(CurrentFont().info.familyName)
ftxt.fontSize(48)
ftxt.append("Headline!\n")

ftxt.fontSize(18)
ftxt.append(txt)

ftxt.fontSize(16)
ftxt.append(txt)

ftxt.fontSize(14)
ftxt.append(txt)

ftxt.fontSize(12)
ftxt.append(txt)

hyphenation(True)


textBox(ftxt, (50, 30, 500, 700))


newPage("Letter")

ftxt2 = FormattedString()
ftxt2.font(CurrentFont().info.familyName)


ftxt2.fontSize(72)
ftxt2.append("ABCDEFG\nHIJKLMN\nOPQRSTU\nVWXYZ\n")
ftxt2.append("abcdefgh\nijklmnopq\nrstuvwxyz\n")
ftxt2.append("?!:;,.&@#$")

textBox(ftxt2, (100, 20, 500, 700))

saveImage("test.pdf")