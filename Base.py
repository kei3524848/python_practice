class base():
    def a(self):
        print("My name is base.a. I will call base.b")
        self.b()

    def b(self):
        print("My Name is base.b. I'm overrided by der.b")


class der(base):
    def b(self):
        print("Hell yeah! I'm der.b")


b = base()
d = der()
b.a()
d.a()
