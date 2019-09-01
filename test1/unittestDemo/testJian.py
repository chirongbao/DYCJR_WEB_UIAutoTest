class Sub(object):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def testsub(self):
        return self.a - self.b


if __name__ == '__main__':
    a= Sub(3,1)
    print(a.testsub())