import ply.lex as lex

#A list of literals
literals = ('{', '}')

#A list of reserved words
reserved = {
    'error'       : 'ID',
    'tbe3'        : 'PRINT',
    'sahih'       : 'INT',
    'hbes'        : 'BREAK', 
    'dkhl'        : 'INPUT',
    'oula'        : 'ELSE',
    'marka'       : 'VAR_TYPE',
    'harf'        : 'CHAR', 
    'reje3'       : 'RETURN', 
    'jme3lia'     : 'UNION', 
    'kemel'       : 'CONTINUE',     
    'fkoula'      : 'FOR',
    'dalla'       : 'FUNCTION',
    'ila'         : 'IF',
    'ma7ed'       : 'WHILE',
    'qyas'        : 'SIZEOF',
    'achari'      : 'FLOATTYPE',
    'manti9i'     : 'BOOL',
    'vri'         : 'TRUE',
    'ffo'         : 'FALSE',
    'o'           : 'AND',
    'aw'          : 'OR'
}


# List of token names
tokens =(
    "GTH",
    "LTH",
    "GTHOREQUAL",
    "LTHOREQUAL",
    "EQUALEQUAL",
    "NOTEQUAL",
    'NUMBER',
    'FLOAT_CONST',
    'INT_CONST',
    'STRING',
    'PLUS',
    'MINUS',
    'MODULO',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'RBRACE',
    'LBRACE',
    'SEMICOL',
    'EQUALS',
    'COMMA'
) + tuple(reserved.values())  


# Regular expression rules for simple tokens
t_EQUALEQUAL = r'=='
t_GTH        = r'>'
t_LTH        = r'<'
t_GTHOREQUAL = r'>='
t_LTHOREQUAL = r'<='
t_NOTEQUAL   = r'!='
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_SEMICOL    = r';'
t_EQUALS     = r'='
t_MODULO     = r'%'
t_COMMA      = r'\,'

#Check for curly braces
def t_LBRACE(t):
    r'\{'
    t.type = 'LBRACE'      
    return t


def t_RBRACE(t):
    r'\}'
    t.type = 'RBRACE'    
    return t

#Check for reserved words 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')  
    return t
    

def t_STRING(t):
    r'\"(\\.|[^"\\])*\"'
    t.value = str(t.value)
    return t


# A regular expression rule for integers
def t_NUMBER(t):
    r'-?[0-9]*\.?[0-9]+((E|e)(\+|-)?[0-9]+)?'
    try:
        t.value = int(t.value)
        t.type = 'NUMBER'
        return t
    except ValueError:
        pass

    try:
        t.value = float(t.value)
        t.type = 'NUMBER'
        return t
    except ValueError:
        pass


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
t_ignore_COMMENT = r'\#.*'


# Error handling rule
def t_error(t):
    print("Achno hiya had: '%s'" % t.value[0])
    t.lexer.skip(1)


# End of file rule
def t_eof(t):
    #more = input('>>> ')
    more = "khrej()"
    if more and more != "khrej" and more != "khrej()":
        lexer.input(more)
        return lexer.token()
    elif more=="khrej()":
        return None
    elif more=="khrej":
        more = input("Wach bghiti tgol khrej()?\n>>> ")
    return None

lexer = lex.lex()

def build_lexer(source_code):
    lexer.input(source_code)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            print("Nihayat l barnamaj, ila lli9a2")
            break  
        print(tok)