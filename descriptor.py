class DescriptorPractice:
    x = 1
    y = 2

    def __init__(self, z):
        self.z = z

    class MyDescriptor:
        def __get__(self, obj, objtype):
            print('Retrieving', self.name)
            return self.val

    class MyGetAttr:
        def __getattr__(self, name):
            print('Caught a not found attr:', name)


d = DescriptorPractice(3)
print('x is', d.x)
print('y is', d.y)
print('d object is', d)
print('DescriptorPractice class is', DescriptorPractice)
print('type(d) is', type(d))
print('DescriptorPractice class dictionary is', DescriptorPractice.__dict__)
print('d object dictionary is', d.__dict__)

# Below throws runtime error because it's a class reference, and the method is expecting 'self' as the 1st arg
#print(DescriptorPractice.MyGetAttr.__getattr__('shit'))
print(DescriptorPractice.MyGetAttr().shit)
