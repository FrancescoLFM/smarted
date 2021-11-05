import os

class smartedFile:
    def __init__(self, filename):
        self.filename = filename
        self.permission = {"readable": os.access(self.filename, os.R_OK), "writable": os.access(self.filename, os.W_OK),
                           "executable": os.access(self.filename, os.X_OK)}

    def fprint(self, read_line):
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

    # Used for checking line number
    # If a line exist it returns 0
    # Else it returns 1
    
    def check_nline(self, nline): 
        with open(self.filename, "r") as f:
            nl = len(f.read().split('\n'))
            if nl < nline or 0 >= nline:
                return 1
            return 0

