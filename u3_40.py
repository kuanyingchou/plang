# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

#token: 
#def replace(tokens, grammar):
#    for t in tokens:
#        for g in grammar:
#            if t == g[0]:
#              yield g[1]
#        yield [t]


# should generate a list of tokens through 'yield [token]'

#def expand_token(token, grammar):
#    yielded=False
#    for rule in grammar:
#        if token == rule[0]:
#            yield rule[1]
#            yielded=True
#    if not yielded:
#        yield token
    
# should generate a list of sentences through 'yield [sentence]'
def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + \
                rule[1] + \
                tokens[pos+1:]

            
depth = 1
utterances = [["a", "exp", "exp"]]
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
