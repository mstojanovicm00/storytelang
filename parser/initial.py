from lark import Lark
from parser import grammar

def parse_to_first_tree(code):
    parser = Lark(grammar.grammar, start="program")
    return parser.parse(code)