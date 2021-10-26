class smartedFile:
    def __init__(self, filename):
        self.filename = filename

    def print(self, read_line):
        nl = 1
        with open(self.filename, 'r') as f:
            if read_line:
                for line in f.read().split('\n'):
                    print(f'{nl}\t{line}')
                    nl += 1
            else:
                print(f.read())

    def write(self, to_insert, overwrite):
        if not overwrite:
            with open(self.filename, 'a+') as f:
                f.write(to_insert)
        else:
            with open(self.filename, 'w') as f:
                f.write(to_insert)
