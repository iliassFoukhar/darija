import ply.yacc as yacc
from Lexer import tokens

functions = {}
variables = {}
is_running = True

errors = (
    (0, "Kayn shi moshkil fl input"),
    (1, "l motaghayyir dyalk rah "),
    (2, "motaghayir makaynsh"),
    (3, "variable dyalk mashi mn nfs nou3 alkhawa"),
    (4, "machi 3adad rkkez al khawa"),
    (5, "had ma7ed dyalk 3merha tsala"),
    (6, "Ta malk baghi dkhl shi f shi ?"),
    (7, "Ghltti fl i3dadat d dalla a batal")
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


class function:

    def __init__(self, name, parameters, statements):
        # Basics
        self.function_name = name
        self.statements = statements
        # parameters
        if parameters == None:
            self.parameters = None
            self.count = 0
        else:
            self.parameters = {}
            self.array = []
            list_parameters = parameters.split(",")
            for par in list_parameters:
                value = par.split("=")[1]
                typee = par.split(" ")[0]
                if typee == "sahih":
                    value = int(value)
                elif typee == "achari":
                    value = float(value)
                elif typee == "manti9i":
                    if value == "vri":
                        value = True
                    else:
                        value = False
                self.count = len(list_parameters)
                if par.split(" ")[0] != '':
                    namee = par.split(" ")[1]
                else:
                    namee = par.split(" ")[2]
                parameter = variable(namee, typee, value)
                self.parameters[parameter.get_name()] = parameter
                self.array.append(namee)

    def __str__(self):
        return f'{self.function_name}()'

    def parse(self, listy):
        global parser, variables
        for k in self.parameters:
            variables[k] = self.parameters[k]
        for k in range(len(self.array)):
            variables[self.array[k]].set_value(listy[k])
        # print(self.parameters)
        result = parser.parse(self.statements)
        if result != None:
            for r in result:
                if r is not None and r != True and r != False:
                    print(r)
                elif r is not None and r == True:
                    print('vri')
                elif r is not None and r == False:
                    print('ffo')
        for k in self.parameters:
            del variables[k]

# CHECKERS


def variable_exists(v):
    global variables
    value = None
    if v in variables.keys():
        value = variables[v]
    else:
        value = None
    return value


def function_exists(f):
    global functions
    if f in functions.keys():
        return functions[f]
    else:
        return None


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

# Basic Functions


def p_statement_print(p):
    '''
    print_statement : PRINT LPAREN expression RPAREN SEMICOL
                    | PRINT LPAREN STRING RPAREN SEMICOL  
    '''
    #p[0] = [p[3]]
    if isinstance(p[3], str) == True:
        if p[3][0] == '"' and p[3][-1] == '"':
            print(p[3][1:-1])
    else:
        print(p[3])
    p[0] = None


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

# Size of a string


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
# Conditions


def p_statement_expr(p):
    '''statement : expression SEMICOL
                 | if_statement_elif
                 | if_statement
                 | while_statement
                 | for_statement
                 | vartype_statement
                 | input_statement
                 | union_statement
                 | comparison
                 | compare_id_value
                 | compare_id_id
                 | bool_comparison
                 | var_statement
                 | var_assign
                 | var_inc
                 | var_dec
                 | print_statement
                 | break_statement
                 | sizeof_statement
                 | and_statement
                 | or_statement
                 '''
    # print(p[1])
    if isinstance(p[1], list):
        if isinstance(p[1][0], list):
            p[0] = p[1][0][0]
        else:
            p[0] = p[1][0]
    else:
        p[0] = p[1]

# Logical operations


def p_statement_and(p):
    '''
    and_statement : comparison AND comparison
                  | comparison AND TRUE
                  | comparison AND FALSE
                  | TRUE AND comparison
                  | FALSE AND comparison
                  | TRUE AND TRUE
                  | TRUE AND FALSE
                  | FALSE AND TRUE
                  | FALSE AND FALSE
                  | compare_id_value AND compare_id_value
                  | compare_id_value AND TRUE
                  | compare_id_value AND FALSE
                  | compare_id_value AND comparison
                  | comparison AND compare_id_value
                  | TRUE AND compare_id_value
                  | FALSE AND compare_id_value

    '''
    if p[1] == True and p[3] == True:
        p[0] = True
    elif p[1] == True and p[3] == False:
        p[0] = False
    elif p[1] == False and p[3] == False:
        p[0] = False
    elif p[1] == False and p[3] == True:
        p[0] = False


def p_statement_or(p):
    '''
    or_statement  : comparison OR comparison
                  | comparison OR TRUE
                  | comparison OR FALSE
                  | TRUE OR comparison
                  | FALSE OR comparison
                  | TRUE OR TRUE
                  | TRUE OR FALSE
                  | FALSE OR TRUE
                  | FALSE OR FALSE
                  | compare_id_value OR compare_id_value
                  | compare_id_value OR TRUE
                  | compare_id_value OR FALSE
                  | compare_id_value OR comparison
                  | comparison OR compare_id_value
                  | TRUE OR compare_id_value
                  | FALSE OR compare_id_value

    '''
    if p[1] == True or p[3] == True:
        p[0] = True
    else:
        p[0] = False

# Change value of a variable


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
               | ID EQUALS expression SEMICOL
    '''
    found = variable_exists(p[1])
    if found is not None:
        if found.get_type() == "sahih":
            if isinstance(p[3], int):
                found.set_value(p[3])
                #p[0] = found.get_value()
            else:
                print("l motaghayyir dyalk rah {0}".format(found.get_type()))
        elif found.get_type() == "achari":
            if isinstance(p[3], float):
                found.set_value(p[3])
            else:
                print("l motaghayyir dyalk rah {0}".format(found.get_type()))
        elif found.get_type() == "harf":
            if isinstance(p[3], str):
                found.set_value(p[3])
            else:
                print("l motaghayyir dyalk rah {0}".format(found.get_type()))
        elif found.get_type() == "manti9i":
            if p[3] == 'vri':
                found.set_value(True)
                # p[0] = True
            elif p[3] == 'ffo':
                found.set_value(False)
                # p[0] = False
            else:
                print("l motaghayyir dyalk rah {0}".format(found.get_type()))
    else:
        print("{0} makaynash a lkhawa".format(p[1]))
    p[0] = None

# Increment and decrement variables
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
            p[0] = None
        elif found.get_type() == "achari":
            found.set_value(found.get_value() + 1.0)
            p[0] = None
        else:
            print(f'{p[1]} {errors[4][1]}')


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


# Assign New Variable
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

    # Get the input
    value = input()

    # Check for errors in input
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

    # Create the variable and store it in the dictionary
    if done == True:
        a = variable(p[2], p[1], value)
        variables[a.get_name()] = a
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

def p_compare_id_id(p):
    '''
        compare_id_id : ID GTH ID
                      | ID LTH ID
                      | ID GTHOREQUAL ID
                      | ID LTHOREQUAL ID
                      | ID EQUALEQUAL ID
                      | ID NOTEQUAL ID
    '''
    found_one = variable_exists(p[1])
    found_two = variable_exists(p[3])
    print("hh")
    if found_one is not None and found_two is not None:
        if p[2] == ">":
            p[0] = found_one.get_value() > found_two.get_value()
        elif p[2] == "<":
            p[0] = found_one.get_value() < found_two.get_value()
        elif p[2] == ">=":
            p[0] = found_one.get_value() >= found_two.get_value()
        elif p[2] == "<=":
            p[0] = found_one.get_value() <= found_two.get_value()
        elif p[2] == "==":
            p[0] = found_one.get_value() == found_two.get_value()
        elif p[2] == "!=":
            p[0] = found_one.get_value() != found_two.get_value()
        
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
        print('kayn shi moshkil')
        p[0] = None

# IF STATEMENTS
def p_IF(p):
    '''
        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE
                     | IF LPAREN compare_id_value RPAREN LBRACE statements RBRACE
                     | IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE
                     | IF LPAREN and_statement RPAREN LBRACE statements RBRACE
                     | IF LPAREN or_statement RPAREN LBRACE statements RBRACE
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


def p_if_else_if(p):
    '''
    if_statement_elif : IF RPAREN comparison LPAREN LBRACE statements RBRACE ELSE if_statement
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
        p[0] = p[9]


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


# WHILE STATEMENTS
def p_WHILE(p):
    '''
        while_statement : WHILE LPAREN comparison RPAREN LBRACE statements RBRACE
                        | WHILE LPAREN TRUE RPAREN LBRACE statements RBRACE
                        | WHILE LPAREN FALSE RPAREN LBRACE statements RBRACE
    '''
    pass

# FOR STATEMENT
def p_FOR(p):
    '''
        for_statement : FOR LPAREN var_statement comparison SEMICOL var_inc RPAREN LBRACE statements RBRACE
    '''
    pass


# Break
def p_break_statement(p):
    '''
        break_statement : BREAK SEMICOL
    '''
    p[0] = ['hbes']


# Arithmetic operations
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

# Empty


def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Kayn shi mushkil f l input !")


# Build the parser
parser = yacc.yacc()


def build_parser(source):
    global is_running, functions
    # print(f"source: {source}", end=" ")
    # while is_running:
    # try:
    #     #s = input('calc > ')
    #     s = source
    # except EOFError:
    #     break
    s = source
    if not s:
        #    continue
        return
    # WHILE STATEMENT
    if "ma7ed" in s:
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

    # FOR STATEMENT
    elif "fkoula" in s:
        var = s.split("(")[1].split(")")[0].split(";")[0] + ";"
        condition = s.split("(")[1].split(")")[0].split(";")[1]
        inc = str(s.split("(")[1].split(")")[0].split(";")[2] + ";")
        statements = str(s.split("{")[1].split("}")[0])

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
    
    # FUNCTION DECLARATIONS
    elif "dalla" in s:
        parameters = s[s.index("(") + 1: s.index(")")]
        tasks = s[s.index("{") + 1: s.index("}")]
        func_name = s[s.index("dalla") + 6: s.index("(")]
        functionn = function(func_name, parameters, tasks)
        functions[func_name] = functionn
    
    # FUNCTION CALL
    elif "dir" in s and "ila" in s:
        condition = s[s.index("(") + 1: s.index(")")]
        statement = s[s.index("{") + 1: s.index("}")]

        if parser.parse(condition) == [True]:
            build_parser(statement)
        else:
            pass


    elif "dir" in s and "ila" not in s:
        # FUNCTION CALL        
        func_name = s[s.index("dir") + 4: s.index("(")]
        dirr = s[s.index("dir"): s.index("dir") + 3]

        
        if func_name in functions and ")" in s and ";" in s and "(" in s and dirr == "dir":
            pars = s.split("(")[1].split(")")[0]
            if ',' in pars:
                pars = pars.split(",")
            else:
                pars = [pars]

            if len(pars) == functions[func_name].count:
                listy = []

                for par in pars:
                    if isinstance(par, str):
                        found = variable_exists(par)
                        if found != None:
                            valuee = found.get_value()
                            listy.append(valuee)
                            continue
                    if '"' == par[0] and '"' == par[-1]:
                        listy.append(par)
                    elif par == 'vri':
                        listy.append(True)
                    elif par == 'ffo':
                        listy.append(False)
                    elif '.' in par:
                        listy.append(float(par))
                    else:
                        listy.append(int(par))

                functions[func_name].parse(listy)
            else:
                print(errors[7][1])
    

    # ANYTHING ELSE
    else:
        result = parser.parse(s)

        if result != None:
            for r in result:
                if r is not None and r != True and r != False:
                    print(r)
                elif r is not None and r == True:
                    print('vri')
                elif r is not None and r == False:
                    print('ffo')
    

def blockify(source):
    blocks = []
    b = [ "dalla ","ila ", "ma7ed ", "fkoula "]
    s = ["tbe3", "dkhl", "dir", "sahih", "achari", "manti9i", "marka", "harf", "jme3lia", "qyas"]
    i = 0
    j = 0
    while i < len(source):
        block = ""
        j = i + 1
        while j < len(source):
            key = source[i: j+1]        
            # Blocks Of Nested Statements
            if "fkoula" in key or "ila" in key or "ma7ed" in key or "dalla" in key:
                o = 0
                e = 0
                for k in range(j+1, len(source)):
                    if source[k] == '{':
                        o += 1
                    elif source[k] == '}':
                        e += 1
                    if e == o and o != 0:
                        block = source[i: k+1]
                        blocks.append(block)
                        i = k + 1
                        break
            #Ordinary statements
            elif "tbe3"  in key or "dkhl" in key or "dir" in key or  "sahih" in key or "achari" in key or  "manti9i" in key or  "marka" in key or "harf" in key or "jme3lia" in key or "qyas" in key:
                for k in range(j+1, len(source)):
                    if source[k] == ";":
                        block = source[i:k+1]
                        blocks.append(block)
                        i = k + 1
                        break
            j += 1
        i += 1
    return blocks



def run_the_code(source):
    listy = blockify(source)
    for l in listy:
        if l != '' and l != " " and l != "  " and l != "\n" and l != "\n\n" and l != "\n\n\n":
            build_parser(l)
    print("--------------------------------------------------------------------------------")
