

__new__ returns an object that has the right type
__init__ initialises the object created by __new__

Explanation:
------------
ex: Consider a class as below:
    
class A(object):
...    def __init__(self, arg):
...       self.arg = arg

a = A('an arg') -- When it is executed; First, Python creates an object that has the right type as below

ex:
tmp = A.__new__(A, 'an arg')
>>> type(tmp)
<class 'A'>

But it will not be initialised.

ex:
tmp.arg
Traceback (most recent call last):
AttributeError: 'A' object has no attribute 'arg'

Second, Python runs our initialisation code which is __init__ as below:

ex:
tmp.__init__('an arg')
tmp.arg
'an arg'

Finally, Python stores the value at a as below:
    
ex:
a = tmp
