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
    (5, "had ma7ed dyalk 3merha tsala"),
    (6, "Ta malk baghi dkhl shi f shi ?")
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
        elif typee == "manti9i":
            if value == 'vri':
                self.dictionary["value"] = True
            elif value == 'ffo':
                self.dictionary["value"] = False
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
    p[0] = [p[3]]

def p_statement_vartype(p):
    '''
    vartype_statement : VAR_TYPE LPAREN ID RPAREN SEMICOL
    '''
    global errors
    found = variable_exists(p[3])
    if found is not None:
        p[0] = found.get_type()
    else:
        print(errors[2][1])
        pass

def p_statement_union(p):
    '''
    union_statement : UNION LPAREN STRING COMMA STRING RPAREN SEMICOL
    '''
    listy = p[3].split('"') + p[5].split('"')
    result = ""
    for l in listy:
        if l != " ":
            result += l
    p[0] = str(result)

def p_statement_union_two(p):
    '''
    union_statement : UNION LPAREN STRING COMMA ID RPAREN SEMICOL
    '''
    global errors
    found = variable_exists(p[5])
    if found is not None:
        if found.get_type() == 'harf':
            v = found.get_value()
            listy = p[3].split('"')
            result = ""
            for l in listy:
                if l != " ":
                    result += l
            for vv in v.split('"'):
                if vv != " ":
                    result += vv
            p[0] = result
        else:
            print(f'{found.get_name} mashi harf alkhawa')
            pass
    else:
        print(errors[2][1])
        pass

def p_statement_union_three(p):
    '''
    union_statement : UNION LPAREN ID COMMA STRING RPAREN SEMICOL
    '''
    global errors
    found = variable_exists(p[3])
    if found is not None:
        if found.get_type() == 'harf':
            v = found.get_value()
            listy = p[5].split('"')
            result = ""
            for vv in v.split('"'):
                if vv != " ":
                    result += vv
            for l in listy:
                if l != " ":
                    result += l
            p[0] = result
        else:
            print(f'{found.get_name} mashi harf alkhawa')
            pass
    else:
        print(errors[2][1])
        pass

#Size of a string
def p_string_size_statement(p):
    '''
    sizeof_statement : SIZEOF LPAREN STRING RPAREN SEMICOL
    '''
    p[0] = len(p[3]) - 2

def p_id_size_statement(p):
    '''
    sizeof_statement : SIZEOF LPAREN ID RPAREN SEMICOL
    '''
    found = variable_exists(p[3])
    if found is not None:
        if found.get_type() == 'harf':
            p[0] = len(found.get_value()) - 2
#Conditions
def p_statement_expr(p):
    '''statement : expression SEMICOL
                 | if_statement
                 | while_statement
                 | for_statement
                 | vartype_statement
                 | input_statement
                 | union_statement
                 | comparison
                 | compare_id_value
                 | bool_comparison
                 | var_statement
                 | var_assign
                 | var_inc
                 | var_dec
                 | print_statement
                 | break_statement
                 | sizeof_statement
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
               | ID EQUALS TRUE SEMICOL
               | ID EQUALS FALSE SEMICOL
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
        elif found.get_type() == "manti9i":
            if p[3] == 'vri':
                found.set_value(True)
                p[0] = True
            elif p[3] == 'ffo':
                found.set_value(False)
                p[0] = False
            else:
                p[0] = "l motaghayyir dyalk rah {0}".format(found.get_type())
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

def p_decrement_var(p):
    '''
    var_dec : ID MINUS MINUS SEMICOL
    '''
    global errors
    found = variable_exists(p[1])
    if found is None:
        p[0] = f'{p[1]} {errors[2][1]}'
    else:
        if found.get_type() == "sahih":
            found.set_value(found.get_value() - 1)
            p[0] = found.get_value()
        elif found.get_type() == "achari":
            found.set_value(found.get_value() - 1.0)
            p[0] = found.get_value()
        else:
            p[0] = f'{p[1]} {errors[4][1]}'


#Assign New Variable
def p_statement_var(p):
    '''
    var_statement : CHAR ID EQUALS STRING SEMICOL
                  | FLOATTYPE ID EQUALS NUMBER SEMICOL
                  | INT ID EQUALS NUMBER SEMICOL
                  | BOOL ID EQUALS TRUE SEMICOL
                  | BOOL ID EQUALS FALSE SEMICOL
    '''
    
    global variables
    my_var = variable(p[2], p[1], p[4])
    variables[my_var.get_name()] = my_var
    # ERROR Gestion
    p[0] = my_var.get_value()
    

# INPUT From user
def p_input_statement(p):
    '''
        input_statement : INT ID EQUALS INPUT LPAREN INT RPAREN SEMICOL
                        | CHAR ID EQUALS INPUT LPAREN CHAR RPAREN SEMICOL
                        | FLOATTYPE ID EQUALS INPUT LPAREN FLOATTYPE RPAREN SEMICOL
    ''' 
    # Check for errors first
    global errors, variables
    if p[1] != p[6]:
        print(errors[6][1])
        pass
    
    done = False

    #Get the input
    value = input()

    #Check for errors in input
    if p[1] == 'sahih':
        try:
            value = int(value)
            done = True
        except:
            print(errors[0][1])
            pass
    elif p[1] == "achari":
        try:
            value = float(value)
            done = True
        except:
            print(errors[0][1])
            pass

    #Create the variable and store it in the dictionary
    if done == True:
        a = variable(p[2], p[1], value)
        variables[a.get_name()] = a
        #p[0] = a.get_value()
        pass
    
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

# Comparisons
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

def p_compare_id_value(p):
    '''
        compare_id_value : ID GTH expression
                         | ID LTH expression
                         | ID GTHOREQUAL expression
                         | ID LTHOREQUAL expression
                         | ID EQUALEQUAL expression
                         | ID NOTEQUAL expression 
    '''
    found = variable_exists(p[1])
    if found is not None:
        if found.get_type() == 'achari' or found.get_type() == 'sahih':
            value = found.get_value()
        else:
            print('mat9drsh dir had l mo9arana al khawa')
            pass
    else:
        print('motaghayir makaynsh al khawa')
        pass
    
    if p[2] == '>':
        if value > p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<':
        if value < p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '>=':
        if value >= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<=':
        if value <= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '==':
        if value == p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '!=':
        if value != p[3]:
            p[0] = True
        else:
            p[0] = False

# Comparing booleans
def p_bool_comparison(p):
    '''
        bool_comparison : ID EQUALEQUAL ID
                        | ID EQUALEQUAL TRUE
                        | ID EQUALEQUAL FALSE
                        | ID NOTEQUAL ID
                        | ID NOTEQUAL TRUE
                        | ID NOTEQUAL FALSE
    '''
    # Check if the second operand is a variable and if it is the case, check if it exists 
    can = False
    if p[3] != "vri" and p[3] != "ffo":
        found_two = variable_exists(p[3])
        if found_two is not None:
            if found_two.get_type() == 'manti9i':
                value_two = found_two.get_value()
            else:
                print('{0} mashi manti9i'.format(found_two.get_name()))
                
                
        else:
            print('{0} mam3rfash al khawa'.format(p[3]))
            
    elif p[3] == 'vri':
        value_two = True
    elif p[3] == 'ffo':
        value_two = False

    found = variable_exists(p[1])
    if found is not None:
        if found.get_type() == 'manti9i':
            value_one = found.get_value()
            can = True
        else:
            print('{0} mashi manti9i'.format(found.get_name()))
            
    elif found == None:
        print('{0} mam3rfash al khawa'.format(p[1]))
        
    
    if p[2] == "==" and can == True and (value_two == True or value_two == False):
        if value_one == value_two:
            p[0] = True
            
        else:
            p[0] = False
            
    elif p[2] == "!=" and can == True and (value_two == True or value_two == False):
        if value_one == value_two:
            p[0] = False
            
        else:
            p[0] = True
            
    else:
        p[0] = 'kayn shi moshkil'
#IF STATEMENTS
def p_IF(p):
    '''
        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE
                     | IF LPAREN compare_id_value RPAREN LBRACE statements RBRACE
                     | IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE
    '''
    if p[3] == True:
        for pp in p[6]:
            if pp != 'hbes':
                print(pp)
        if 'hbes' in p[6]:
            p[0] = 'hbes'
        else:
            p[0] = None
    else:
        p[0] = None
        

def p_IF_ELSE(p):
    '''
        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
                     | IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
                     | IF LPAREN compare_id_value RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    '''
    if p[3] == True:
        for pp in p[6]:
            if pp != 'hbes':
                print(pp)
        if 'hbes' in p[6]:
            p[0] = 'hbes'
        else:
            p[0] = None
    else:
        for pp in p[10]:
            if pp != 'hbes':
                print(pp)
        if 'hbes' in p[10]:
            p[0] = 'hbes'
        else:
            p[0] = None


#WHILE STATEMENTS
def p_WHILE(p):
    '''
        while_statement : WHILE LPAREN comparison RPAREN LBRACE statements RBRACE
                        | WHILE LPAREN TRUE RPAREN LBRACE statements RBRACE
                        | WHILE LPAREN FALSE RPAREN LBRACE statements RBRACE
    '''
    pass

#FOR STATEMENT
def p_FOR(p):
    '''
        for_statement : FOR LPAREN var_statement comparison SEMICOL var_inc RPAREN LBRACE statements RBRACE
    '''
    #fkoula(sahih a = 1; a < 5; a++;){ task; task; }
    pass

#Break
def p_break_statement(p):
    '''
        break_statement : BREAK SEMICOL
    '''
    p[0] = ['hbes']


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

def build_parser(source):
    global is_running
    #while is_running:
        # try:
        #     #s = input('calc > ')
        #     s = source
        # except EOFError:
        #     break
    s = source
    if not s: 
    #    continue
        return
    #WHILE 
    if "ma7ed" in s:
        #statements = s.split("{")[1].split("}")[0]
        prestatements = s.split("{")
        statements = ""
        for i in range(1, len(prestatements)):
            if i != len(prestatements) - 1:
                statements += prestatements[i] + "{"
            else:
                statements += prestatements[i]
        prestatements = statements.split("}")
        statements = ""
        for i in range(0, len(prestatements) - 1):
            if i != len(prestatements) - 2:
                statements += prestatements[i] + "}"
            else:
                statements += prestatements[i]
        condition = s.split("(")[1].split(")")[0]
        statements = str(statements)
        is_looping = True
        while parser.parse(condition)[0] == True and is_looping == True:
            if is_looping == True:
                result = parser.parse(statements)    
            else:
                break
            if result != None:
                for r in result:
                    if r is not None and r != 'hbes':
                        print(r)
                    elif r is not None and r == 'hbes':
                        is_looping = False
                        break
            
    
    elif "fkoula" in s:
        var       = s.split("(")[1].split(")")[0].split(";")[0] + ";"
        condition = s.split("(")[1].split(")")[0].split(";")[1]
        inc       = str(s.split("(")[1].split(")")[0].split(";")[2] + ";")
        statements= str(s.split("{")[1].split("}")[0])
    
        parser.parse(var)
        is_looping = True
        while parser.parse(condition)[0] == True and is_looping == True:
            result = parser.parse(statements)
            if result is not None:
                for r in result:
                    if r is not None and r != "hbes":
                        print(r)
                    elif r is not None and r == "hbes":
                        is_looping = False
                        break
            parser.parse(inc)
    else:
        result = parser.parse(s)

        if result != None:
            for r in result:
                if r is not None:
                    print(r)


