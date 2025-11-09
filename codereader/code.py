def read_file(filename):
    with open(filename, encoding='UTF-8') as f:
        lines = [line.rstrip() for line in f]
        lines = list(map(lambda line: line + ' ; ', lines))
        res = []
        tabs = 0
        for line in lines:
            count = 0
            s = line[:]
            while s.startswith('\t'):
                count += 1
                s = s[1:]
            if not s.strip():
                continue
            if count < tabs:
                for i in range(tabs - count):
                    res.append(" end ; ")
            res.append(s)
            tabs = count
        return "\n".join([i.strip() for i in res if i.strip() != ';'])

class Code:
    def __init__(self, filename):
        self.code = read_file(filename)

    def get(self):
        return self.code

    def write(self):
        with open('modified.story', 'w') as f:
            f.write(self.code)