
def positional(arg1, arg2):
    pass


def keyword(arg1, arg2_name=1.2):
    print(f'arg1: {arg1}, arg2_name: {arg2_name}')


def kwargs(arg1, *kwargs1, **kwargs2):
    print(f'tuple: {kwargs1}')
    print(f'dict: {kwargs2}')


if __name__ == '__main__':
    keyword('string')
    kwargs('foo', *('bar', '123'), **{"foo": "bar"})
