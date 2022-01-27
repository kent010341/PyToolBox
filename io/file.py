def read(path):
    opt = ''
    with open(path, 'r') as f:
        opt = f.read()

    return opt

def write(path, string, append=True):
    op = 'a' if append else 'r'

    with open(path, op) as f:
        f.write(string)
