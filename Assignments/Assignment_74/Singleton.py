class c1(object):
    obj=False
    def __new__(cls,a,b):
        if not cls.obj:
            cls.obj = super(c1,cls).__new__(cls)
            print cls.obj
        else:
            raise Exception("Only one object can be allowed")
        return cls.obj
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get(self):
        return self.a,self.b

try:
    print "**Singleton Method**\n"
    o1=c1(10,20)
    print o1.get()
    o2=c1(100,200)
    o3=c1(1000,2000)
except Exception as err:
    print err

