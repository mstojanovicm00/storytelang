from codereader.code import Code
from parser import initial

if __name__ == '__main__':
    code = Code('exam.story')
    code.write()
    tree = initial.parse_to_first_tree(code.get())
    s = tree.pretty(' ')
    print(s)
    pass