alphabet = "abcdefghijklmnopqrstuvwxyz"
cap = alphabet.upper()


#for letter in cap:
#    print 'HH' + letter + 'H' + letter + 'O' + letter + 'OO'

# for letter in cap:
#     for otherLetter in cap:
#         print letter + otherLetter + letter + otherLetter,

for letter in cap:
    for otherLetter in cap:
        print 'HH' + letter + otherLetter + 'HH'