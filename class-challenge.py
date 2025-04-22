# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def specs(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."

    def call(self, number):
        return f"Calling {number} from {self.model}..."

# Inherited class
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, stylus_support):
        super().__init__(brand, model, storage)
        self.stylus_support = stylus_support

    def specs(self):
        stylus = "with Stylus support" if self.stylus_support else "no Stylus support"
        return f"{super().specs()} and {stylus}."

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy A51", 128)
phone2 = SmartphonePro("Samsung", "Galaxy Note 20", 256, True)

# Output
print(phone1.specs())
print(phone2.specs())
print(phone2.call("055-123-4567"))