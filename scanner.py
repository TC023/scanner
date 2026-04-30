import ply.lex as lex 
import ply.yacc as yacc
keywords = {
    'while': 'WHILE',
    'if': 'IF'
}

tokens = [
    'INTLIT',
    'FLOATLIT',
    'ID',
    'LE',
    'PP'
] + list(keywords.values())

t_ignore = ' \t\n'

t_LE = r'<='
t_PP = r'\+\+'

literals = '+**/%-(){},;='

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    if t.value in keywords.keys():
        t.type = keywords[t.value]
    return t
    
def t_FLOATLIT(t):
    r'[0-9](_?[0-9])*\.[0-9](_?[0-9])*'
    t.value = float(t.value)
    return t
    
def t_INTLIT(t):
    r'[0-9](_?[0-9])*'
    t.value = int(t.value)
    return t

lexer = lex.lex()

# lexer.input("(10 + 5) * 3")
# Tokenize
# while True:
#   tok = lexer.token()
#   if not tok:
#       break   # No more input
#   print(tok)

def p_Term(p):
    """
    Term : Term MulOp Factor
         | Factor
    """

def p_MulOp(p):
    """
    MulOp : '*'
          | '/'
          | '%'
    """



def p_Factor(p):
    """
    Factor : Primary
    """

def p_Primary(p):
    """
    Primary : ID 
            | INTLIT
            | FLOATLIT
            | '(' Term ')'
    """

parser = yacc.yacc()

print(parser.parse("3.1415 * (radius * radius)"))