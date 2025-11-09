grammar = r"""

    program: person+ (apply_sc*)? (func_decl*)? scene_decl+
    
    FUNCTION: "function"
    SCENE: "scene"
    IF: "if"
    ELSE: "else"
    ELIF: "else if"
    CHOICE: "choice"
    END: "end"
    LEAVE: "leave"
    RETURN: "return"
    
    scene_decl: SCENE ID ":" stmts? LEAVE
    
    func_decl: FUNCTION ID params? ":" stmts? ret_stmt ";" LEAVE
    params: ID+
    ret_stmt: RETURN args?
    
    apply_sc: apply ";"

    person: person_type STRING ";"
    person_type: "hero" | "friend" | "enemy"

    stmts: (stmt ";" | ";")*
    stmt: if_stmt | choice_stmt | apply

    apply: ID args?
    
    if_stmt: if_arm END (elif_arm END)* (else_arm END)?
    if_arm: IF cond ":" stmts
    elif_arm: ELIF cond ":" stmts
    else_arm: ELSE ":" stmts

    choice_stmt: CHOICE STRING "->" "$" ID

    args: arg ("," arg)*
    arg: STRING | expr | cond

    cond: atomic_cond | apply
    atomic_cond: not_cond (("and" | "or") not_cond)*
    not_cond: "not" not_cond | rel_cond
    rel_cond: expr ("=" | "<>" | "<" | ">" | "<=" | ">=") expr

    expr: add
    add: ("+" | "-")? mul (("+" | "-") mul)*
    mul: atom (("*" | "/" | "//" | "%") atom)*
    atom: NUMBER | ID | "(" expr ")" | apply

    ID: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /([1-9][0-9]*|0)(\.[0-9]+)?/
    STRING: ESCAPED_STRING

    COMMENT: /#[^\r\n]*/

    %import common.ESCAPED_STRING
    %import common.WS

    %ignore WS
    %ignore COMMENT

"""