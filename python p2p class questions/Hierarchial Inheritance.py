# base classes
class D():
    def __init__(self, child1name, age1):
        self.child1name = child1name
        self.age1 = age1

class E():
    def __init__(self, child2name, age2):
        self.child2name = child2name
        self.age2 = age2

class F():
    def __init__(self, child3name, age3):
        self.child3name = child3name
        self.age3 = age3

class G():
    def __init__(self, child4name, age4):
        self.child4name = child4name
        self.age4 = age4

# intermediate classes
class B(D, E):
    def __init__(self, father1name, age5, child1name, age1, child2name, age2):
        self.father1name = father1name
        self.age5 = age5

        D.__init__(self, child1name, age1)

        E.__init__(self, child2name, age2)

class C(F, G):
    def __init__(self, father2name, age6, child3name, age3, child4name, age4):
        self.father2name = father2name
        self.age6 = age6

        F.__init__(self, child3name, age3)

        G.__init__(self, child4name, age4)

# derived class
class A(B, C):
    def __init__(self, grandfathername, age7, father1name, age5, father2name, age6, child1name, age1, child2name, age2,
                 child3name, age3, child4name, age4):
        self.grandfathername = grandfathername
        self.age7 = age7

        B.__init__(self, father1name, age5, child1name, age1, child2name, age2)

        C.__init__(self, father2name, age6, child3name, age3, child4name, age4)

    def print_names(self):
        print("Family Tree:")
        print("Grandfather name:", self.grandfathername, "\nGrandfather Age:", self.age7)
        print("Father1 name:", self.father1name, "\nFather1 age:", self.age5)
        print("Children of father1:", self.child1name, "and", self.child2name, "\nTheir ages:", self.age1, "and",
              self.age2, "respectively")
        print("Father2 name:", self.father2name, "\nFather2 age:", self.age6)
        print("Children of father2:", self.child3name, "and", self.child4name, "\nTheir ages:", self.age3, "and",
              self.age4, "respectively")

# driver code
obj = A("shyamlal", "75", "ramlal", "52", "mohanlal", "49", "sita", "26", "geeta", "24", "lakhan", "22", "gopi", "20")
obj.print_names()





