class car:
    def __init__(self,model,brand,year):
        self.model = model
        self.brand = brand
        self.year = year

    def display(self):
        print("model:", self.model)
        print("brand:", self.brand)
        print("year:", self.year)
        print("------")
model1= input("enter model: ")
brand1 =input("enter brand: ")
year1 =int(input("enter year number: "))
model12= input("enter model: ")
brand12 = input("enter brand: ")
year12 = int(input("enter year number: "))
s1 = car(model1,year1,brand1)
s2 = car(model12,year12,brand12)
s1.display()
s2.display()