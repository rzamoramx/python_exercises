# A closure is a function object that remembers values in enclosing scopes even
# if they are not present in memory. 

def local_func():
    def inner():
        print('inner')
    return inner


def closure(x):
    print(f'closure: {x}')
    
    def inner(y):
        print(f'x, y: {x}, {y}')
        return x+y
    return inner


if __name__ == '__main__':
    lf = local_func()
    lf()
    print("-"*30)

    add_numbers = closure(1)
    print(add_numbers(4))
    print("-"*30)
