class calc:
    def add(self,a,b):
        x = a+b
        return x
    def add(self, a, b, c):
        x = a+b+c
        return x
ob = calc()
print(ob.add(1,2,3))
print(ob.add(1,2))
