#!/usr/bin/python3

from sys import argv, exit

if len(argv) > 1: incomingroute = argv[1]
else: incomingroute = '/'

print("Incoming route: '%s'" % incomingroute)

def route(route, *rargs):
    print("  - Create decorator for route '%s'." % route)
    def decorator(func):
        print('    - Create wrapper.')
        if incomingroute == route:
            print('      - Route match')
            print('      - Function behinds decoration starts.')
            func(*rargs)
            exit()
        print('      - No route. Next..')
        if route == '*':
            print('      - Create defaults wrapper')
            def wrapper(*args):
                print('        - wrapper starts.')
                res = func(*args)
                return res
            return wrapper
        return None
    return decorator

@route('*')
def default(ir):
    print("        # Called other - '%s'." % ir)

@route('/')
def root(*args, **kwargs):
    print("        # Called '/' with params: {}, {}".format(args, kwargs))

@route('/login', 'UserName', 'Secret')
def login(usr, pswd):
    print("        # Called '/login' for '%s' with '%s'." % (usr, pswd))

@route('/logoff', 'UserName')
def logoff(usr):
    print("        # Called '/logoff' for '%s'." % usr)

default(incomingroute)
