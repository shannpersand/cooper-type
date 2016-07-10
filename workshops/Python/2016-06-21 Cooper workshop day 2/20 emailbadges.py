f = open("email-addresses.txt")
data = f.read()
f.close()

for email in data.splitlines():
    name, domain = email.split("@")
    newPage(400, 250)
    font("Curlz MT")
    fontSize(100)
    w, h = textSize(name)
    fs = 100 * (width() / w)
    fontSize(fs)
    text(name, (0, height() - 0.8 * fs))
    fontSize(40)
    text(domain, (0, height() - 0.8 * fs - 70))
