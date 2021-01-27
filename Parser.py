import ply.yacc as yacc
from Lexer import tokens

#variables = []
variables = {}
is_running = True

errors = (
    (0, "Kayn shi moshkil fl input"),
    (1, "l motaghayyir dyalk rah "),
    (2, "variable makaynash"),
    (3, "variable dyalk mashi mn nfs nou3 alkhawa"),
    (4, "machi 3adad rkkez al khawa"),
    (5, "had ma7ed dyalk 3merha tsala")
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
    #result = p[1]
    #for i in range(1,len(p)):
        #if p[i] is not None:
            #print(p[i]) 
            #p[0] += p[i]
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    '''
    statements : statement
    '''
    p[0] = [p[1]]

#Basic Functions
def p_statement_print(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN SEMICOL
                    | PRINT LPAREN STRING RPAREN SEMICOL  
    '''
    p[0] = p[3]



#Conditions
def p_statement_expr(p):
    '''statement : expression SEMICOL
                 | while_statement
                 | if_statement
                 | comparison
                 | var_statement
                 | var_assign
                 | var_inc
                 | print_statement
                 '''
    #print(p[1])
    if isinstance(p[1], list):
        if isinstance(p[1][0], list):
            p[0] = p[1][0][0]
        else:
            p[0] = p[1][0]
    else:
        p[0] = p[1]


#Change value of a variable
def p_statement_assign_var_id(p):
    '''
    var_assign : ID EQUALS ID SEMICOL
    '''
    global errors
    found_one = variable_exists(p[1])
    found_two = variable_exists(p[3])

    if found_one is None and found_two is None:
        p[0] = f'{p[1]} {errors[2][1]}\n{p[3]} {errors[2][1]}'
        pass
    elif found_one is None and found_two is not None:
        p[0] = f'{p[1]} {errors[2][1]}'
        pass
    elif found_two is None and found_one is not None:
        p[0] = f'{p[3]} {errors[2][1]}'
        pass
    
    elif found_one is not None and found_two is not None:
        if found_one.get_type() == found_two.get_type():
            found_one.set_value(found_two.get_value())
        else:
            p[0] = errors[3][2]
    

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

#Increment and decrement variables
def p_increment_var(p):
    '''
    var_inc : ID PLUS PLUS SEMICOL
    '''
    global errors
    found = variable_exists(p[1])
    if found is None:
        p[0] = f'{p[1]} {errors[2][1]}'
    else:
        if found.get_type() == "sahih":
            found.set_value(found.get_value() + 1)
            p[0] = found.get_value()
        elif found.get_type() == "achari":
            found.set_value(found.get_value() + 1.0)
            p[0] = found.get_value()
        else:
            p[0] = f'{p[1]} {errors[4][1]}'

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


#IF STATEMENTS
def p_IF(p):
    '''if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE'''
    if p[3] == True:
        p[0] = p[6]
    else:
        pass

def p_IF_ELSE(p):
    '''
        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    '''
    if p[3] == True:
        p[0] = p[6]
    else:
        p[0] = p[10]


#WHILE STATEMENTS
def p_WHILE(p):
    '''
        while_statement : WHILE LPAREN comparison RPAREN LBRACE statements RBRACE
    '''
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

#def parsii(s):
    #result = parser.parse(s)
    #if result != None:
while is_running:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: 
        continue
    #WHILE 
    if "ma7ed" in s:
        statements = s.split("{")[1].split("}")[0]
        condition = s.split("(")[1].split(")")[0]
        statements = str(statements)
        while parser.parse(condition)[0] == True:
            result = parser.parse(statements)    
            if result != None:
                for r in result:
                    print(r)
    else:
        result = parser.parse(s)

        if result != None:
            for r in result:
                print(r)
   

