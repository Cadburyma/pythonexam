class A:
    def A(self):
        print("sangeetha")
class B(A):
    def B(self):
        print("lakshaman")
class C:
    def C(self):
        print("lavanya")
class D(B,C):
    def D(self):
        print("vijay")
O=D()
O.A()
O.B()
O.C()
O.D()
