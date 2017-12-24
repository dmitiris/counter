from sys import argv


def read(name):
    with open(name, 'r') as fp:
        counter = int(fp.read())
    return counter


def write(counter):
    with open(name, 'w') as fp:
        fp.write(str(counter))


def main(name):
    try:
        counter = read(name)
        counter += 1
        write(counter)
    except IOError:
        counter = 1
        write(counter)
    return counter


def read_args(args):
    name = '.python.counter' # default name
    action = ''
    try:
        if argv[1] in ['read', '-r']:
            action = 'read'
        elif argv[1] in ['get', '-g']:
            action = ''
        else:
            name = argv[1]
    except IndexError:
        pass
    try:
        name = argv[2]
    except IndexError:
        pass
    return name, action


if __name__=="__main__":
    name, action = read_args(argv)
    if action=='read':
        print read(name)
    else:
        print main(name)
