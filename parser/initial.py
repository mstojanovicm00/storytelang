from lark import Lark
from parser import grammar

def write_tree(tree, filename):
    with open(filename, "w") as f:
        f.write(tree.pretty('\t'))

def parse_to_first_tree(code):
    parser = Lark(grammar.grammar, start="program", parser="lalr", lexer="contextual")
    tree = None
    try:
        tree = parser.parse(code)
    finally:
        if tree:
            write_tree(tree, 'tree.txt')
        else:
            print("No tree was generated")
    return tree