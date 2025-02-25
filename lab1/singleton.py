"""
    Реалізація патерну Одинак (Singleton)
"""
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'value'):
            self.value = value


if __name__ == "__main__":
    s1 = Singleton("First instance")
    s2 = Singleton("Second instance")

    print(s1.value)
    print(s1.value)
    print(s1 is s2)

