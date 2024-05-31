from singleton import Singleton

def test_variable_transference():
    class Dummy:
        def __init__(self, dummy):
            self.dummy = dummy

    Dummy2 = Singleton(Dummy)

    t1 = Dummy2(1)
    t2 = Dummy2()
    t1.dummy = 5
    t3 = Dummy2()
    assert t1.dummy == t2.dummy == t3.dummy


def test_object_identity():
    class Dummy:
        def __init__(self, dummy):
            self.dummy = dummy

    Dummy2 = Singleton(Dummy)

    t1 = Dummy2(1)
    t2 = Dummy2()
    assert t1 is t2


def test_wrapping():
    class Dummy:
        def __init__(self, dummy):
            self.dummy = dummy

    Dummy2 = Singleton(Dummy)

    assert Dummy.__annotations__ == Dummy2.__annotations__
    assert Dummy.__doc__ == Dummy2.__doc__