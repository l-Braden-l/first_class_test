# 
# 
# 

# -- 
class Dog: 
    "A atempt to model a dog"

    def __init__(self, name, age): 
        "init name and age"
        self.name = name
        self.age = age 

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self): 
        print(f'{self.name} rolled over!')