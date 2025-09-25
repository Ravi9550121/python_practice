



class Phones:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost


p1 = Phones()
p1.set_color("red")  # Correct method call
p1.set_cost(10000)   # Correct method call

print(p1.show_color())  # To actually see output
print(p1.show_cost())   # To actually see output














class mobile:
    
    def set_number(self,number):
        self.number=number
    def set_contactname(self,contactname):
        self.contactname=contactname
    def show_number(self):
        return self.number
    def show_contactname(self):
        return self.contactname



p1=mobile()

p1.set_number(9999988888)

p1.set_contactname("amagi")

print(p1.show_number())


print(p1.show_contactname())
