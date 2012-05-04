# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

#token: 
def expand(tokens, grammar):
    res=[]
    for pos in range(len(tokens)):
        for rule in grammar:
            # hmmmm
            # res += [ rule[1] for t in tokens if t == rule[0] ]
            if tokens[pos] == rule[0]:
                res.append(rule[1])
            else:
                res.append(tokens[pos])
    return res  
            
depth = 1
utterances = [["a", "exp"]]
for x in range(depth):
    for sentence in utterances: # a sentence is a list of words(tokens)
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']