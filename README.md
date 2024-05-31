# Singleton

Create Singleton classes simply by decorating them.

The package is
1. complete. it's tiny, but does exactly what it says.
2. free from trickery. No metaclasses, inheritance or hidden modifications, just a simple decorator for the constructor call.
3. easily modifiable. Does the package not fulfil all your needs anymore? Are you on an incomplatible python version? Just copy the file over and adapt it yourself, it's not even twenty LLoC!


```python
from dead_simple_singleton import Singleton


@Singleton
class DummyClass:
    def __init__(self, dummy_var):
        self.dummy_var = dummy_var

t1 = DummyClass(5)
t2 = DummyClass(3)

assert t1 is t2 # True
assert t1.dummy_var == t2.dummy_var # True
```