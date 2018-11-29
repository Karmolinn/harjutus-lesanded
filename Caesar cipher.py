plaintext = input('sisestage sõnum ')
alphabet = "ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY"
key = 1
cipher = ''

for c in plaintext:
        if c in alphabet:
                cipher += alphabet[ (alphabet.index(c)+key)%(len(alphabet))]

print('teie sõnum on: ' + cipher)
