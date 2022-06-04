class Person:
    def __init__(self, name, age, role, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
    def __str__(self):
        return f'My name is {self.name} and I am a {self.role}'