# JavaScript: Comments & Keywords
#
# In this exercise you will write token definition rules for all of the
# tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and
# STRING. In addition, you will handle // end of line comments
# as well as /* delimited comments */. 
#
# We will assume that JavaScript is case sensitive and that keywords like
# 'if' and 'true' must be written in lowercase. There are 26 possible
# tokens that you must handle. The 'tokens' variable below has been 
# initialized below, listing each token's formal name (i.e., the value of
# token.type). In addition, each token has its associated textual string
# listed in a comment. For example, your lexer must convert && to a token
# with token.type 'ANDAND' (unless the && is found inside a comment). 
#
# Hint 1: Use an exclusive state for /* comments */. You may want to define
# t_comment_ignore and t_comment_error as well. 

import ply.lex as lex

def test_lexer(lexer,input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result
  
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem. 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

#
# Write your code here. 
#

t_ignore = ' \t\v\r' # whitespace 
t_ignore_comment = r'//[^\n]*'
t_ignore_blockcomment = r'/\*(?:[^*]|\*[^/])*\*/'

t_ANDAND = r'&&'
t_COMMA = r','
t_DIVIDE = r'/'
t_ELSE = r'else'
t_EQUAL = r'='
t_EQUALEQUAL = r'=='
t_FALSE = r'false'
t_FUNCTION = r'function'
t_GE = r'>='
t_GT = r'>'
#       'IDENTIFIER',   #### Not used in this problem.
t_IF = r'if'
t_LBRACE = r'{'
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
#       'NUMBER',       #### Not used in this problem.
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE = r'}'
t_RETURN = r'return'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
#       'STRING',       #### Not used in this problem. 
t_TIMES = r'\*'
t_TRUE = r'true'
t_VAR = r'var'



    
#def t_comment_error(t):
#    print "JavaScript Lexer: Illegal character " + t.value[0]
#    t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character " + t.value[0]
    t.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own. 

lexer = lex.lex() 

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1) == output1

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']
#print test_lexer(input2)
print test_lexer(input2) == output2