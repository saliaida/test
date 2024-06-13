class Test:
    def __init__(self):
        self.a = 10
        self._b = None
        self.__c = 30
        
class Sub(Test):
    def __init__(self):
        Test.__init__(self)
        # print(self.__c)
    pass


_x = 5
__y = 6

print('************')
def _xx():
    print('******')
    
def __yy():
    print('++++++++')    

# t1 = Test()
# t1.a = 100
# print(t1.a)
# t1._b = 200
# print(t1._b)
# t1.__c = 300
# # print(t1.__c)

# s1 = Sub()
# s1._b = 200
# print(s1._b)
# t1.a = 100
