
def do_four(f,val):
    f(val)
    f(val)
    f(val)
    f(val)

def print_word(word):
    print(word)

do_four(print_word,"fridah is awesome so awesomeeeeee")
do_four(print_word,"i am blessed, I am forgiven, I am in the best place everrrr")

# lets do some patterns babyyyy :)

def height():
    print('+', ' -'*4, '+', ' -'*4, '+', ' -'*4, '+', ' -'*4, '+')
    print(' |', '  '*4 +'  ', '|', '  '*4 +'  ', '|',  '  '*4 +'  ', '|', '  '*4 +'  ', '|')
    print(' |', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|')
    print(' |', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|')
    print(' |', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|', '  '*4 +'  ', '|')

def twice(f):
    f()
    f()
    f()
    f()

twice(height)
print('+', ' -'*4, '+', ' -'*4, '+',' -'*4, '+', ' -'*4, '+')

print('+', end = ' ')
print('-')

def horizontal():
    pass
    
