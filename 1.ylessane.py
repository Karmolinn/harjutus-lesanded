code:
def pos_func(input_text):
    #pos tagging code:
    texr=input_text
    tokens=tokenize_words(Mina Karmo olen Suur poiss ja ma jooksen.)
    tagged=pos_tag(tokens)
    pos_store(tagged)

def pos_store(tagged):
    verbs=[]
    adjectives=[]
    adverbs=[]
    nouns=[]
    for tag is tagged
         if pos[0]=='V':
          verbs.append(tag[0])
    elif pos[0]=='N':
         nouns.append(tag[0])
    elif pos[0]=='J':
         adjectives.append(tag[0])
    elif pos[0:2]=='RB':
         adverbs.append(tag[0])

