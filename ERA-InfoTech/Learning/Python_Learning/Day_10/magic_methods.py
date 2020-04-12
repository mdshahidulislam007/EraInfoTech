class AbstractClass(object):
 
    def __new__(cls, a, b):
        instance = super(AbstractClass, cls).__new__(cls)
        instance.__init__(a, b)
        return 3
 
    def __init__(self, a, b):
        print "Initializing Instance", a, b
