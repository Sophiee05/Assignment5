#Assignment1
class Smartphone:
    def __init__(self):
        self.brand = "Vivo"
        self.storage = "64gb"
        self.battery = 100

    def get_brand(self):
        return self.brand

    def get_storage(self):
        return self.storage

    def display_info(self):
        print(f"Smartphone info: {self.get_brand()} {self.get_storage()}")

    def charge_phone(self):
        if self.battery < 50:
            print("Phone needs to be charged")
        elif self.battery >= 100:
            print("Phone fully charged")

phone = Smartphone()
print(phone.get_brand())
print(phone.get_storage())
phone.display_info()
phone.charge_phone()

class Android:
    def use_assistant(self):
        return "Using Google Assistant..."

class Iphone:
    def use_assistant(self):
        return "Using Siri..."

for assistant in [Android(), Iphone()]:
    print(assistant.use_assistant())

#Assignment2
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Ship:
    def move(self):
        return "Sailing"

class Horse:
    def move(self):
        return "Galloping"

for movement in [Car(), Plane(), Ship(), Horse()]:
    print(movement.move())