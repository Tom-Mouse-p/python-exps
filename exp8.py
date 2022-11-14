class A:
    show = "I am class A"
    def _init_(self):
        self.show = "I am class A"
    def display(self):
        print(self.show)


class B(A):
    def _init_(self):
        pass
    def display(self):
        print("This is Child class B of Parent class A", self.show)

class C(A):
    def _init_(self):
        self.show = "/Single Inheritance"
    def display(self):
        print("This is Child class C of Parent class A", self.show)

class P(B, C):
    def _init_(self):
        self.show = "/Multiple Inheritance"
    def display(self):
        print("This is Child class P of Parent class B and C", self.show)


obj1 = A()
obj2 = B()
obj3 = C()
obj4 = P()

obj1.display()
obj2.display()
obj3.display()
obj4.display()
