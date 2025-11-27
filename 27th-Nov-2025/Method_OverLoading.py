class ops:
    def add(self,a,b=0,c=0):
        return a+b+c
m=ops()
print(m.add(1,2))
print(m.add(1))
print(m.add(1,2,3))

################################################################################3

#args is used for any number of argument, it does not have any limit

class ops:
    def add(self,*args):
        return sum(args)
m=ops()
print(m.add(1,2,3,4,5))
print(m.add(1))
print(m.add(1,2,3))
