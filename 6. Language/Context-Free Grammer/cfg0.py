import nltk

grammer = nltk.CFG.fromstring('''
    S -> NP VP
    
    NP -> D N | N
    VP -> V NP | V
    
    D -> "the" | "an" | "a"
    N -> "She" | "city" | "car" | "airplane"
    V -> "saw" | "walked" | "hear" | "has"
''')

parser = nltk.ChartParser(grammer)

sentence = input("Sentence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()
except ValueError:
    print("Not Possible")