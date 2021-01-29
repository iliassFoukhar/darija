
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL BREAK CHAR COMMA CONSTANT CONTINUE DIVIDE ELSE EQUALEQUAL EQUALS FALSE FLOATTYPE FLOAT_CONST FOR GTH GTHOREQUAL ID IF INPUT INT INT_CONST LBRACE LPAREN LTH LTHOREQUAL MINUS MODULO NOTEQUAL NUMBER PLUS PRINT RBRACE RETURN RPAREN SEMICOL SIZEOF STRING TIMES TRUE UNION VAR_TYPE VOID WHILE\n    statements : statements statement\n    \n    statements : statement\n    \n    print_statement : PRINT LPAREN expression RPAREN SEMICOL\n                    | PRINT LPAREN STRING RPAREN SEMICOL  \n    \n    vartype_statement : VAR_TYPE LPAREN ID RPAREN SEMICOL\n    \n    union_statement : UNION LPAREN STRING COMMA STRING RPAREN SEMICOL\n    \n    union_statement : UNION LPAREN STRING COMMA ID RPAREN SEMICOL\n    \n    union_statement : UNION LPAREN ID COMMA STRING RPAREN SEMICOL\n    statement : expression SEMICOL\n                 | while_statement\n                 | for_statement\n                 | if_statement\n                 | vartype_statement\n                 | input_statement\n                 | union_statement\n                 | comparison\n                 | compare_id_value\n                 | bool_comparison\n                 | var_statement\n                 | var_assign\n                 | var_inc\n                 | var_dec\n                 | print_statement\n                 | break_statement\n                 \n    var_assign : ID EQUALS ID SEMICOL\n    \n    var_assign : ID EQUALS STRING SEMICOL\n               | ID EQUALS NUMBER SEMICOL\n               | ID EQUALS TRUE SEMICOL\n               | ID EQUALS FALSE SEMICOL\n    \n    var_inc : ID PLUS PLUS SEMICOL\n    \n    var_dec : ID MINUS MINUS SEMICOL\n    \n    var_statement : CHAR ID EQUALS STRING SEMICOL\n                  | FLOATTYPE ID EQUALS NUMBER SEMICOL\n                  | INT ID EQUALS NUMBER SEMICOL\n                  | BOOL ID EQUALS TRUE SEMICOL\n                  | BOOL ID EQUALS FALSE SEMICOL\n    \n        input_statement : INT ID EQUALS INPUT LPAREN INT RPAREN SEMICOL\n                        | CHAR ID EQUALS INPUT LPAREN CHAR RPAREN SEMICOL\n                        | FLOATTYPE ID EQUALS INPUT LPAREN FLOATTYPE RPAREN SEMICOL\n    \n    expression : ID\n    term : ID\n    factor : ID\n    \n    comparison : expression GTH expression\n                  | expression LTH expression\n                  | expression GTHOREQUAL expression\n                  | expression LTHOREQUAL expression\n                  | expression EQUALEQUAL expression\n                  | expression NOTEQUAL expression\n    \n        compare_id_value : ID GTH expression\n                         | ID LTH expression\n                         | ID GTHOREQUAL expression\n                         | ID LTHOREQUAL expression\n                         | ID EQUALEQUAL expression\n                         | ID NOTEQUAL expression \n    \n        bool_comparison : ID EQUALEQUAL ID\n                        | ID EQUALEQUAL TRUE\n                        | ID EQUALEQUAL FALSE\n                        | ID NOTEQUAL ID\n                        | ID NOTEQUAL TRUE\n                        | ID NOTEQUAL FALSE\n    \n        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE\n                     | IF LPAREN compare_id_value RPAREN LBRACE statements RBRACE\n                     | IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE\n    \n        if_statement : IF LPAREN comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE\n                     | IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE\n    \n        while_statement : WHILE LPAREN comparison RPAREN LBRACE statements RBRACE\n                        | WHILE LPAREN TRUE RPAREN LBRACE statements RBRACE\n                        | WHILE LPAREN FALSE RPAREN LBRACE statements RBRACE\n    \n        for_statement : FOR LPAREN var_statement comparison SEMICOL var_inc RPAREN LBRACE statements RBRACE\n    \n        break_statement : BREAK SEMICOL\n    expression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : term MODULO factorterm : factorfactor : NUMBERfactor : LPAREN expression RPARENempty :'
    
_lr_action_items = {'ID':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,26,27,28,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,59,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,107,108,109,110,124,125,126,127,128,129,130,148,154,155,156,157,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[19,19,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,59,63,64,65,-78,67,-77,-1,-9,71,71,59,59,59,59,59,59,59,59,59,59,83,87,91,99,99,99,59,-40,114,115,120,59,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,59,135,136,137,-25,-26,-27,-28,-29,-30,-31,172,19,19,19,182,19,19,19,-5,-34,-32,-33,-35,-36,-3,-4,19,19,19,19,19,19,-66,-67,-68,-61,-62,-63,-6,-7,-8,19,-37,-38,-39,19,19,19,-69,19,19,-64,-65,]),'WHILE':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[21,21,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,21,21,21,21,21,21,-5,-34,-32,-33,-35,-36,-3,-4,21,21,21,21,21,21,-66,-67,-68,-61,-62,-63,-6,-7,-8,21,-37,-38,-39,21,21,21,-69,21,21,-64,-65,]),'FOR':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[23,23,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,23,23,23,23,23,23,-5,-34,-32,-33,-35,-36,-3,-4,23,23,23,23,23,23,-66,-67,-68,-61,-62,-63,-6,-7,-8,23,-37,-38,-39,23,23,23,-69,23,23,-64,-65,]),'IF':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[24,24,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,24,24,24,24,24,24,-5,-34,-32,-33,-35,-36,-3,-4,24,24,24,24,24,24,-66,-67,-68,-61,-62,-63,-6,-7,-8,24,-37,-38,-39,24,24,24,-69,24,24,-64,-65,]),'VAR_TYPE':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[25,25,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,25,25,25,25,25,25,-5,-34,-32,-33,-35,-36,-3,-4,25,25,25,25,25,25,-66,-67,-68,-61,-62,-63,-6,-7,-8,25,-37,-38,-39,25,25,25,-69,25,25,-64,-65,]),'INT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,60,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,165,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[26,26,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,110,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,26,26,26,26,26,26,-5,186,-34,-32,-33,-35,-36,-3,-4,26,26,26,26,26,26,-66,-67,-68,-61,-62,-63,-6,-7,-8,26,-37,-38,-39,26,26,26,-69,26,26,-64,-65,]),'CHAR':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,60,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,167,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[27,27,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,108,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,27,27,27,27,27,27,-5,-34,187,-32,-33,-35,-36,-3,-4,27,27,27,27,27,27,-66,-67,-68,-61,-62,-63,-6,-7,-8,27,-37,-38,-39,27,27,27,-69,27,27,-64,-65,]),'FLOATTYPE':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,60,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,169,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[28,28,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,109,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,28,28,28,28,28,28,-5,-34,-32,188,-33,-35,-36,-3,-4,28,28,28,28,28,28,-66,-67,-68,-61,-62,-63,-6,-7,-8,28,-37,-38,-39,28,28,28,-69,28,28,-64,-65,]),'UNION':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[29,29,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,29,29,29,29,29,29,-5,-34,-32,-33,-35,-36,-3,-4,29,29,29,29,29,29,-66,-67,-68,-61,-62,-63,-6,-7,-8,29,-37,-38,-39,29,29,29,-69,29,29,-64,-65,]),'BOOL':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,60,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[31,31,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,31,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,31,31,31,31,31,31,-5,-34,-32,-33,-35,-36,-3,-4,31,31,31,31,31,31,-66,-67,-68,-61,-62,-63,-6,-7,-8,31,-37,-38,-39,31,31,31,-69,31,31,-64,-65,]),'PRINT':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[32,32,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,32,32,32,32,32,32,-5,-34,-32,-33,-35,-36,-3,-4,32,32,32,32,32,32,-66,-67,-68,-61,-62,-63,-6,-7,-8,32,-37,-38,-39,32,32,32,-69,32,32,-64,-65,]),'BREAK':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[33,33,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,33,33,33,33,33,33,-5,-34,-32,-33,-35,-36,-3,-4,33,33,33,33,33,33,-66,-67,-68,-61,-62,-63,-6,-7,-8,33,-37,-38,-39,33,33,33,-69,33,33,-64,-65,]),'NUMBER':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,57,59,61,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,107,116,118,124,125,126,127,128,129,130,154,155,156,159,160,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[30,30,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,30,-78,-77,-1,-9,30,30,30,30,30,30,30,30,30,30,30,30,30,30,93,30,30,30,30,-40,30,30,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,30,143,147,-25,-26,-27,-28,-29,-30,-31,30,30,30,147,143,30,30,30,-5,-34,-32,-33,-35,-36,-3,-4,30,30,30,30,30,30,-66,-67,-68,-61,-62,-63,-6,-7,-8,30,-37,-38,-39,30,30,30,-69,30,30,-64,-65,]),'LPAREN':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,29,30,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,55,56,57,59,61,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,107,124,125,126,127,128,129,130,142,144,146,154,155,156,161,162,163,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,205,208,209,210,211,212,213,214,215,216,217,218,],[22,22,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,57,22,60,61,62,66,-78,68,-77,-1,-9,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-40,22,22,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,22,-25,-26,-27,-28,-29,-30,-31,165,167,169,22,22,22,22,22,22,-5,-34,-32,-33,-35,-36,-3,-4,22,22,22,22,22,22,-66,-67,-68,-61,-62,-63,-6,-7,-8,22,-37,-38,-39,22,22,22,-69,22,22,-64,-65,]),'$end':([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,164,166,168,170,174,175,176,177,192,193,194,196,197,198,202,203,204,208,209,210,214,217,218,],[0,-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,-5,-34,-32,-33,-35,-36,-3,-4,-66,-67,-68,-61,-62,-63,-6,-7,-8,-37,-38,-39,-69,-64,-65,]),'RBRACE':([2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,30,34,35,36,59,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,106,124,125,126,127,128,129,130,164,166,168,170,174,175,176,177,178,179,180,183,184,185,192,193,194,196,197,198,202,203,204,208,209,210,211,214,215,216,217,218,],[-2,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-73,-78,-77,-1,-9,-40,-70,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,-79,-25,-26,-27,-28,-29,-30,-31,-5,-34,-32,-33,-35,-36,-3,-4,192,193,194,196,197,198,-66,-67,-68,-61,-62,-63,-6,-7,-8,-37,-38,-39,214,-69,217,218,-64,-65,]),'SEMICOL':([3,19,20,30,33,34,59,70,71,72,73,74,75,76,77,78,91,92,93,94,95,96,97,98,99,100,101,106,134,141,143,145,147,150,151,152,153,189,190,191,199,200,201,],[36,-40,-73,-78,69,-77,-40,-71,-41,-72,-43,-44,-45,-46,-47,-48,124,125,126,127,128,129,130,-74,-42,-75,-76,-79,157,164,166,168,170,174,175,176,177,202,203,204,208,209,210,]),'PLUS':([3,19,20,30,34,52,58,59,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,98,99,100,101,105,106,114,122,182,],[37,52,-73,-78,-77,96,37,-40,-71,-41,-72,37,37,37,37,37,37,37,37,37,37,-40,37,-40,37,-74,-42,-75,-76,37,-79,-40,37,52,]),'MINUS':([3,19,20,30,34,53,58,59,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,98,99,100,101,105,106,114,122,],[38,53,-73,-78,-77,97,38,-40,-71,-41,-72,38,38,38,38,38,38,38,38,38,38,-40,38,-40,38,-74,-42,-75,-76,38,-79,-40,38,]),'GTH':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[39,45,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,39,-79,45,]),'LTH':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[40,46,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,40,-79,46,]),'GTHOREQUAL':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[41,47,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,41,-79,47,]),'LTHOREQUAL':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[42,48,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,42,-79,48,]),'EQUALEQUAL':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[43,49,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,43,-79,49,]),'NOTEQUAL':([3,19,20,30,34,59,70,71,72,98,99,100,101,105,106,114,],[44,50,-73,-78,-77,-40,-71,-41,-72,-74,-42,-75,-76,44,-79,50,]),'EQUALS':([19,63,64,65,67,135,136,137,],[51,116,117,118,121,158,159,160,]),'TIMES':([19,20,30,34,59,70,71,72,83,87,98,99,100,101,106,114,],[-41,54,-78,-77,-41,54,-41,54,-41,-41,-74,-42,-75,-76,-79,-41,]),'DIVIDE':([19,20,30,34,59,70,71,72,83,87,98,99,100,101,106,114,],[-41,55,-78,-77,-41,55,-41,55,-41,-41,-74,-42,-75,-76,-79,-41,]),'MODULO':([19,20,30,34,59,70,71,72,83,87,98,99,100,101,106,114,],[-41,56,-78,-77,-41,56,-41,56,-41,-41,-74,-42,-75,-76,-79,-41,]),'RPAREN':([20,30,34,58,59,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,98,99,100,101,102,103,104,106,111,112,113,115,122,123,129,171,172,173,181,186,187,188,],[-73,-78,-77,106,-40,-71,-41,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-40,-53,-56,-57,-40,-54,-59,-60,-74,-42,-75,-76,131,132,133,-79,138,139,140,141,152,153,-30,189,190,191,195,199,200,201,]),'TRUE':([49,50,51,57,121,],[85,89,94,103,150,]),'FALSE':([49,50,51,57,121,],[86,90,95,104,151,]),'STRING':([51,66,68,117,148,149,158,],[92,119,123,145,171,173,145,]),'INPUT':([116,117,118,],[142,144,146,]),'COMMA':([119,120,],[148,149,]),'LBRACE':([131,132,133,138,139,140,195,206,207,],[154,155,156,161,162,163,205,212,213,]),'ELSE':([196,198,],[206,207,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,154,155,156,161,162,163,205,212,213,],[1,178,179,180,183,184,185,211,215,216,]),'statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[2,35,2,2,2,2,2,2,35,35,35,35,35,35,2,35,2,2,35,35,]),'expression':([0,1,22,39,40,41,42,43,44,45,46,47,48,49,50,57,61,68,107,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[3,3,58,73,74,75,76,77,78,79,80,81,82,84,88,105,105,122,105,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'while_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'for_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'if_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'vartype_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'input_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'union_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'comparison':([0,1,57,61,107,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[10,10,102,111,134,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'compare_id_value':([0,1,61,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[11,11,112,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'bool_comparison':([0,1,61,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[12,12,113,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'var_statement':([0,1,60,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[13,13,107,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'var_assign':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'var_inc':([0,1,154,155,156,157,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[15,15,15,15,15,181,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'var_dec':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'print_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'break_statement':([0,1,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'term':([0,1,22,37,38,39,40,41,42,43,44,45,46,47,48,49,50,57,61,68,107,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[20,20,20,70,72,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'factor':([0,1,22,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,55,56,57,61,68,107,154,155,156,161,162,163,178,179,180,183,184,185,205,211,212,213,215,216,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,98,100,101,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements_multiple','Parser.py',61),
  ('statements -> statement','statements',1,'p_statements_single','Parser.py',67),
  ('print_statement -> PRINT LPAREN expression RPAREN SEMICOL','print_statement',5,'p_statement_print','Parser.py',74),
  ('print_statement -> PRINT LPAREN STRING RPAREN SEMICOL','print_statement',5,'p_statement_print','Parser.py',75),
  ('vartype_statement -> VAR_TYPE LPAREN ID RPAREN SEMICOL','vartype_statement',5,'p_statement_vartype','Parser.py',81),
  ('union_statement -> UNION LPAREN STRING COMMA STRING RPAREN SEMICOL','union_statement',7,'p_statement_union','Parser.py',93),
  ('union_statement -> UNION LPAREN STRING COMMA ID RPAREN SEMICOL','union_statement',7,'p_statement_union_two','Parser.py',104),
  ('union_statement -> UNION LPAREN ID COMMA STRING RPAREN SEMICOL','union_statement',7,'p_statement_union_three','Parser.py',129),
  ('statement -> expression SEMICOL','statement',2,'p_statement_expr','Parser.py',153),
  ('statement -> while_statement','statement',1,'p_statement_expr','Parser.py',154),
  ('statement -> for_statement','statement',1,'p_statement_expr','Parser.py',155),
  ('statement -> if_statement','statement',1,'p_statement_expr','Parser.py',156),
  ('statement -> vartype_statement','statement',1,'p_statement_expr','Parser.py',157),
  ('statement -> input_statement','statement',1,'p_statement_expr','Parser.py',158),
  ('statement -> union_statement','statement',1,'p_statement_expr','Parser.py',159),
  ('statement -> comparison','statement',1,'p_statement_expr','Parser.py',160),
  ('statement -> compare_id_value','statement',1,'p_statement_expr','Parser.py',161),
  ('statement -> bool_comparison','statement',1,'p_statement_expr','Parser.py',162),
  ('statement -> var_statement','statement',1,'p_statement_expr','Parser.py',163),
  ('statement -> var_assign','statement',1,'p_statement_expr','Parser.py',164),
  ('statement -> var_inc','statement',1,'p_statement_expr','Parser.py',165),
  ('statement -> var_dec','statement',1,'p_statement_expr','Parser.py',166),
  ('statement -> print_statement','statement',1,'p_statement_expr','Parser.py',167),
  ('statement -> break_statement','statement',1,'p_statement_expr','Parser.py',168),
  ('var_assign -> ID EQUALS ID SEMICOL','var_assign',4,'p_statement_assign_var_id','Parser.py',183),
  ('var_assign -> ID EQUALS STRING SEMICOL','var_assign',4,'p_statement_assign_var','Parser.py',208),
  ('var_assign -> ID EQUALS NUMBER SEMICOL','var_assign',4,'p_statement_assign_var','Parser.py',209),
  ('var_assign -> ID EQUALS TRUE SEMICOL','var_assign',4,'p_statement_assign_var','Parser.py',210),
  ('var_assign -> ID EQUALS FALSE SEMICOL','var_assign',4,'p_statement_assign_var','Parser.py',211),
  ('var_inc -> ID PLUS PLUS SEMICOL','var_inc',4,'p_increment_var','Parser.py',246),
  ('var_dec -> ID MINUS MINUS SEMICOL','var_dec',4,'p_decrement_var','Parser.py',264),
  ('var_statement -> CHAR ID EQUALS STRING SEMICOL','var_statement',5,'p_statement_var','Parser.py',284),
  ('var_statement -> FLOATTYPE ID EQUALS NUMBER SEMICOL','var_statement',5,'p_statement_var','Parser.py',285),
  ('var_statement -> INT ID EQUALS NUMBER SEMICOL','var_statement',5,'p_statement_var','Parser.py',286),
  ('var_statement -> BOOL ID EQUALS TRUE SEMICOL','var_statement',5,'p_statement_var','Parser.py',287),
  ('var_statement -> BOOL ID EQUALS FALSE SEMICOL','var_statement',5,'p_statement_var','Parser.py',288),
  ('input_statement -> INT ID EQUALS INPUT LPAREN INT RPAREN SEMICOL','input_statement',8,'p_input_statement','Parser.py',301),
  ('input_statement -> CHAR ID EQUALS INPUT LPAREN CHAR RPAREN SEMICOL','input_statement',8,'p_input_statement','Parser.py',302),
  ('input_statement -> FLOATTYPE ID EQUALS INPUT LPAREN FLOATTYPE RPAREN SEMICOL','input_statement',8,'p_input_statement','Parser.py',303),
  ('expression -> ID','expression',1,'p_variable_expression','Parser.py',340),
  ('term -> ID','term',1,'p_variable_expression','Parser.py',341),
  ('factor -> ID','factor',1,'p_variable_expression','Parser.py',342),
  ('comparison -> expression GTH expression','comparison',3,'p_expression_comparison','Parser.py',355),
  ('comparison -> expression LTH expression','comparison',3,'p_expression_comparison','Parser.py',356),
  ('comparison -> expression GTHOREQUAL expression','comparison',3,'p_expression_comparison','Parser.py',357),
  ('comparison -> expression LTHOREQUAL expression','comparison',3,'p_expression_comparison','Parser.py',358),
  ('comparison -> expression EQUALEQUAL expression','comparison',3,'p_expression_comparison','Parser.py',359),
  ('comparison -> expression NOTEQUAL expression','comparison',3,'p_expression_comparison','Parser.py',360),
  ('compare_id_value -> ID GTH expression','compare_id_value',3,'p_compare_id_value','Parser.py',400),
  ('compare_id_value -> ID LTH expression','compare_id_value',3,'p_compare_id_value','Parser.py',401),
  ('compare_id_value -> ID GTHOREQUAL expression','compare_id_value',3,'p_compare_id_value','Parser.py',402),
  ('compare_id_value -> ID LTHOREQUAL expression','compare_id_value',3,'p_compare_id_value','Parser.py',403),
  ('compare_id_value -> ID EQUALEQUAL expression','compare_id_value',3,'p_compare_id_value','Parser.py',404),
  ('compare_id_value -> ID NOTEQUAL expression','compare_id_value',3,'p_compare_id_value','Parser.py',405),
  ('bool_comparison -> ID EQUALEQUAL ID','bool_comparison',3,'p_bool_comparison','Parser.py',457),
  ('bool_comparison -> ID EQUALEQUAL TRUE','bool_comparison',3,'p_bool_comparison','Parser.py',458),
  ('bool_comparison -> ID EQUALEQUAL FALSE','bool_comparison',3,'p_bool_comparison','Parser.py',459),
  ('bool_comparison -> ID NOTEQUAL ID','bool_comparison',3,'p_bool_comparison','Parser.py',460),
  ('bool_comparison -> ID NOTEQUAL TRUE','bool_comparison',3,'p_bool_comparison','Parser.py',461),
  ('bool_comparison -> ID NOTEQUAL FALSE','bool_comparison',3,'p_bool_comparison','Parser.py',462),
  ('if_statement -> IF LPAREN comparison RPAREN LBRACE statements RBRACE','if_statement',7,'p_IF','Parser.py',514),
  ('if_statement -> IF LPAREN compare_id_value RPAREN LBRACE statements RBRACE','if_statement',7,'p_IF','Parser.py',515),
  ('if_statement -> IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE','if_statement',7,'p_IF','Parser.py',516),
  ('if_statement -> IF LPAREN comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE','if_statement',11,'p_IF_ELSE','Parser.py',525),
  ('if_statement -> IF LPAREN bool_comparison RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE','if_statement',11,'p_IF_ELSE','Parser.py',526),
  ('while_statement -> WHILE LPAREN comparison RPAREN LBRACE statements RBRACE','while_statement',7,'p_WHILE','Parser.py',537),
  ('while_statement -> WHILE LPAREN TRUE RPAREN LBRACE statements RBRACE','while_statement',7,'p_WHILE','Parser.py',538),
  ('while_statement -> WHILE LPAREN FALSE RPAREN LBRACE statements RBRACE','while_statement',7,'p_WHILE','Parser.py',539),
  ('for_statement -> FOR LPAREN var_statement comparison SEMICOL var_inc RPAREN LBRACE statements RBRACE','for_statement',10,'p_FOR','Parser.py',545),
  ('break_statement -> BREAK SEMICOL','break_statement',2,'p_break_statement','Parser.py',553),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','Parser.py',560),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','Parser.py',564),
  ('expression -> term','expression',1,'p_expression_term','Parser.py',568),
  ('term -> term TIMES factor','term',3,'p_term_times','Parser.py',572),
  ('term -> term DIVIDE factor','term',3,'p_term_div','Parser.py',576),
  ('term -> term MODULO factor','term',3,'p_term_modulo','Parser.py',580),
  ('term -> factor','term',1,'p_term_factor','Parser.py',584),
  ('factor -> NUMBER','factor',1,'p_factor_num','Parser.py',588),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','Parser.py',592),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',597),
]
