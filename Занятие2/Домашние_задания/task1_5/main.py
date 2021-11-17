from string import ascii_lowercase, ascii_uppercase, digits
from random import choice, seed

def passgen(ln=8):
    seed()
    ag = ascii_lowercase + ascii_uppercase + digits
    while True:
#        out = ''
#        for _ in range(ln+1):
#            out = out + choice(ag)
        out = (choice(ag) for _ in range(ln+1))
        yield ''.join(out)

if __name__ == "__main__":
    #print(ascii_lowercase)
    #print(ascii_uppercase)
    #print(digits)
    pg = passgen(8)
    print(next(pg))
    print(next(pg))
    print(next(pg))