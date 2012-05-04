import ply.lex as lex

tokens = (
    'WHITESPACE',
    'STRING',
    'WORD',
)

def t_WHITESPACE(token):
  r'[ \n]'
  pass
def t_WORD(token):
  r'[^ \t\n]+'
  return token
def t_STRING(token):
  r'"[^"]*"'
  token.value=token.value[1:-1]
  return token


# Define a rule so we can track line numbers
#def t_newline(t):
#    r'\n+'
#    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer

lexer=lex.lex()

# Test it out
data = '''
hello, "wo rld"
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
