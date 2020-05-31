from nltk.corpus import wordnet
syns =wordnet.synsets("hot")
print(syns)
#just the word
print(syns[0].lemmas()[0].name())
print("\n")
#definition
print(syns[4].definition())
print("\n")
#examples
print(syns[4].examples())
print("\n")
synonyms=[]
antonyms=[]

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        # print("l:",l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print("\n")
print(set(antonyms))

w1=wordnet.synset("boat.n.01")
w2=wordnet.synset("ship.n.01")
print(w1.wup_similarity(w2))


w1=wordnet.synset("boat.n.01")
w2=wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1=wordnet.synset("boat.n.01")
w2=wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2))


