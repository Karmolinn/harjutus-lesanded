valid_dna = "ACGT"
sequence = input('pane üks järjestus: ').upper()
condition = all(i in valid_dna for i in sequence)
print('kehtiv järjestus') if condition else print ('ei ole kehtiv järjestus')
if count==1:
    print