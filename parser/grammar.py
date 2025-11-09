grammar = r"""

    program: person+ (apply_sc*)? (func_decl*)? scene_decl+
    
    scene_decl: "scene" ID ":" stmts? "leave"
    
    func_decl: "function" ID params? ":" stmts? ret_stmt ";" "leave"    
    params: ID+
    ret_stmt: "return" args?
    
    apply_sc: apply ";"

    person: person_type STRING ";"
    person_type: "hero" | "friend" | "enemy"

    stmts: stmt*
    stmt: if_stmt | choice_stmt | apply_sc | ";"

    apply: ID args?
    
    if_stmt: if_arm "end" ";" (elif_arm "end" ";")* (else_arm "end" ";")?
    if_arm: "if" (cond | apply) ":" stmts
    elif_arm: "else" "if" cond ":" stmts
    else_arm: "else" ":" stmts

    choice_stmt: "choice" STRING "->" "$" ID ";"

    args: arg ("," arg)*
    arg: STRING | expr | cond

    cond: atomic_cond
    atomic_cond: not_cond (("and" | "or") not_cond)*
    not_cond: "not" not_cond | rel_cond
    rel_cond: expr ("=" | "<>" | "<" | ">" | "<=" | ">=") expr

    expr: add
    add: ("+" | "-")? mul (("+" | "-") mul)*
    mul: atom (("*" | "/" | "//" | "%") atom)*
    atom: NUMBER | apply | "(" expr ")"

    ID: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /([1-9][0-9]*|0)(\.[0-9]+)?/
    STRING: ESCAPED_STRING

    COMMENT: /#[^\r\n]*/

    %import common.ESCAPED_STRING
    %import common.WS

    %ignore WS
    %ignore COMMENT

"""