from math import sqrt


def find_next_square(sq):
    
    print(str(type(sqrt(sq))) == '<class \'float\'>')
    if str(type(sqrt(sq))) == '<class \'float\'>':
        return -1
    return 'OK'


print(find_next_square(121))
