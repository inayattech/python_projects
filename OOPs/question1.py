class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"    
    
class ElecticCar(Car):
    def __init__(self,brand,model,battery_size):   
        super().__init__(brand,model)
        self.battery_size = battery_size

tesla = ElecticCar("tesla","supers","85KWH")
print(tesla.full_name())
print(tesla.battery_size)

# result = Car("Toyota","Corolla")
# print(result.brand)
# print(result.model) 
# print(result.full_name())