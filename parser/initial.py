from lark import Lark
from parser import grammar

def parse_to_first_tree(code):
    parser = Lark(grammar.grammar, start="program", parser="lalr", lexer="contextual")
    tree = None
    try:
        tree = parser.parse(code)
    finally:
        if tree:
            print(tree.pretty(' '))
    return tree