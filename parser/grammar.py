grammar = r"""

    program: person+ top_item*

    person: person_type STRING ";"
    person_type: "hero" | "friend" | "enemy"

    top_item: "scene" scene_decl | apply_stmt

    scene_decl: ID ":" ";" stmts "end" ";" "leave" ";"

    stmts: (stmt ";" | ";")+
    stmt: if_stmt | choice_stmt | apply
    
    apply_stmt: apply ";"

    apply: ID args?

    if_stmt: "if" cond ":" ";" stmts "end" ";" else_stmt?
    else_stmt: "else" (else_only | if_stmt)
    else_only: ":" ";" stmts "end" ";"

    choice_stmt: "choice" STRING "->" "$" ID

    args: arg ("," arg)*
    arg: STRING | expr | cond

    cond: atomic_cond | apply
    atomic_cond: not_cond (("and" | "or") not_cond)*
    not_cond: "not" not_cond | rel_cond
    rel_cond: expr ("=" | "<>" | "<" | ">" | "<=" | ">=") expr

    expr: add
    add: mul (("+" | "-") mul)*
    mul: unary (("*" | "/" | "//" | "%") atom)*
    unary: ("+" | "-")? atom
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