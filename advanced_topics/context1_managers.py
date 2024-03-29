"""
context managers are used to manage resources, such as files, database connections, etc.
they ensure that resources are properly acquired and released, even when exceptions occurs.
"""

def equivalent_approach():
    file = open('hello_world.txt', 'w')

    try:
        file.write("form python :D")
    except Exception as e:
        print(f'error: {e}')
    finally:
        file.close()


def context_manager_approach():
    with open('hello_world.txt', mode='w') as file:
        file.write('from python and context manager :D')


if __name__ == '__main__':
    context_manager_approach()
