import ply.yacc as yacc
from Lexer import tokens

#variables = []
variables = {}
is_running = True

errors = (
    (0, "Kayn shi moshkil fl input"),
    (1, "l motaghayyir dyalk rah "),
    (2, "variable makaynash")
)

class variable:
    def __init__(self, name, typee, value):
        self.dictionary = {}
        self.dictionary["name"] = name
        self.dictionary["type"] = typee
        if typee == "sahih":
            self.dictionary["value"] = int(value)
        elif typee == "achari":
            self.dictionary["value"] = float(value)
        else:
            self.dictionary["value"] = value

    def __str__(self):
        return "{0} {1} = {2}".format(self.dictionary["type"], self.dictionary["name"], self.dictionary["value"]) 

    def get_value(self):
        return self.dictionary["value"]
    
    def get_type(self):
        return self.dictionary["type"]

    def get_name(self):
        return self.dictionary["name"]
    
    def set_value(self, value):
        self.dictionary["value"] = value

def variable_exists(v):
    global variables
    value = None
    if v in variables.keys():
        value = variables[v]
    else:
        value = None
    return value

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''
    #p[0] = p[1] + [p[2]]
    pass

def p_statements_single(p):
    '''
    statements : statement
    '''
    p[0] = p[1]

#Basic Functions
def p_statement_print(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN SEMICOL
                    | PRINT LPAREN STRING RPAREN SEMICOL  
    '''
    p[0] = p[3]



#Conditions
def p_statement_expr(p):
    '''statement : expression
                 | if_statement
                 | comparison
                 | var_statement
                 | var_assign
                 | print_statement
                 '''
    #print(p[1])
    p[0] = p[1]
#Change value of a variable
def p_statement_assign_var(p):
    '''
    var_assign : ID EQUALS STRING SEMICOL
               | ID EQUALS NUMBER SEMICOL
    '''
    found = variable_exists(p[1])
    if found is not None:
        if found.get_type() == "sahih":
            if isinstance(p[3] , int):
                found.set_value(p[3])
                p[0] = found.get_value()
            else:
                p[0] = "l motaghayyir dyalk rah {0}".format(found.get_type())
        elif found.get_type() == "achari":
            if isinstance(p[3], float):
                found.set_value(p[3])
            else:
                p[0]  = "l motaghayyir dyalk rah {0}".format(found.get_type())
        elif found.get_type() == "harf":
            if isinstance(p[3], str):
                found.set_value(p[3])
            else:
                p[0]  = "l motaghayyir dyalk rah {0}".format(found.get_type())
    else:
        p[0] = "{0} makaynash a lkhawa".format(p[1])

#Assign New Variable
def p_statement_var(p):
    '''
    var_statement : CHAR ID EQUALS STRING SEMICOL
                  | FLOATTYPE ID EQUALS NUMBER SEMICOL
                  | INT ID EQUALS NUMBER SEMICOL
    '''
    
    global variables
    my_var = variable(p[2], p[1], p[4])
    variables[my_var.get_name()] = my_var
    # ERROR Gestion
    p[0] = my_var.get_value()
    
def p_variable_expression(p):
    '''
    expression : ID
    term : ID
    factor : ID
    '''
    global variables
    found = variable_exists(p[1])

    if found == None:
        p[0] = "{0} makaynash a lkhawa".format(p[1])
    else:
        p[0] = found.get_value()


def p_expression_comparison(p):
    '''
    comparison : expression GTH expression
                  | expression LTH expression
                  | expression GTHOREQUAL expression
                  | expression LTHOREQUAL expression
                  | expression EQUALEQUAL expression
                  | expression NOTEQUAL expression
    '''
    if p[2] == '>':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '>=':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<=':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '==':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '!=':
        if p[1] != p[3]:
            p[0] = True
        else:
            p[0] = False



def p_IF(p):
    '''if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE'''
    if p[3] == True:
        p[0] = p[6]
    else:
        pass

#Arithmetic operations
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    'term : term MODULO factor'
    p[0] = p[1] % p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

#Empty
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Kayn shi mushkil f l input !")

# Build the parser
parser = yacc.yacc()

while is_running:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    if result != None:
        print(result)
   

