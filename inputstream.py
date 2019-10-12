class InputStream:


    @classmethod
    def from_path(cls, path):
        return cls(open(path).read())

    def __init__(self, source):
        self.source = source

        self.index = 0
        self.last_index = len(source)

        self.row = 1
        self.column = 1

    def peek(self):
        if self.index >= self.last_index:
            return ''
        return self.source[self.index]

    def next(self):
        character = self.peek()

        if character == '\n':
            self.row += 1
            self.column = 0
        else:
            self.column += 1

        self.index += 1
        return character