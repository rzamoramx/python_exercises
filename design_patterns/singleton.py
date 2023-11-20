"""
singleton pattern
"""


class Singleton(object):
    """
    singleton class
    """
    def __new__(cls):
        """
        override __new__ method
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# usage
s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
